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

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea()
        layout.addWidget(self.video_area, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 1, 0)

    # Variable name a0 because it's overloading parent closeEvent method
    def closeEvent(self, a0: QCloseEvent):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        for module in [self.video_area, self.task_selector, self.logger]:
            module.kill_module()

        # Shutdown rclpy
        rclpy.shutdown()
        a0.accept()

    def kill_all_executors(self):
        """Called on shutdown, should be """
        pass
