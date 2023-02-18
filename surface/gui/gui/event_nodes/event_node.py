from rclpy.node import Node


class GUIEventNode(Node):
    """
    Superclass for all event nodes.

    Requires all event nodes that create executors to implement an executor killer.
    """

    def __init__(self, node_name: str):
        super().__init__(node_name, namespace='/gui',
                         parameter_overrides=[])
        self.node_name = node_name

    def kill_executor(self):
        """Kill this node's executor."""
        raise NotImplementedError('You called kill_executor on an event node' +
                                  'that doesn\'t have executors to kill')
