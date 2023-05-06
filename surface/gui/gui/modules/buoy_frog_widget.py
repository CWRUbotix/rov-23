from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from cv2 import Mat
import cv2
import os

from gui.modules.video_area import VideoWidget


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
        if not os.path.exists("video"):
            os.makedirs("video")

        writer = cv2.VideoWriter(
            f"video/{self.mode}.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 180, (320, 240)
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
