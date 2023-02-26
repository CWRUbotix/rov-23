import re
from threading import Thread
from event_nodes.event_node import GUIEventNode

from rclpy.executors import SingleThreadedExecutor
from rclpy.client import SrvType


class GUIEventServer(GUIEventNodeExecutor):
    """Multithreaded server for processing service requests to update GUI."""

    def __init__(self, srv_type: SrvType, topic: str, callback: callable):
        """
        Initialize this server with a CALLBACK for processing requests.

        Remember to use a signal to update the GUI!
        """
        # Name this node with a sanitized version of the topic
        super().__init__(f'gui_event_server_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.srv = self.create_service(srv_type, topic, callback)

        self.custom_executor = SingleThreadedExecutor()
        self.custom_executor.add_node(self)
        Thread(target=self.custom_executor.spin, daemon=True,
               name=f'{self.node_name}_spin').start()

    def kill_executor(self):
        self.custom_executor.shutdown()
