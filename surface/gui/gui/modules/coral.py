from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
import subprocess

from gui.modules.video_widget import VideoWidget


class CoralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.root_layout: QHBoxLayout = QHBoxLayout(self)

        self.depth_cam_stream = VideoWidget("/bottom_cam/image_raw", "Depth Cam")  # TODO update stream topic

        self.button_layout = QVBoxLayout()

        self.rtabmap_button = ProcessLaunchButton("RTAB-Map")
        self.open3d_button = ProcessLaunchButton("Point Mesher")
        self.viewer_button = ProcessLaunchButton("Mesh Viewer")

        self.button_layout.addWidget(self.rtabmap_button, alignment=Qt.AlignRight)
        self.button_layout.addWidget(self.open3d_button, alignment=Qt.AlignRight)
        self.button_layout.addWidget(self.viewer_button, alignment=Qt.AlignRight)

        self.button_layout.addStretch()
        self.button_layout.setSpacing(20)

        self.root_layout.addWidget(self.depth_cam_stream, 3)
        self.root_layout.addLayout(self.button_layout, 1)


class ProcessLaunchButton(QPushButton):
    BUTTON_HEIGHT = 50
    BUTTON_WIDTH = 250
    BUTTON_STYLESHEET = 'QPushButton { font-size: 20px; }'

    def __init__(self, process_label: str, process_args: list):
        super().__init__(f"Start {process_label}")

        self.process_label = process_label
        self.process_args = process_args

        self.setMinimumHeight(self.BUTTON_HEIGHT)
        self.setMinimumWidth(self.BUTTON_WIDTH)
        self.setStyleSheet(self.BUTTON_STYLESHEET)

        self.setCheckable(True)
        self.toggled.connect(self.toggle_process)

        self.process = None

    def toggle_process(self, run_process: bool):
        if run_process:
            self.process = subprocess.Popen(self.process_args, text=True)
            self.setText(f"Stop {self.process_label}")
        else:
            if self.process is not None:
                self.process.kill()
                self.setText(f"Start {self.process_label}")
