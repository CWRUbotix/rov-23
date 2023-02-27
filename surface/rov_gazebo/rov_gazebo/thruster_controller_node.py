import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

thrusters = [
    {"location": "top_front_left", "reflect_blade": -1},
    {"location": "top_front_right", "reflect_blade": -1},
    {"location": "top_back_left", "reflect_blade": 1},
    {"location": "top_back_right", "reflect_blade": 1},
    {"location": "bottom_front_left", "reflect_blade": 1},
    {"location": "bottom_front_right", "reflect_blade": -1},
    {"location": "bottom_back_left", "reflect_blade": -1},
    {"location": "bottom_back_right", "reflect_blade": 1},
]


class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node")
        self.publishers_ = []
        self.subscriber_ = self.create_subscription(
            Twist, "/cmd_vel", self.callback, qos_profile=10
        )

    def callback(self, msg):
        if msg.linear.z > 0:
            self.z_control(msg.linear.z)
        elif msg.linear.z < 0:
            self.z_control(msg.linear.z)
        else:
            self.z_control(0.0, 0.0)

    def create_publishers(self, msg_type, qos_profile=10):
        for thruster in thrusters:
            topic = (
                "model/rov/joint/thruster_"
                + thruster["location"]
                + "_body_blade_joint/cmd_force"
            )
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def z_control(self, speed):
        multiplier = 30
        for i in range(4, 8):
            thruster_input = speed * multiplier * thrusters[i]["reflect_blade"]
            self.publishers_[i].publish(Float64(data=thruster_input))

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
