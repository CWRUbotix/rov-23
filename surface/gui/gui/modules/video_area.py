from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage

from gui.event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv2 import Mat
import cv2

from dataclasses import dataclass


class VideoWidget(QLabel):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self, index: int, topic: str, widget_width: int = 640,
                 widget_height: int = 480, swap_rb_channels: bool = False):
        super().__init__()

        self.widget_width: int = widget_width
        self.widget_height: int = widget_height
        self.swap_rb_channels: bool = swap_rb_channels

        self.index: int = index

        # For debugging, display row number in each VideoWidget
        self.setText(str(index))

        self.cv_bridge: CvBridge = CvBridge()

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

        self.handle_frame_signal.connect(self.handle_frame)
        self.camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, topic, self.handle_frame_signal)

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image: Mat = self.cv_bridge.imgmsg_to_cv2(
            frame, desired_encoding='passthrough')

        qt_image: QImage = self.convert_cv_qt(cv_image, self.widget_width, self.widget_height)

        self.setPixmap(QPixmap.fromImage(qt_image))

    def convert_cv_qt(self, cv_img: Mat, width: int = 0, height: int = 0) -> QImage:
        """Convert from an opencv image to QPixmap."""
        # Color image
        if len(cv_img.shape) == 3:
            # Swap red & blue channels if necessary
            if self.swap_rb_channels:
                cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)

            h, w, ch = cv_img.shape
            bytes_per_line: int = ch * w

            img_format = QImage.Format_RGB888

        # Grayscale image
        elif len(cv_img.shape) == 2:
            h, w = cv_img.shape
            bytes_per_line: int = w

            img_format = QImage.Format_Grayscale8

        else:
            raise Exception("Somehow not color or grayscale image.")

        qt_image = QImage(cv_img.data, w, h, bytes_per_line, img_format)
        qt_image: QImage = qt_image.scaled(width, height, Qt.KeepAspectRatio)

        return qt_image


@dataclass
class LabeledVideo:
    label: str
    topic: str
    coords: 'list[int]'
    debug_index: int


class VideoArea(QWidget):
    """Container widget handling all video streams."""

    VIDEOS: 'list[LabeledVideo]' = [
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
            labeled_video = QWidget()
            labeled_video_layout = QVBoxLayout()
            labeled_video.setLayout(labeled_video_layout)

            label = QLabel(video.label)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet('QLabel { font-size: 20px; }')
            labeled_video_layout.addWidget(label)
            labeled_video_layout.addWidget(
                VideoWidget(video.debug_index, video.topic, self.VIDEO_WIDTH, self.VIDEO_HEIGHT))

            self.grid_layout.addWidget(labeled_video, video.coords[0], video.coords[1])
