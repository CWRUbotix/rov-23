import re
from threading import Thread
from gui.event_nodes.event_node import GUIEventNode

from rclpy.executors import SingleThreadedExecutor

from PyQt5.QtCore import pyqtBoundSignal

# import event_nodes.global_executor


class GUIEventSubscriber(GUIEventNode):
    """Multithreaded subscriber for receiving messages to the GUI."""

    def __init__(self, interface: type, topic: str, signal: pyqtBoundSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.subscription = self.create_subscription(
            interface, topic, signal.emit, 10)

        # Setter
        self.executor = SingleThreadedExecutor()
        self.thread_helper()

    def thread_helper(self):
        # Type Guarding
        if self.executor is not None:
            Thread(target=self.executor.spin(), daemon=True,
                   name=f'{self.node_name}_spin').start()
        else:
            self.get_logger().error("Error Thread Not Started")

    def kill_executor(self):
        if self.executor is not None:
            self.executor.shutdown()
