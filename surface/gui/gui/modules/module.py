
import rclpy
from PyQt5.QtWidgets import QWidget


class Module(QWidget):
    """
    Superclass for all modules.

    Requires that modules which create spinning nodes implement an executor killer.
    """

    def __init__(self):
        super().__init__()
        rclpy.init()  # We'll need to create ROS nodes

    def kill_all_executors(self):
        """Kill all executors create by this module."""
        return
