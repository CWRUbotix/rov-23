from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage

from gui.event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

from typing import Optional


class VideoWidget(QWidget):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self, index: int, topic: str, widget_width: int = 640,
                 widget_height: int = 480, label_text: Optional[str] = None,
                 swap_rb_channels: bool = False):
        super().__init__()

        self.widget_width: int = widget_width
        self.widget_height: int = widget_height
        self.swap_rb_channels: bool = swap_rb_channels
        self.index: int = index

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        if label_text is not None:
            self.label = QLabel(label_text)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet('QLabel { font-size: 20px; }')
            self.layout.addWidget(self.label)

        self.video_frame_label = QLabel()
        self.video_frame_label.setText(str(index))
        self.layout.addWidget(self.video_frame_label)

        self.cv_bridge: CvBridge = CvBridge()

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

        self.handle_frame_signal.connect(self.handle_frame)
        self.camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, topic, self.handle_frame_signal)

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image: cv2.Mat = self.cv_bridge.imgmsg_to_cv2(
            frame, desired_encoding='passthrough')

        qt_image: QImage = self.convert_cv_qt(cv_image, self.widget_width, self.widget_height)

        self.video_frame_label.setPixmap(QPixmap.fromImage(qt_image))

    def convert_cv_qt(self, cv_img: cv2.Mat, width: int = 0, height: int = 0) -> QImage:
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


class PausableVideoWidget(VideoWidget):
    """A single video stream widget that can be paused and played."""

    def __init__(self, cam_topic: str):
        super().__init__(0, cam_topic)

        self.is_paused = False

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        if not self.is_paused:
            super().handle_frame(frame)

    def pause(self):
        self.is_paused = False

    def play(self):
        self.is_paused = True

    def toggle(self):
        """Toggle whether this widget is paused or playing."""
        self.is_paused = not self.is_paused
