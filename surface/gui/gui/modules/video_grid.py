from PyQt5.QtWidgets import QGridLayout, QWidget

from typing import List, Tuple

from dataclasses import dataclass

from gui.modules.video_widget import VideoWidget


@dataclass
class LabeledVideo:
    label: str
    topic: str
    coords: Tuple[int, int]
    debug_index: int


class VideoGrid(QWidget):
    """Container widget handling all video streams."""

    VIDEOS: List[LabeledVideo] = [
        LabeledVideo('Front Cam', '/front_cam/image_raw', (0, 0), 0),
        LabeledVideo('Bottom Cam', '/bottom_cam/image_raw', (0, 1), 1)
    ]

    VIDEO_WIDTH:  int = 900
    VIDEO_HEIGHT: int = 675

    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)
        self.grid_layout.setRowStretch(0, 4)
        self.grid_layout.setRowStretch(1, 4)
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 1)

        for video in self.VIDEOS:
            video_widget = VideoWidget(video.debug_index, video.topic,
                                       self.VIDEO_WIDTH, self.VIDEO_HEIGHT, video.label)

            self.grid_layout.addWidget(video_widget, video.coords[0], video.coords[1])
