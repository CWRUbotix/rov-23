from typing import List

import rclpy
from geometry_msgs.msg import Twist, Vector3
from rclpy.node import Node, Publisher
from std_msgs.msg import Float64

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
            ROVControl, "manual_control", self.control_callback, qos_profile=10
        )
        self.arm_sub = self.create_subscription(
            Armed,'armed', self.arm_callback, 10
        )
        self.is_armed = False

    def arm_callback(self, msg: Armed):
        self.is_armed = msg.armed

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
        self.control(twist)

    def create_publishers(self, msg_type: type, qos_profile: int = 10):
        ns: str = self.get_namespace()
        for thruster in self.thrusters:
            topic = (
                f"{ns}/model/rov/joint/thruster_{thruster}_body_blade_joint/cmd_thrust"
            )
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def control(self, msg: Twist):
        thrust_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        thrust_list = self.x_control(msg.linear.x, thrust_list)
        thrust_list = self.y_control(msg.linear.y, thrust_list)
        thrust_list = self.z_control(msg.linear.z, thrust_list)
        thrust_list = self.roll_control(msg.angular.x, thrust_list)
        thrust_list = self.pitch_control(msg.angular.y, thrust_list)
        thrust_list = self.yaw_control(msg.angular.z, thrust_list)
        self.publish_thrust(thrust_list)

    def x_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # first: add thrust
        thrust_list[0] += thrust
        # second: subtract thrust
        thrust_list[1] -= thrust
        # third: subtract thrust
        thrust_list[2] -= thrust
        # fourth: add thrust
        thrust_list[3] += thrust
        return thrust_list

    def y_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # first: subtract thrust
        thrust_list[0] -= thrust
        # second: subtract thrust
        thrust_list[1] -= thrust
        # third: subtract thrust
        thrust_list[2] -= thrust
        # fourth: subtract thrust
        thrust_list[3] -= thrust
        return thrust_list

    def z_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # 5th: add thrust
        thrust_list[4] += thrust
        # 6th: add thrust
        thrust_list[5] += thrust
        # 7th: add thrust
        thrust_list[6] += thrust
        # 8th: add thrust
        thrust_list[7] += thrust
        return thrust_list

    def roll_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # 5th: add thrust
        thrust_list[4] += thrust
        # 6th: subtract thrust
        thrust_list[5] -= thrust
        # 7th: add thrust
        thrust_list[6] += thrust
        # 8th: subtract thrust
        thrust_list[7] -= thrust
        return thrust_list

    def pitch_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # 5th: subtract thrust
        thrust_list[4] -= thrust
        # 6th: subtract thrust
        thrust_list[5] -= thrust
        # 7th: add thrust
        thrust_list[6] += thrust
        # 8th: add thrust
        thrust_list[7] += thrust
        return thrust_list

    def yaw_control(self, speed: float, thrust_list: List[float]):
        thrust = speed * self.multiplier
        # first: subtract thrust
        thrust_list[0] -= thrust
        # second: subtract thrust
        thrust_list[1] -= thrust
        # third: add thrust
        thrust_list[2] += thrust
        # fourth: add thrust
        thrust_list[3] += thrust
        return thrust_list

    def publish_thrust(self, thrust_list: List[float]):
        for i in range(len(self.thrusters)):
            self.publishers_[i].publish(Float64(data=thrust_list[i]))

    def spin(self):
        rclpy.spin(self)


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
