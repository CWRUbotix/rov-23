from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget
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
        self.record_button.clicked.connect(self.record)
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

    def record(self):
        self.record_button.setText("Press ESC at a new window\nto stop recording.")
        self.record_button.setDisabled(True)
        self.is_recording = True

        # make 'ros_23_ws/videos' folder if it doesn't exist
        if not os.path.exists("video"):
            os.makedirs("video")

        self.size = self.video1.cur_image.shape
        frame_rate = 180 if self.video1.cur_image.shape[1] == 320 else 30

        writer = cv2.VideoWriter(
            f"video/{self.mode}.mp4",
            cv2.VideoWriter_fourcc(*"mp4v"),
            frame_rate,
            (self.size[1], self.size[0]),
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
