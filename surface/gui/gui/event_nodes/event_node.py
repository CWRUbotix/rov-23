from rclpy.node import Node


class GUIEventNode(Node):
    """
    Superclass for all event nodes.
    Requires all event nodes that create executors to implement an executor killer.
    """

    def __init__(self, node_name: str):
        super().__init__(node_name)
        self.node_name = node_name

    def kill_executor(self):
        """Kill this node's executor."""
        return
