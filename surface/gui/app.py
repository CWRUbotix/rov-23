from PyQt5.QtWidgets import QWidget, QGridLayout

import rclpy

from modules.task_selector import TaskSelector
from modules.video import VideoArea


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ROV 2023')
        self.resize(1850, 720)

        layout: QGridLayout = QGridLayout()

        taskSelector: TaskSelector = TaskSelector()

        layout.addWidget(taskSelector)

        video_area = VideoArea(4)

        layout.addWidget(video_area)

        self.setLayout(layout)

    def closeEvent(self, event):
        # This shutdown should kill all nodes the GUI makes
        # rclpy.init() still needs to be called in each file that constructs a node
        rclpy.shutdown()

        event.accept()
