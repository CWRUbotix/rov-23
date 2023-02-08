import re
from threading import Thread
from event_nodes.event_node import GUIEventNode

from rclpy.executors import SingleThreadedExecutor


class GUIEventServer(GUIEventNode):
    """Multithreaded server for processing service requests to update GUI."""

    def __init__(self, interface: type, topic: str,  callback: callable):
        """
        Initialize this server with a CALLBACK for processing requests.

        Remember to use a signal to update the GUI!
        """
        # Name this node with a sanitized version of the topic
        super().__init__(f'gui_event_server_{re.sub(r"[^a-zA-Z0-9_]", "_", topic)}')

        self.srv = self.create_service(interface, topic, callback)

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
