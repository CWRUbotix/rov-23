import re

from rclpy.node import Node
from rclpy.publisher import MsgType


class GUIEventPublisher(Node):
    """Publisher for sending messages from the GUI."""

    def __init__(self, msg_type: MsgType, topic: str):
        # Name this node with a sanitized version of the topic
        name: str = f'gui_event_publisher_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}'
        super().__init__(name, namespace="surface/gui",
                         parameter_overrides=[])

        self.publisher = self.create_publisher(msg_type, topic, 10)

    def publish(self, msg: MsgType):
        """Send a message with the provided parameters."""
        self.publisher.publish(msg)
