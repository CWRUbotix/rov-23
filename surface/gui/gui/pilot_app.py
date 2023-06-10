from PyQt5.QtWidgets import QGridLayout
from gui.modules.video_widget import SwitchableVideoWidget
from gui.modules.arm import Arm
from gui.app import App


class PilotApp(App):
    def __init__(self):
        super().__init__('pilot_gui_node')

        self.setWindowTitle('Pilot GUI - CWRUbotix ROV 2023')

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = SwitchableVideoWidget(["/front_cam/image_raw",
                                                 "/bottom_cam/image_raw",
                                                 "/depth_cam/image_raw"],
                                                ["Front Camera",
                                                 "Bottom Camera",
                                                 "Depth Camera"],
                                                "camera_switch")
        layout.addWidget(self.video_area, 1, 1, 1, 2)

        self.arm: Arm = Arm()
        layout.addWidget(self.arm, 3, 3)


def run_gui_pilot():
    PilotApp().run_gui()
