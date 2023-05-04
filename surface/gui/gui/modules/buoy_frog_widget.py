from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QSizePolicy,
)
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage

from gui.event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv2 import Mat
import cv2
import os


class VideoWidget(QLabel):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self, index: int, topic: str):
        super().__init__()

        self.index: int = index
        self.cur_image: Mat = None

        # For debugging, display row number in each VideoWidget
        self.setText(str(index))

        self.cv_bridge: CvBridge = CvBridge()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.handle_frame_signal.connect(self.handle_frame)
        self.camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, topic, self.handle_frame_signal
        )

    # def mousePressEvent(self, ev: QMouseEvent):
    #     """Swap this video with the big video on click."""
    #     if self.index != 0:
    #         self.update_big_video_signal.emit(self)

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image: Mat = self.cv_bridge.imgmsg_to_cv2(
            frame, desired_encoding="passthrough"
        )
        self.cur_image = cv_image

        # TODO: dynamic image scaling based on Qt element size
        # qt_image: QImage = self.convert_cv_qt(
        #     cv_image,
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height()
        # )

        qt_image: QImage = self.convert_cv_qt(cv_image, 480, 480)

        # self.setPixmap(qt_image.scaled(
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height(),
        #     Qt.KeepAspectRatio))

        self.setPixmap(QPixmap.fromImage(qt_image))

    def convert_cv_qt(self, cv_img: Mat, width: int = 0, height: int = 0) -> QImage:
        """Convert from an opencv image to QPixmap."""
        # Color image
        if len(cv_img.shape) == 3:
            # Rectify weird colors
            # cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2RGBA)
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

        if width == 0:
            qt_image: QImage = qt_image.scaled(width, height, Qt.KeepAspectRatio)
        return qt_image


class BuoyFrogWidget(QWidget):
    CAMERA_TOPICS = ["/front_cam/image_raw", "/bottom_cam/image_raw"]

    def __init__(self):
        super().__init__()
        self.mode = "buoy"
        self.is_recording = False

        layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(layout)

        self.video1: VideoWidget = VideoWidget(0, self.CAMERA_TOPICS[0])
        self.video2: VideoWidget = VideoWidget(1, self.CAMERA_TOPICS[1])

        self.videos = QHBoxLayout()
        self.videos.addWidget(self.video1)
        self.videos.addWidget(self.video2)

        self.mode_button = QPushButton()
        self.mode_button.setText("Toggle Mode\nCurrent: Buoy")
        self.mode_button.clicked.connect(self.toggle_mode)
        self.mode_button.setFixedSize(200, 100)

        self.record_button = QPushButton()
        self.record_button.setText("Record")
        self.record_button.clicked.connect(self.record)
        self.record_button.setFixedSize(200, 100)

        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.mode_button)
        self.buttons.addWidget(self.record_button)

        layout.addLayout(self.videos)
        layout.addLayout(self.buttons)

    def toggle_mode(self):
        # toggle video widget between video1 and video2 at first item of the layout
        if self.mode == "buoy":
            self.mode = "frog"
            self.mode_button.setText("Toggle Mode\nCurrent: Frog")
        else:
            self.mode = "buoy"
            self.mode_button.setText("Toggle Mode\nCurrent: Buoy")

    def record(self):
        self.record_button.setText("Press ESC at a new window\nto stop recording.")
        self.record_button.setDisabled(True)
        self.is_recording = True

        # make 'ros_23_ws/videos' folder if it doesn't exist
        if not os.path.exists("videos"):
            os.makedirs("videos")

        writer = cv2.VideoWriter(
            f"videos/{self.mode}.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 15, (640, 480)
        )

        while True:
            cv_image: Mat = (
                self.video1.cur_image if self.mode == "buoy" else self.video2.cur_image
            )
            writer.write(cv_image)

            cv2.imshow(f"Recording at {self.mode} mode", cv_image)

            if cv2.waitKey(1) & 0xFF == 27:
                self.record_button.setText("Record")
                self.record_button.setDisabled(False)
                self.is_recording = False
                writer.release()
                cv2.destroyAllWindows()
                break
