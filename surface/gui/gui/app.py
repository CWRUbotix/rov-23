from rclpy.node import Node
import rclpy

from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
import sys

from gui.modules.task_selector import TaskSelector
from gui.modules.video_area import VideoArea
from gui.modules.logger import Logger


class App(Node, QWidget):
    """Main app window."""

    def __init__(self):
        super().__init__(node_name='app_node', parameter_overrides=[])
        super(QWidget, self).__init__()

        self.setWindowTitle('ROV 2023')
        self.resize(1850, 720)

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea()
        layout.addWidget(self.video_area, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 1, 0)

    def closeEvent(self, event):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        for module in [self.video_area, self.task_selector, self.logger]:
            module.kill_module()

        # Shutdown rclpy
        rclpy.shutdown()

        event.accept()


def run_app():
    rclpy.init()
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())
