from typing import Union
from rclpy.node import Node


class GUIEventNodeExecutor(Node):
    """
    Superclass for all event nodes.

    Requires all Subscriber and Server event nodes to implement an executor killer.
    """

    def __init__(self, node_name: str):
        super().__init__(node_name, namespace='surface/gui',
                         parameter_overrides=[])
        self.node_name = node_name

    def kill_executor(self) -> None:
        """Kill this node's executor."""
        raise NotImplementedError('You called kill_executor on an event node' +
                                  'that doesn\'t have executors to kill')


class GUIEventNodeNonExecutor(Node):
    """
    Superclass for all non-executor event nodes.

    This is for Publishers and Clients.
    """

    def __init__(self, node_name: str):
        super().__init__(node_name, namespace='surface/gui',
                         parameter_overrides=[])
        self.node_name = node_name

    # TODO? remove nothing calls this
    def kill_executor(self) -> None:
        """No executors does nothing."""
        pass


# TODO no one uses this remove?
GUIEventNode = Union[GUIEventNodeExecutor, GUIEventNodeNonExecutor]
"""Superclass for all event nodes."""
