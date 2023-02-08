import re
from threading import Thread
from gui.event_nodes.event_node import GUIEventNode

from rclpy.executors import SingleThreadedExecutor, Executor

from PyQt5.QtCore import pyqtBoundSignal


class GUIEventSubscriber(GUIEventNode):
    """Multithreaded subscriber for receiving messages to the GUI."""

    def __init__(self, interface: type, topic: str, signal: pyqtBoundSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.subscription = self.create_subscription(
            interface, topic, signal.emit, 10)

        self.custom_executor = SingleThreadedExecutor()
        self.custom_executor.add_node(self)
        Thread(target=self.custom_executor.spin, daemon=True,
               name=f'{self.node_name}_spin').start()

    def kill_executor(self):
        self.custom_executor.shutdown()
