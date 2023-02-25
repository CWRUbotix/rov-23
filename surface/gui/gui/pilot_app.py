from PyQt5.QtWidgets import QGridLayout


from gui.modules.task_selector import TaskSelector
from gui.modules.video_area import VideoArea
from gui.app import App


class PilotApp(App):
    def __init__(self):
        super().__init__("pilot_gui_node")

        self.setWindowTitle('CWRUbotix ROV 2023 - Pilot')

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea()
        layout.addWidget(self.video_area, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)


