from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication


from gui.modules.task_selector import TaskSelector
from gui.modules.video_area import VideoArea
from gui.modules.logger import Logger
from app import App


class PilotApp(App):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CWRUbotix ROV 2023 - Pilot')

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea(4)
        layout.addWidget(self.video_area, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 1, 0)

    def kill_all_executors(self):
        self.task_selector.kill_all_executors()
        self.logger.kill_all_executors()
