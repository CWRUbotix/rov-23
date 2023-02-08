import re
from threading import Thread
from gui.event_nodes.event_node import GUIEventNode

from rclpy.executors import SingleThreadedExecutor

from PyQt5.QtCore import pyqtSignal


class GUIEventSubscriber(GUIEventNode):
    """Multithreaded subscriber for receiving messages to the GUI."""

    def __init__(self, interface: type, topic: str, signal: pyqtSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.subscription = self.create_subscription(
            interface, topic, signal.emit, 10)

        # TODO would be nice to use self.executor setter
        executor = SingleThreadedExecutor()
        executor.add_node(self)
        Thread(target=executor.spin, daemon=True,
               name=f'{self.node_name}_spin').start()

    def kill_executor(self):
        if self.executor is not None:
            self.executor.shutdown()
