import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist


class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node")
        self.thrusters = [
            {"location": "top_front_left"},
            {"location": "top_front_right"},
            {"location": "top_back_left"},
            {"location": "top_back_right"},
            {"location": "bottom_front_left"},
            {"location": "bottom_front_right"},
            {"location": "bottom_back_left"},
            {"location": "bottom_back_right"},
        ]
        self.multiplier = 3

        self.publishers_ = []
        self.subscriber_ = self.create_subscription(
            Twist, "/cmd_vel", self.control, qos_profile=10
        )

    def create_publishers(self, msg_type, qos_profile=10):
        for thruster in self.thrusters:
            topic = (
                "model/rov/joint/thruster_"
                + thruster["location"]
                + "_body_blade_joint/cmd_thrust"
            )
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def control(self, msg):
        thrust_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        thrust_list = self.x_control(msg.linear.x, thrust_list)
        thrust_list = self.y_control(msg.linear.y, thrust_list)
        thrust_list = self.z_control(msg.linear.z, thrust_list)
        thrust_list = self.roll_control(msg.angular.x, thrust_list)
        thrust_list = self.pitch_control(msg.angular.y, thrust_list)
        thrust_list = self.yaw_control(msg.angular.z, thrust_list)
        self.publish_thrust(thrust_list)

    def x_control(self, speed, thrust_list):
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

    def y_control(self, speed, thrust_list):
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

    def z_control(self, speed, thrust_list):
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

    def roll_control(self, speed, thrust_list):
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

    def pitch_control(self, speed, thrust_list):
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

    def yaw_control(self, speed, thrust_list):
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

    def publish_thrust(self, thrust_list):
        for i in range(len(self.thrusters)):
            self.publishers_[i].publish(Float64(data=thrust_list[i]))

    def spin(self):
        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)

    print("Keyboard controller node started")

    node = ThrusterControllerNode()
    node.create_publishers(Float64)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
