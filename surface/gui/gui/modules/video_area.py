from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import rclpy

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import cv2

from event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from modules.module import Module


class VideoWidget(QLabel):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)

    def __init__(self, row: int):
        super().__init__()

        self.row = row

        # For debugging, display row number in each VideoWidget
        self.setText(str(row))

        # TODO: For actual streaming, use something like this:
        # self.setPixmap(img.scaled(
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height(),
        #     Qt.KeepAspectRatio))

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

    def mousePressEvent(self, event):
        """Swap this video with the big video on click."""
        if self.row != -1:
            self.update_big_video_signal.emit(self)


class VideoArea(Module):
    """Container widget handling all video streams."""

    handle_front_frame_signal = pyqtSignal(Image)

    def __init__(self, num_video_widgets):
        super().__init__()
        rclpy.init()  # We'll need to create ROS nodes

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)
        self.grid_layout.setRowStretch(0, 3)

        self.video_widgets = []

        self.cv_bridge = CvBridge()
        self.handle_front_frame_signal.connect(self.handle_front_frame)
        camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, '/front_cam/image_raw', self.handle_front_frame_signal)
        camera_subscriber.spin_async()

        # MAGIC VALUE WARNING: -1 represents the big video
        for i in range(-1, num_video_widgets - 1):
            video = VideoWidget(i)
            self.video_widgets.append(video)
            video.update_big_video_signal.connect(self.set_as_big_video)

            if i == -1:
                self.grid_layout.addWidget(video, 0, 0, 1, 3)
            else:
                self.grid_layout.addWidget(video, 1, i, 1, 1)

    @pyqtSlot(QWidget)
    def set_as_big_video(self, target_widget: VideoWidget):
        """Swap target VideoWidget with big VideoWidget."""
        big_widget: QWidget = self.grid_layout.itemAtPosition(
            0, 0).widget()

        self.grid_layout.removeWidget(target_widget)
        self.grid_layout.removeWidget(big_widget)

        big_widget.row = target_widget.row
        target_widget.row = -1  # -1 still represents the big video

        self.grid_layout.addWidget(target_widget, 0, 0, 1, 3)
        self.grid_layout.addWidget(big_widget, 1, big_widget.row, 1, 1)

    @pyqtSlot(Image)
    def handle_front_frame(self, frame: Image):
        cv_image = self.cv_bridge.imgmsg_to_cv2(frame, desired_encoding='passthrough')

        # TODO: dynamic image scaling based on Qt element size
        qt_image = convert_cv_qt(cv_image, 500, 500)

        self.video_widgets[0].setPixmap(qt_image)

        # self.video_widgets[0].setPixmap(qt_image.scaled(
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height(),
        #     Qt.KeepAspectRatio))


def convert_cv_qt(cv_img, width=None, height=None):
    """Convert from an opencv image to QPixmap"""

    if len(cv_img.shape) == 3:
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = cv_img.shape
        bytes_per_line = ch * w

        img_format = QtGui.QImage.Format_RGB888

    elif len(cv_img.shape) == 2:
        h, w = cv_img.shape
        bytes_per_line = w

        img_format = QtGui.QImage.Format_Grayscale8

    convert_to_Qt_format = QtGui.QImage(cv_img.data, w, h, bytes_per_line, img_format)

    if width is not None:
        convert_to_Qt_format = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)

    return QtGui.QPixmap.fromImage(convert_to_Qt_format)
