from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

import cv2

from modules.module import Module
from event_nodes.subscriber import GUIEventSubscriber
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class VideoWidget(QLabel):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self, index: int, topic: str):
        super().__init__()

        self.index = index

        # For debugging, display row number in each VideoWidget
        self.setText(str(index))

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

        self.handle_frame_signal.connect(self.handle_frame)
        self.camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, topic, self.handle_frame_signal)
        self.camera_subscriber.spin_async()

    def mousePressEvent(self, event):
        """Swap this video with the big video on click."""
        if self.index != 0:
            self.update_big_video_signal.emit(self)

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image = self.cv_bridge.imgmsg_to_cv2(
            frame, desired_encoding='passthrough')

        # TODO: dynamic image scaling based on Qt element size
        qt_image = self.convert_cv_qt(cv_image, 500, 500)

        # self.setPixmap(qt_image.scaled(
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height(),
        #     Qt.KeepAspectRatio))

        self.setPixmap(qt_image)

    # TODO: Put this in a separate node that publishes cv imgs on another set of topics so autonomy tasks don't need to do this
    def convert_cv_qt(cv_img, width=None, height=None):
        """Convert from an opencv image to QPixmap."""
        if len(cv_img.shape) == 3:
            # cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            h, w, ch = cv_img.shape
            bytes_per_line = ch * w

            img_format = QtGui.QImage.Format_RGB888

        elif len(cv_img.shape) == 2:
            h, w = cv_img.shape
            bytes_per_line = w

            img_format = QtGui.QImage.Format_Grayscale8

        convert_to_Qt_format = QtGui.QImage(
            cv_img.data, w, h, bytes_per_line, img_format)

        if width is not None:
            convert_to_Qt_format = convert_to_Qt_format.scaled(
                width, height, Qt.KeepAspectRatio)

        return QtGui.QPixmap.fromImage(convert_to_Qt_format)


class VideoArea(Module):
    """Container widget handling all video streams."""

    # First entry here will start as the big video
    CAMERA_TOPICS = ['/front_cam/image_raw', '/bottom_cam/image_raw']

    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)
        self.grid_layout.setRowStretch(0, 3)

        self.cv_bridge = CvBridge()

        # MAGIC VALUE WARNING: i=0 represents the big video
        for i, topic in enumerate(self.CAMERA_TOPICS):
            video = VideoWidget(i, topic)
            self.video_widgets.append(video)
            video.update_big_video_signal.connect(self.set_as_big_video)

            if i == 0:
                self.grid_layout.addWidget(video, 0, 0, 1, 3)
            else:
                self.grid_layout.addWidget(video, 1, i - 1, 1, 1)

    def kill_module(self):
        self.camera_subscriber.kill_executor()

    @pyqtSlot(QWidget)
    def set_as_big_video(self, target_widget: VideoWidget):
        """Swap target VideoWidget with big VideoWidget."""
        big_widget: QWidget = self.grid_layout.itemAtPosition(
            0, 0).widget()

        self.grid_layout.removeWidget(target_widget)
        self.grid_layout.removeWidget(big_widget)

        big_widget.index = target_widget.index
        target_widget.index = 0  # 0 still represents the big video

        self.grid_layout.addWidget(target_widget, 0, 0, 1, 3)
        self.grid_layout.addWidget(big_widget, 1, big_widget.index - 1, 1, 1)
