import rclpy
from rclpy.node import Node

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QCloseEvent


class App(Node, QWidget):
    """Main app window."""

    def __init__(self, node_name: str):
        super().__init__(node_name=node_name, parameter_overrides=[])
        super(QWidget, self).__init__()

        self.declare_parameter('theme', '')
        self.modules = []

        self.resize(1850, 720)

    # Variable name a0 because it's overloading parent closeEvent method
    def closeEvent(self, a0: QCloseEvent):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        for module in self.modules:
            module.kill_module()

        # Shutdown rclpy
        rclpy.shutdown()
        a0.accept()
