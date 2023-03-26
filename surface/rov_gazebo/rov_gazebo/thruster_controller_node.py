from typing import List

import time
import copy
import rclpy
from geometry_msgs.msg import Twist, Vector3
from rclpy.node import Node, Publisher
from std_msgs.msg import Float64
from geometry_msgs.msg import PoseStamped
from tf2_msgs.msg import TFMessage
from interfaces.msg import ROVControl, Armed

# Range of values Pixhawk takes
# In microseconds
ZERO_SPEED: int = 1500
RANGE_SPEED: int = 400


class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node", parameter_overrides=[])
        self.thrusters = [
            "top_front_left",
            "top_front_right",
            "top_back_left",
            "top_back_right",
            "bottom_front_left",
            "bottom_front_right",
            "bottom_back_left",
            "bottom_back_right",
        ]

        self.linear_scale = 1
        self.angular_scale = 1
        self.multiplier = 3

        self.publishers_: List[Publisher] = []
        self.sub_keyboard = self.create_subscription(
            ROVControl, "/manual_control", self.control_callback, qos_profile=10
        )
        self.pos_sub = self.create_subscription(
            TFMessage, "/simulation/rov_pose", self.pos_callback, qos_profile=10
        )
        self.arm_sub = self.create_subscription(
            Armed, "/armed", self.arm_callback, qos_profile=10
        )
        self.is_armed = False
        self.control_msg = Twist()
        self.prev_pose = PoseStamped()
        self.pose = PoseStamped()

    def arm_callback(self, msg: Armed):
        self.is_armed = msg.armed
        self.get_logger().info("Got Armed message: " + str(self.is_armed))

    def pos_callback(self, msg: TFMessage):
        # msg[0] is a pose of ROV body
        self.prev_pose = copy.deepcopy(self.pose)
        cur_time = time.time()
        time_sec = int(cur_time)
        time_nsec = int((cur_time - time_sec) * 1e9)
        self.pose.header.stamp.sec = time_sec
        self.pose.header.stamp.nanosec = time_nsec
        self.pose.pose.position.x = msg.transforms[0].transform.translation.x
        self.pose.pose.position.y = msg.transforms[0].transform.translation.y
        self.pose.pose.position.z = msg.transforms[0].transform.translation.z
        self.pose.pose.orientation.x = msg.transforms[0].transform.rotation.x
        self.pose.pose.orientation.y = msg.transforms[0].transform.rotation.y
        self.pose.pose.orientation.z = msg.transforms[0].transform.rotation.z
        self.pose.pose.orientation.w = msg.transforms[0].transform.rotation.w
        self.control()

    def control_callback(self, msg: ROVControl):
        if not self.is_armed:
            return

        twist = Twist(
            linear=Vector3(
                x=float((msg.x - ZERO_SPEED) / RANGE_SPEED * self.linear_scale),
                y=float((msg.y - ZERO_SPEED) / RANGE_SPEED * self.linear_scale),
                z=float((msg.z - ZERO_SPEED) / RANGE_SPEED * self.linear_scale),
            ),
            angular=Vector3(
                x=float((msg.roll - ZERO_SPEED) / RANGE_SPEED * self.angular_scale),
                y=float((msg.pitch - ZERO_SPEED) / RANGE_SPEED * self.angular_scale),
                z=float((msg.yaw - ZERO_SPEED) / RANGE_SPEED * self.angular_scale),
            ),
        )
        self.control_msg = twist  # for stablization

    def create_publishers(self, msg_type: type, qos_profile: int = 10):
        ns: str = self.get_namespace()
        for thruster in self.thrusters:
            topic = (
                f"{ns}/model/rov/joint/thruster_{thruster}_body_blade_joint/cmd_thrust"
            )
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def control(self):
        thrust_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        msg = self.control_msg
        thrust_list = self.x_control(msg.linear.x, thrust_list)
        thrust_list = self.y_control(msg.linear.y, thrust_list)
        thrust_list = self.z_control(msg.linear.z, thrust_list)
        thrust_list = self.roll_control(msg.angular.x, thrust_list)
        thrust_list = self.pitch_control(msg.angular.y, thrust_list)
        thrust_list = self.yaw_control(msg.angular.z, thrust_list)
        thrust_list = self.stablize(msg, thrust_list)
        self.publish_thrust(thrust_list)

    def x_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[0] += thrust
        thrust_list[1] -= thrust
        thrust_list[2] -= thrust
        thrust_list[3] += thrust
        return thrust_list

    def y_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[0] -= thrust
        thrust_list[1] -= thrust
        thrust_list[2] -= thrust
        thrust_list[3] -= thrust
        return thrust_list

    def z_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[4] += thrust
        thrust_list[5] += thrust
        thrust_list[6] += thrust
        thrust_list[7] += thrust
        return thrust_list

    def roll_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[4] -= thrust
        thrust_list[5] += thrust
        thrust_list[6] -= thrust
        thrust_list[7] += thrust
        return thrust_list

    def pitch_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[4] -= thrust
        thrust_list[5] -= thrust
        thrust_list[6] += thrust
        thrust_list[7] += thrust
        return thrust_list

    def yaw_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        thrust_list[0] -= thrust
        thrust_list[1] -= thrust
        thrust_list[2] += thrust
        thrust_list[3] += thrust
        return thrust_list

    def stablize(self, control_msg: Twist, thrust_list: List[float]):
        # stablize directions or rotations when it is 0.0
        coeff = 1000
        if control_msg.linear.x == 0.0:
            diff = self.pose.pose.position.x - self.prev_pose.pose.position.x
            thrust_list = self.x_control(-1 * diff * coeff, thrust_list)
        if control_msg.linear.y == 0.0:
            diff = self.pose.pose.position.y - self.prev_pose.pose.position.y
            thrust_list = self.y_control(-1 * diff * coeff, thrust_list)
        if control_msg.linear.z == 0.0:
            diff = self.pose.pose.position.z - self.prev_pose.pose.position.z
            thrust_list = self.z_control(-1 * diff * coeff, thrust_list)
        if control_msg.angular.x == 0.0:
            diff = self.pose.pose.orientation.x - self.prev_pose.pose.orientation.x
            thrust_list = self.roll_control(1 * diff * coeff, thrust_list)
        if control_msg.angular.y == 0.0:
            diff = self.pose.pose.orientation.y - self.prev_pose.pose.orientation.y
            thrust_list = self.pitch_control(-1 * diff * coeff, thrust_list)
        if control_msg.angular.z == 0.0:
            diff = self.pose.pose.orientation.z - self.prev_pose.pose.orientation.z
            thrust_list = self.yaw_control(-1 * diff * coeff, thrust_list)

        return thrust_list

    def publish_thrust(self, thrust_list: List[float]):
        for i in range(len(self.thrusters)):
            self.publishers_[i].publish(Float64(data=thrust_list[i]))


def main():
    rclpy.init()

    print("Thruster controller node started")

    node = ThrusterControllerNode()
    node.create_publishers(Float64)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
