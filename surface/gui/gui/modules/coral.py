from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from gui.modules.video_widget import VideoWidget


class CoralWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.root_layout: QHBoxLayout = QHBoxLayout(self)

        self.depth_cam_stream = VideoWidget("/bottom_cam/image_raw", "Depth Cam")  # TODO update stream topic

        self.button_layout = QVBoxLayout()

        self.rtabmap_button = QPushButton("Start RTAB-Map")
        self.open3d_button = QPushButton("Start Meshing")
        self.viewer_button = QPushButton("Start Mesh Viewer")

        self.button_layout.addWidget(self.rtabmap_button, alignment=Qt.AlignCenter)
        self.button_layout.addWidget(self.open3d_button, alignment=Qt.AlignCenter)
        self.button_layout.addWidget(self.viewer_button, alignment=Qt.AlignCenter)
        self.button_layout.addStretch()

        self.root_layout.addWidget(self.depth_cam_stream, 3)
        self.root_layout.addLayout(self.button_layout, 1)
