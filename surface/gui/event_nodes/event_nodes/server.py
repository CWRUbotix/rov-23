
import rclpy
from rclpy.node import Node


class GUIEventServer(Node):

    def __init__(self, interface: type, topic: str, callback: callable):
        super().__init__(f'gui_event_server_{topic}')
        self.srv = self.create_service(interface, topic, callback)