import re
from threading import Thread
from event_nodes.event_node import GUIEventNode

import rclpy


class GUIEventServer(GUIEventNode):
    """Multithreaded server for processing service requests to update GUI."""

    def __init__(self, interface: type, topic: str, callback: callable):
        """
        Initialize this server with a CALLBACK for processing requests.

        Remember to use a signal to update the GUI!
        """
        # Name this node with a sanitized version of the topic
        super().__init__(f'gui_event_server_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.srv = self.create_service(interface, topic, callback)

    def spin_async(self):
        """Spin the server in a new thread."""
        # Create new executor to avoid spinning global executor multiple times
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self)
        Thread(target=self.executor.spin, daemon=True,
               name=f'{self.node_name}_spin').start()

        self.executor = executor

    def kill_executor(self):
        self.executor.shutdown()
