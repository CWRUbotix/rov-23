import re
from threading import Thread
from gui.event_nodes.event_node import GUIEventNode

import rclpy

from PyQt5.QtCore import pyqtSignal

# import event_nodes.global_executor


class GUIEventSubscriber(GUIEventNode):
    """Multithreaded subscriber for receiving messages to the GUI."""

    def __init__(self, interface: type, topic: str, signal: pyqtSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.subscription = self.create_subscription(
            interface, topic, signal.emit, 10)
        self.subscription  # prevent unused variable warning

    def spin_async(self):
        """Wait for message in a different thread, emit signal with message when received."""
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self)
        Thread(target=executor.spin, daemon=True,
               name=f'{self.node_name}_spin').start()

        self.executor = executor

    def kill_executor(self):
        self.executor.shutdown()
