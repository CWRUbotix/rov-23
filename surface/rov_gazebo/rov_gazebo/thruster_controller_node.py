import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

from std_msgs.msg import String

topic_names = [
    "model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_top_front_right_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_top_back_left_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_top_back_right_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_bottom_front_left_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_bottom_front_right_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_bottom_back_left_body_blade_joint/cmd_force",
    "model/rov/joint/thruster_bottom_back_right_body_blade_joint/cmd_force",
]


class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node")
        self.publishers_ = []
        self.subscriber_ = self.create_subscription(
            Twist, "/cmd_vel", self.callback, qos_profile=10
        )
        self.dummy = self.create_publisher(String, "dummy", qos_profile=10)

    def callback(self, msg):
        self.dummy.publish(String(data="got message"))
        self.get_logger().info("got message")
        if msg.linear.z > 0:
            self.publish_all(1, msg.linear.z)
        elif msg.linear.z < 0:
            self.publish_all(-1, msg.linear.z)
        else:
            self.publish_all(0.0, 0.0)

    def create_publishers(self, msg_type, qos_profile=10):
        for topic in topic_names:
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def publish_all(self, direction, speed):
        for publisher in self.publishers_:
            publisher.publish(Float64(data=direction * speed * 50))

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
