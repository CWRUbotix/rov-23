
import rclpy
from rclpy.node import Node
import re


class GUIEventServer(Node):

    def __init__(self, interface: type, topic: str, callback: callable):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_server_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')
        self.srv = self.create_service(interface, topic, callback)
