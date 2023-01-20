
from typing import Dict, Any

import rclpy
from rclpy.node import Node
import re
from threading import Thread


# Set to None for no timeout limits on service requests
# else set to float number of seconds to limit request spinning
TIMEOUT_SEC: float = 1.0


class GUIEventClient(Node):

    def __init__(self, interface: type, topic: str):
        # Name this node with a sanitized version of the topic
        super().__init__(
            f'gui_event_client_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.interface: type = interface
        self.topic: str = topic
        self.connected = False

        self.cli = self.create_client(interface, topic)
        connection_thread: Thread = Thread(
            target=self.__connect_to_service, daemon=True)
        connection_thread.start()

    def __connect_to_service(self):
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                f'Service for GUI event client node on topic {self.topic} unavailable, waiting again...')
        self.connected = True
        self.req = self.interface.Request()

    def send_request_async(self, params: Dict[str, Any], callback: callable):
        send_thread: Thread = Thread(target=self.send_request_callback, kwargs={
                                     'params': params, 'callback': callback}, daemon=True)
        send_thread.start()

    def send_request_callback(self, params: Dict[str, Any], callback: callable):
        for key, value in params.items():
            setattr(self.req, key, value)

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(
            self, self.future, timeout_sec=TIMEOUT_SEC)
        callback(self.future.result())
