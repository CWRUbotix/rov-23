from rclpy.node import Node
import rclpy

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QCloseEvent


class App(Node, QWidget):
    """Main app window."""

    def __init__(self):
        super().__init__(node_name='app_node', parameter_overrides=[])
        super(QWidget, self).__init__()

        self.declare_parameter('theme', '')

        self.resize(1850, 720)

    # Variable name a0 because it's overloading parent closeEvent method
    def closeEvent(self, a0: QCloseEvent):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        self.kill_all_executors()

        # Shutdown rclpy
        rclpy.shutdown()
        a0.accept()

    def kill_all_executors(self):
        """Called on shutdown, should be """
        pass
