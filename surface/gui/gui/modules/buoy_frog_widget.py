from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
import cv2
import os, threading

from gui.modules.video_area import VideoWidget


class BuoyFrogWidget(QWidget):
    CAMERA_TOPICS = ["/front_cam/image_raw", "/bottom_cam/image_raw"]

    def __init__(self):
        super().__init__()
        self.mode = "buoy"
        self.is_recording = False

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video1: VideoWidget = VideoWidget(0, self.CAMERA_TOPICS[0])
        self.video2: VideoWidget = VideoWidget(1, self.CAMERA_TOPICS[1])
        self.video1.setStyleSheet("border: 5px solid green;")

        self.mode_button = QPushButton()
        self.mode_button.setText("Toggle Mode\nCurrent: Buoy")
        self.mode_button.clicked.connect(self.toggle_mode)
        self.mode_button.setFixedSize(200, 100)

        self.record_button = QPushButton()
        self.record_button.setText("Record")
        self.record_button.clicked.connect(self.toggle_record)
        self.record_button.setFixedSize(200, 100)

        layout.addWidget(self.video1, 0, 0)
        layout.addWidget(self.video2, 0, 1)
        layout.addWidget(self.mode_button, 1, 0)
        layout.addWidget(self.record_button, 1, 1)

    def toggle_mode(self):
        # toggle video widget between video1 and video2 at first item of the layout
        if self.mode == "buoy":
            self.mode = "frog"
            self.mode_button.setText("Toggle Mode\nCurrent: Frog")
            self.video1.setStyleSheet("border: none;")
            self.video2.setStyleSheet("border: 5px solid green;")
        else:
            self.mode = "buoy"
            self.mode_button.setText("Toggle Mode\nCurrent: Buoy")
            self.video1.setStyleSheet("border: 5px solid green;")
            self.video2.setStyleSheet("border: none;")

    def toggle_record(self):
        if self.is_recording:
            self.is_recording = False
            self.mode_button.setEnabled(True)
            self.record_button.setText("Record")
        else:
            self.is_recording = True
            self.record_button.setText("Stop Recording")
            self.mode_button.setEnabled(False)
            threading.Thread(target=self.record).start()

    def record(self):
        dir_path = "video"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        self.size = self.video1.cur_image.shape
        fps = 3600 if self.size[1] == 320 else 30

        video_writer = cv2.VideoWriter(
            f"{dir_path}/{self.mode}.mp4",
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
