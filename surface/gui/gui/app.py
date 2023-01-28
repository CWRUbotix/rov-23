import rclpy

from PyQt5.QtWidgets import QWidget, QGridLayout

from modules.task_selector import TaskSelector
from modules.video_area import VideoArea
from modules.logger import Logger


class App(QWidget):
    """Main app window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle('ROV 2023')
        self.resize(1850, 720)

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea(4)
        layout.addWidget(self.video_area, 0, 0)

        # self.task_selector: TaskSelector = TaskSelector()
        # layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 1, 0)

    def closeEvent(self, event):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        # self.task_selector.kill_all_executors()
        self.logger.kill_all_executors()

        # Shutdown rclpy
        rclpy.shutdown()

        event.accept()
