from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage

from gui.event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Image
from interfaces.msg import CameraControllerSwitch
from cv_bridge import CvBridge
import cv2

from typing import Optional, List


class VideoWidget(QWidget):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self, topic: str, label_text: Optional[str] = None,
                 widget_width: int = 640, widget_height: int = 480,
                 swap_rb_channels: bool = False):
        super().__init__()

        self.widget_width: int = widget_width
        self.widget_height: int = widget_height
        self.swap_rb_channels: bool = swap_rb_channels

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        if label_text is not None:
            self.label = QLabel(label_text)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet('QLabel { font-size: 20px; }')
            self.layout.addWidget(self.label)

        self.video_frame_label = QLabel()
        self.video_frame_label.setText(f'This topic had no frame: {topic}')
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


class SwitchableVideoWidget(VideoWidget):
    """A single video stream widget that can be paused and played."""

    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 100

    controller_signal = pyqtSignal(CameraControllerSwitch)

    def __init__(self, cam_topics: List[str], button_names: List[str],
                 controller_button_topic: Optional[str] = None,
                 default_cam_num: int = 0,
                 label_text: Optional[str] = None,
                 widget_width: int = 640, widget_height: int = 480,
                 swap_rb_channels: bool = False):

        self.active_cam = default_cam_num
        self.cam_topics = cam_topics
        self.button_names = button_names

        super().__init__(cam_topics[self.active_cam], label_text, widget_width,
                         widget_height, swap_rb_channels)

        self.num_of_cams = len(cam_topics)

        if self.num_of_cams != len(button_names):
            self.camera_subscriber.get_logger().error("Number of cam topics != num of cam names")
            raise ValueError("Number of cam topics != num of cam names")

        self.button: QPushButton = QPushButton(button_names[self.active_cam])
        self.button.setMaximumWidth(self.BUTTON_WIDTH)
        self.button.setMaximumHeight(self.BUTTON_HEIGHT)
        self.button.clicked.connect(lambda: self.camera_switch(True))
        self.layout.addWidget(self.button, Qt.AlignCenter)

        if controller_button_topic is not None:
            self.controller_signal.connect(self.controller_camera_switch)
            self.controller_subscriber = GUIEventSubscriber(CameraControllerSwitch,
                                                            controller_button_topic,
                                                            self.controller_signal)

    @pyqtSlot(CameraControllerSwitch)
    def controller_camera_switch(self, switch: CameraControllerSwitch):
        if switch.toggle_left:
            self.camera_switch(False)
        elif switch.toggle_right:
            self.camera_switch(True)
        else:
            self.controller_subscriber.get_logger().warn("CameraControllerSwitch msg sent Empty")

    def camera_switch(self, toggle_right: bool):
        if toggle_right:
            self.active_cam = (self.active_cam + 1) % self.num_of_cams
        else:
            self.active_cam = (self.active_cam - 1) % self.num_of_cams

        self.camera_subscriber.destroy_node()
        self.camera_subscriber = GUIEventSubscriber(
            Image, self.cam_topics[self.active_cam], self.handle_frame_signal)
        self.button.setText(self.button_names[self.active_cam])


class PausableVideoWidget(VideoWidget):
    """A single video stream widget that can be paused and played."""

    BUTTON_WIDTH = 120
    PAUSED_TEXT = 'Play'
    PLAYING_TEXT = 'Pause'

    def __init__(self, cam_topic: str, label_text: Optional[str] = None,
                 widget_width: int = 640, widget_height: int = 480,
                 swap_rb_channels: bool = False):
        super().__init__(cam_topic, label_text, widget_width,
                         widget_height, swap_rb_channels)

        self.button: QPushButton = QPushButton(self.PLAYING_TEXT)
        self.button.setMaximumWidth(self.BUTTON_WIDTH)
        self.button.clicked.connect(self.toggle)
        self.layout.addWidget(self.button, alignment=Qt.AlignHCenter)

        self.is_paused = False

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        if not self.is_paused:
            super().handle_frame(frame)

    def toggle(self):
        """Toggle whether this widget is paused or playing."""
        self.is_paused = not self.is_paused

        self.button.setText(self.PAUSED_TEXT if self.is_paused else self.PLAYING_TEXT)
