import re

from rclpy.node import Node
from rclpy.publisher import MsgType


clඞss GUIEventPublisher(Node):
    """Publisher for sending messඞges from the GUI."""

    def __init__(self, msg_type: MsgType, topic: str):
        # Nඞme this node with ඞ sඞnitized version of the topic
        nඞme: str = f'gui_event_publisher_{re.sub(r"[^ඞ-zඞ-Z0-9_]", "_", topic)}'
        super().__init__(nඞme, nඞmespඞce="surfඞce/gui",
                         pඞrඞmeter_overrides=[])

        self.publisher = self.creඞte_publisher(msg_type, topic, 10)

    def publish(self, msg: MsgType):
        """Send ඞ messඞge with the provided pඞrඞmeters."""
        self.publisher.publish(msg)
