import re
from threading import Thread

from rclpy.executors import SingleThreadedExecutor
from rclpy.node import Node
from PyQt5.QtCore import pyqtBoundSignal
import atexit


class GUIEventSubscriber(Node):
    """Multithreaded subscriber for receiving messages to the GUI."""

    def __init__(self, msg_type: type, topic: str, signal: pyqtBoundSignal):
        # Name this node with a sanitized version of the topic
        name: str = f'gui_event_subscriber_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}'
        super().__init__(name, namespace="surface/gui",
                         parameter_overrides=[])

        self.subscription = self.create_subscription(
            msg_type, topic, signal.emit, 10)

        custom_executor = SingleThreadedExecutor()
        custom_executor.add_node(self)
        Thread(target=custom_executor.spin, daemon=True,
               name=f'{name}_spin').start()
        atexit.register(custom_executor.shutdown)
