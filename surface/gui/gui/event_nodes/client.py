from typing import Dict, Any
import re
from threading import Thread
from event_nodes.event_node import GUIEventNode

import rclpy

from PyQt5.QtCore import pyqtSignal

# Set to None for no timeout limits on service requests
# else set to float number of seconds to limit request spinning
TIMEOUT_SEC: float = 1.0


class GUIEventClient(GUIEventNode):
    """Multithreaded client for sending service requests from the GUI."""

    def __init__(self, interface: type, topic: str, signal: pyqtSignal):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_client_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.interface: type = interface
        self.topic: str = topic
        self.connected: bool = False
        self.signal: pyqtSignal = signal

        self.cli = self.create_client(interface, topic)
        Thread(target=self.__connect_to_service, daemon=True,
               name=f'{self.node_name}_connect_to_service').start()

    def __connect_to_service(self):
        """Connect this client to a server in a seperate thread; set self.connected when done."""
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Service for GUI event client node on topic' +
                f' {self.topic} unavailable, waiting again...')
        self.connected = True
        self.req = self.interface.Request()

    def send_request_async(self, params: Dict[str, Any]):
        """Send request to server in seperate thread."""
        Thread(target=self.send_request_with_signal, kwargs={'params': params},
               daemon=True, name=f'{self.node_name}_send_request').start()

    def send_request_with_signal(self, params: Dict[str, Any]):
        """Send synchronous request to server and emit signal."""
        for key, value in params.items():
            setattr(self.req, key, value)

        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(
            self, future, timeout_sec=TIMEOUT_SEC)

        self.signal.emit(future.result())

    def send_request(self, params: Dict[str, Any]):
        """Send synchronous request to server and return result."""
        for key, value in params.items():
            setattr(self.req, key, value)

        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(
            self, future, timeout_sec=TIMEOUT_SEC)

        return future.result()
