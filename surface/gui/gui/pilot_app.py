from PyQt5.QtWidgets import QGridLayout
from gui.modules.video_area import VideoArea
from gui.modules.arm import Arm
from gui.app import App


class PilotApp(App):
    def __init__(self):
        super().__init__('pilot_gui_node')

        self.setWindowTitle('Pilot GUI - CWRUbotix ROV 2023')

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea()
        layout.addWidget(self.video_area, 0, 0, 1, 2)

        self.arm: Arm = Arm()
        layout.addWidget(self.arm, 1, 1)


def run_gui_pilot():
    PilotApp().run_gui()
