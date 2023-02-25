from rclpy.node import Node
import rclpy


class AppNode(Node):

    def __init__(self):
        super().__init__(node_name='app_node', parameter_overrides=[])

        self.declare_parameter('gui_type', '')
        self.declare_parameter('theme', '')

