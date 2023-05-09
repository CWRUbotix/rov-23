from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
from PyQt5.QtCore import Qt
import cv2
import os
import threading

from gui.modules.video_widget import VideoWidget


class BuoyFrogWidget(QWidget):
    CAMERA_TOPICS = ["/front_cam/image_raw", "/bottom_cam/image_raw"]

    BUTTON_STYLESHEET = "QPushButton { font-size: 20px; }"

    SELECTED_STYLESHEET = (
        "QLabel { font-size: 20px; padding: 10px 0; background-color: yellowgreen; }"
    )
    UNSELECTED_STYLESHEET = (
        "QLabel { font-size: 20px; padding: 10px 0; background-color: none; }"
    )
    RECORDING_STYLESHEET = (
        "QLabel { font-size: 20px; padding: 10px 0; background-color: pink; }"
    )

    VIDEO_WIDTH: int = 900
    VIDEO_HEIGHT: int = 675

    def __init__(self):
        super().__init__()
        self.mode = "buoy"
        self.is_recording = False
        self.buoy_count = 1
        self.frog_count = 1

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video1: VideoWidget = VideoWidget(
            self.CAMERA_TOPICS[0],
            "Front Cam - Buoy Mission",
            self.VIDEO_WIDTH,
            self.VIDEO_HEIGHT,
        )
        self.video2: VideoWidget = VideoWidget(
            self.CAMERA_TOPICS[1],
            "Bottom Cam - Frog Mission",
            self.VIDEO_WIDTH,
            self.VIDEO_HEIGHT,
        )

        self.video1.label.setStyleSheet(self.SELECTED_STYLESHEET)
        self.video2.label.setStyleSheet(self.UNSELECTED_STYLESHEET)

        self.mode_button = QPushButton()
        self.mode_button.setText("Toggle Mode\nCurrent: Buoy")
        self.mode_button.setStyleSheet(self.BUTTON_STYLESHEET)
        self.mode_button.clicked.connect(self.toggle_mode)
        self.mode_button.setFixedSize(400, 100)

        self.record_button = QPushButton()
        self.record_button.setText("Record")
        self.record_button.setStyleSheet(self.BUTTON_STYLESHEET)
        self.record_button.clicked.connect(self.toggle_record)
        self.record_button.setFixedSize(400, 100)

        layout.addWidget(self.video1, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.video2, 0, 1, alignment=Qt.AlignCenter)
        layout.addWidget(self.mode_button, 1, 0, alignment=Qt.AlignRight)
        layout.addWidget(self.record_button, 1, 1, alignment=Qt.AlignLeft)

    def toggle_mode(self):
        # toggle video widget between video1 and video2 at first item of the layout
        if self.mode == "buoy":
            self.mode = "frog"
            self.mode_button.setText("Toggle Mode\nCurrent: Frog")
            self.video1.label.setStyleSheet(self.UNSELECTED_STYLESHEET)
            self.video2.label.setStyleSheet(self.SELECTED_STYLESHEET)
        else:
            self.mode = "buoy"
            self.mode_button.setText("Toggle Mode\nCurrent: Buoy")
            self.video1.label.setStyleSheet(self.SELECTED_STYLESHEET)
            self.video2.label.setStyleSheet(self.UNSELECTED_STYLESHEET)

    def toggle_record(self):
        if self.is_recording:
            self.is_recording = False
            self.mode_button.setEnabled(True)
            self.record_button.setText("Record")
            if self.mode == "buoy":
                self.video1.label.setStyleSheet(self.SELECTED_STYLESHEET)
            else:
                self.video2.label.setStyleSheet(self.SELECTED_STYLESHEET)
        else:
            self.is_recording = True
            self.mode_button.setEnabled(False)
            self.record_button.setText("Stop Recording")
            if self.mode == "buoy":
                self.video1.label.setStyleSheet(self.RECORDING_STYLESHEET)
            else:
                self.video2.label.setStyleSheet(self.RECORDING_STYLESHEET)
            threading.Thread(target=self.record).start()

    def record(self):
        dir_path = "video"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        self.size = self.video1.cur_image.shape
        fps = 3600 if self.size[1] == 320 else 30

        if self.mode == "buoy":
            count = self.buoy_count
            self.buoy_count += 1
        else:
            count = self.frog_count
            self.frog_count += 1

        video_writer = cv2.VideoWriter(
            f"{dir_path}/{self.mode}{count}.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (self.size[1], self.size[0]),
        )

        while self.is_recording:
            if self.mode == "buoy":
                video_writer.write(self.video1.cur_image)
            else:
                video_writer.write(self.video2.cur_image)

        video_writer.release()

    def blink_label(self):
        # Make the label of the selected video blink
        while self.is_recording:
            if self.mode == "buoy":
                self.video1.label.setStyleSheet(self.RECORDING_STYLESHEET)
            else:
                self.video2.label.setStyleSheet(self.RECORDING_STYLESHEET)
        # cv2.waitKey(500)

        # if self.mode == "buoy":
        #     self.video1.label.setStyleSheet(self.UNSELECTED_STYLESHEET)
        # else:
        #     self.video2.label.setStyleSheet(self.UNSELECTED_STYLESHEET)
        # cv2.waitKey(500)

        # if self.mode == "buoy":
        #     self.video1.label.setStyleSheet(self.SELECTED_STYLESHEET)
        # else:
        #     self.video2.label.setStyleSheet(self.SELECTED_STYLESHEET)
