import re
from typing import Dict, Any

from rclpy.node import Node


class GUIEventPublisher(Node):

    def __init__(self, interface: type, topic: str):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_publisher_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')
        self.publisher = self.create_publisher(interface, topic, 10)
        self.interface = interface

    def publish(self, params: Dict[str, Any]):
        msg: self.interface = self.interface()

        for key, value in params.items():
            setattr(msg, key, value)

        self.publisher.publish(msg)
