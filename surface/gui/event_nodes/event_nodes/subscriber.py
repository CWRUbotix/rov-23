import re
from threading import Thread

import rclpy
from rclpy.node import Node


class GUIEventSubscriber(Node):

    def __init__(self, interface: type, topic: str, callback: callable):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')
        self.subscription = self.create_subscription(
            interface, topic, callback, 10)
        self.subscription  # prevent unused variable warning

    def spin_async(self):
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self)
        subscriber_thread: Thread = Thread(
            target=executor.spin, daemon=True)
        subscriber_thread.start()
