import sys

from typing import List, Optional, Callable
from cv2 import Mat

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QWidget, QPushButton, QGridLayout, QApplication,
                             QHBoxLayout, QVBoxLayout, QLabel, QFrame)
from PyQt5.QtGui import QPixmap, QImage

from gui.modules.video_area import VideoWidget
from sensor_msgs.msg import Image


class PausableVideoWidget(VideoWidget):

    def __init__(self, cam_topic: str):
        super().__init__(0, cam_topic)

        self.is_paused = False

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):

        if not self.is_paused:

            cv_image: Mat = self.cv_bridge.imgmsg_to_cv2(
                frame, desired_encoding='passthrough')

            qt_image: QImage = self.convert_cv_qt(
                cv_image,
                480,
                480
            )

            self.setPixmap(QPixmap.fromImage(qt_image))


class SeagrassWidget(QWidget):

    BUTTON_WIDTH = 120

    def __init__(self):
        super().__init__()

        root_layout: QHBoxLayout = QHBoxLayout(self)

        self.after_grid: SeagrassGrid = SeagrassGrid(self.update_result_text)
        self.before_grid: SeagrassGrid = SeagrassGrid(self.update_result_text,
                                                      self.after_grid.set_button)
        # Before layout
        before_layout: QVBoxLayout = QVBoxLayout()

        before_btns_layout: QHBoxLayout = QHBoxLayout()

        set_all_green: QPushButton = QPushButton("Set All Green")
        set_all_green.setMaximumWidth(self.BUTTON_WIDTH)
        set_all_green.clicked.connect(lambda: self.before_grid.reset_grid(True))

        set_all_white: QPushButton = QPushButton("Set All White")
        set_all_white.setMaximumWidth(self.BUTTON_WIDTH)
        set_all_white.clicked.connect(lambda: self.before_grid.reset_grid(False))

        before_btns_layout.addWidget(set_all_green)
        before_btns_layout.addWidget(set_all_white)

        before_layout.addWidget(QLabel("Before"), alignment=Qt.AlignCenter)
        before_layout.addLayout(before_btns_layout)
        before_layout.addWidget(self.before_grid.frame)

        before_layout.addStretch()

        # Bottom cam
        cam_layout: QVBoxLayout = QVBoxLayout()

        self.bottom_cam: PausableVideoWidget = PausableVideoWidget("/bottom_cam/image_raw")

        self.toggle_pause_bttn: QPushButton = QPushButton("Pause")
        self.toggle_pause_bttn.setMaximumWidth(self.BUTTON_WIDTH)
        self.toggle_pause_bttn.clicked.connect(self.toggle_pause)

        cam_layout.addWidget(QLabel("Bottom Camera"), alignment=Qt.AlignHCenter)
        cam_layout.addWidget(self.toggle_pause_bttn, alignment=Qt.AlignHCenter)
        cam_layout.addWidget(self.bottom_cam, alignment=Qt.AlignHCenter)

        # After layout
        after_layout: QVBoxLayout = QVBoxLayout()

        after_bttn_layout: QHBoxLayout = QHBoxLayout()

        match_before: QPushButton = QPushButton("Match Before")
        match_before.setMaximumWidth(120)
        match_before.clicked.connect(self.before_grid.update_connected_grid)

        after_bttn_layout.addWidget(match_before)

        after_layout.addWidget(QLabel("After"), alignment=Qt.AlignCenter)
        after_layout.addLayout(after_bttn_layout)
        after_layout.addWidget(self.after_grid.frame)

        after_layout.addStretch()

        # Result layout
        result_widget: QWidget = QWidget()
        result_layout: QVBoxLayout = QVBoxLayout()

        result_widget.setLayout(result_layout)

        self.before_label: QLabel = QLabel("Before: ")
        self.after_label: QLabel = QLabel("After: ")
        self.diff_label: QLabel = QLabel()

        result_layout.addWidget(self.before_label)
        result_layout.addWidget(self.after_label)
        result_layout.addWidget(self.diff_label)

        # Add all sections to main layout
        root_layout.addLayout(before_layout, 1)
        root_layout.addLayout(cam_layout, 3)
        root_layout.addLayout(after_layout, 1)
        root_layout.addWidget(result_widget, 2)

        result_layout.addStretch()

        self.show()

    def toggle_pause(self) -> None:
        self.bottom_cam.is_paused = not self.bottom_cam.is_paused

        if self.bottom_cam.is_paused:
            self.toggle_pause_bttn.setText("Unpause")
        else:
            self.toggle_pause_bttn.setText("Pause")

    def update_result_text(self) -> None:
        before_num: int = self.before_grid.get_num_recovered()
        after_num: int = self.after_grid.get_num_recovered()

        diff: int = abs(after_num - before_num)

        if after_num > before_num:
            result = f"{diff} went from white to green"
        elif after_num < before_num:
            result = f"{diff} went from green to white"
        else:
            result = "There was no change"

        self.before_label.setText(f"Before: {before_num} green")
        self.after_label.setText(f"After: {after_num} green")

        self.diff_label.setText(result)


class SeagrassGrid(QWidget):
    def __init__(self, update_result_text: Callable,
                 set_other_button: Optional[Callable] = None):
        super().__init__()

        self.update_result_text: Callable = update_result_text
        self.set_other_button: Callable = set_other_button

        self.setMaximumWidth(200)

        grid_layout: QGridLayout = QGridLayout()
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(grid_layout)

        self.frame: QFrame = QFrame()
        self.frame.setLayout(grid_layout)
        self.frame.setStyleSheet("border: 1px solid gray")

        self.all_buttons: List[SeagrassButton] = []
        N = 8
        button_id = 0

        for row in range(N):
            for col in range(N):
                seagrass_button: SeagrassButton = SeagrassButton(button_id=button_id, size=50)
                self.all_buttons.append(seagrass_button)

                seagrass_button.clicked.connect(
                    (lambda local_button_id: 
                        lambda: self.toggle_button(local_button_id))(button_id))

                grid_layout.addWidget(seagrass_button, row, col)

                button_id += 1

    def reset_grid(self, recovered: bool) -> None:
        for button in self.all_buttons:
            button.set_color(recovered)

            if self.set_other_button:
                self.set_other_button(button.button_id, button.recovered)

        self.update_result_text()

    def get_num_recovered(self) -> int:
        num_recovered: int = 0

        for button in self.all_buttons:
            if button.recovered:
                num_recovered += 1
        
        return num_recovered

    def update_connected_grid(self) -> None:
        if self.set_other_button is None:
            return

        for button in self.all_buttons:
            self.set_other_button(button.button_id, button.recovered)

    def set_button(self, button_id: int, recovered: bool) -> None:
        button = self.all_buttons[button_id]
        button.set_color(recovered)

        if self.set_other_button is not None:
            self.set_other_button(button_id, recovered)

        self.update_result_text()

    def toggle_button(self, button_id: int) -> None:
        button = self.all_buttons[button_id]
        button.toggle_button_color()

        if self.set_other_button is not None:
            self.set_other_button(button_id, button.recovered)

        self.update_result_text()


class SeagrassButton(QPushButton):
    def __init__(self, button_id: int, size: int):
        super(SeagrassButton, self).__init__()

        self.button_id: int = button_id
        self.setFixedSize(size, size)

        self.recovered = True
        self.set_color(self.recovered)

    def toggle_button_color(self) -> None:
        self.recovered = not self.recovered

        self.set_color(self.recovered)

    def set_color(self, recovered: bool) -> None:
        self.recovered = recovered

        if recovered:
            color = "green"
        else:
            color = "white"

        self.setStyleSheet("border: 1px solid gray; background-color :" + color)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    seagrass = SeagrassWidget()
    sys.exit(app.exec_())