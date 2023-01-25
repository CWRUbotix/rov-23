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

        video_area = VideoArea(4)
        layout.addWidget(video_area, 0, 0)

        task_selector: TaskSelector = TaskSelector()
        layout.addWidget(task_selector, 0, 1)

        logger: Logger = Logger()
        layout.addWidget(logger, 1, 0)

    def closeEvent(self, event):
        """Piggyback the PyQt window close to kill rclpy."""
        # This shutdown should kill all nodes the GUI makes
        # rclpy.init() still needs to be called in each file that constructs a node
        rclpy.shutdown()

        event.accept()
