import re
from threading import Thread

from rclpy.node import Node
import rclpy
from rclpy.client import SrvType, SrvTypeRequest, SrvTypeResponse

from PyQt5.QtCore import pyqtBoundSignal

# Set to None for no timeout limits on service requests
# else set to float number of seconds to limit request spinning
TIMEOUT_SEC: float = 1.0


class GUIEventClient(Node):
    """Multithreaded client for sending service requests from the GUI."""

    def __init__(self, srv_type: SrvType, topic: str, signal: pyqtBoundSignal):
        # Name this node with a sanitized version of the topic
        self.name: str = f'gui_event_client_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}'
        super().__init__(self.name, namespace="surface/gui",
                         parameter_overrides=[])

        self.srv_type = srv_type
        self.topic: str = topic
        self.connected: bool = False
        self.signal: pyqtBoundSignal = signal

        self.cli = self.create_client(srv_type, topic)
        Thread(target=self.__connect_to_service, daemon=True,
               name=f'{self.name}_connect_to_service').start()

    def __connect_to_service(self):
        """Connect this client to a server in a separate thread; set self.connected when done."""
        while not self.cli.wait_for_service(timeout_sec=TIMEOUT_SEC):
            self.get_logger().info(
                'Service for GUI event client node on topic' +
                f' {self.topic} unavailable, waiting again...')
        self.connected = True
        self.req: SrvTypeRequest = self.srv_type.Request()

    def send_request_async(self, request: SrvTypeRequest):
        """Send request to server in separate thread."""
        Thread(target=self.send_request_with_signal,
               kwargs={'request': request},
               daemon=True, name=f'{self.name}_send_request').start()

    def send_request_with_signal(self, request: SrvTypeRequest):
        """Send synchronous request to server and emit signal."""
        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(
            self, future, timeout_sec=TIMEOUT_SEC)

        self.signal.emit(future.result())

    def send_request(self, request: SrvTypeRequest) -> SrvTypeResponse:
        """Send synchronous request to server and return result."""
        future = self.cli.call_async(request)
        rclpy.spin_until_future_complete(
            self, future, timeout_sec=TIMEOUT_SEC)

        return future.result()
