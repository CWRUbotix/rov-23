from typing import Union
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
import atexit


class GUIEventNode(Node):
    """Superclass for all event nodes."""

    def __init__(self, node_name: str):
        super().__init__(node_name, namespace='surface/gui',
                         parameter_overrides=[])
        self.node_name = node_name
        self.custom_executor: Union[SingleThreadedExecutor, None] = None

        def kill_executor():
            """Kill this node's executor."""
            if self.custom_executor is not None:
                self.custom_executor.shutdown()

        atexit.register(kill_executor)
