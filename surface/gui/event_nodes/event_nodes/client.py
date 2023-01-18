
from typing import Dict, Any

import rclpy
from rclpy.node import Node


# Set to None for no timeout limits on service requests
# else set to float number of seconds to limit request spinning
TIMEOUT_SEC: float = None


class GUIEventClient(Node):

    def __init__(self, interface: type, topic: str):
        super().__init__(f'gui_event_client_{topic}')
        self.cli = self.create_client(interface, topic)
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                f'Service for GUI event client node on topic {topic} unavailable, waiting again...')
        self.req = interface.Request()

    def send_request(self, params: Dict[str, Any]):
        for key, value in params.items():
            setattr(self.req, key, value)

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(
            self, self.future, timeout_sec=TIMEOUT_SEC)
        return self.future.result()
