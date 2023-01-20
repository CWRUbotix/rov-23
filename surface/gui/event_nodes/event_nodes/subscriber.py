import re
from threading import Thread

import rclpy
from rclpy.node import Node

from PyQt5.QtCore import pyqtSignal


class GUIEventSubscriber(Node):

    def __init__(self, interface: type, topic: str, signal: pyqtSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')
        self.subscription = self.create_subscription(
            interface, topic, lambda msg: signal.emit(msg), 10)
        self.subscription  # prevent unused variable warning

    def spin_async(self):
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self)
        Thread(target=executor.spin, daemon=True).start()
