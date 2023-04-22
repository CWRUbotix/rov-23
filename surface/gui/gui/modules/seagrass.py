import sys
import numpy as np

from enum import Enum
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame


class Color(Enum):
    GREEN = "green"
    WHITE = "white"


class SeagrassButton(QPushButton):
    def __init__(self, size: int):
        super(SeagrassButton, self).__init__()

        self.setFixedSize(size, size)

        self.color: Color = Color.GREEN
        self.set_color(self.color)

        self.clicked.connect(self.toggle_button_color)

        self.recovered = True

    def toggle_button_color(self) -> None:
        new_color: Color

        if self.color == Color.WHITE:
            new_color = Color.GREEN
        else:
            new_color = Color.WHITE

        self.color = new_color
        self.recovered = not self.recovered

        self.set_color(new_color)

    def set_color(self, color: Color) -> None:
        self.color = color
        self.recovered = self.color == Color.GREEN

        self.setStyleSheet("border: 1px solid gray; background-color :" + color.value)


class SeagrassGrid():
    def __init__(self, text: str = ""):
        self.root_layout = QVBoxLayout()
        self.root_layout.setSpacing(0)
        # self.root_layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(text)
        self.root_layout.addWidget(label, alignment=Qt.AlignCenter)

        button_layout = QHBoxLayout()

        set_all_green = QPushButton("Set All Green")
        set_all_green.setMaximumWidth(120)
        set_all_green.clicked.connect(lambda: self.reset_grid(Color.GREEN))

        set_all_white = QPushButton("Set All White")
        set_all_white.setMaximumWidth(120)
        set_all_white.clicked.connect(lambda: self.reset_grid(Color.WHITE))

        button_layout.addWidget(set_all_green)
        button_layout.addWidget(set_all_white)

        self.root_layout.addWidget(label, alignment=Qt.AlignCenter)
        self.root_layout.addLayout(button_layout)

        grid_widget = QWidget()
        grid_widget.setMaximumWidth(200)

        grid = QGridLayout()
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)

        grid_widget.setLayout(grid)

        frame = QFrame()
        frame.setLayout(grid)
        frame.setStyleSheet("border: 1px solid gray")

        self.root_layout.addWidget(frame)
        self.root_layout.addStretch()

        self.all_buttons: List[QPushButton] = []
        N = 8

        for row in range(N):
            for col in range(N):
                seagrass_button: SeagrassButton = SeagrassButton(size=50)
                grid.addWidget(seagrass_button, row, col)
                self.all_buttons.append(seagrass_button)

    def reset_grid(self, color: Color) -> None:
        for button in self.all_buttons:
            button.set_color(color)

    def get_num_recovered(self) -> int:
        num_recovered: List[bool] = [button.recovered for button in self.all_buttons]

        return np.count_nonzero(num_recovered)


class SeagrassWidget(QWidget):
    def __init__(self):
        super().__init__()

        root_layout = QHBoxLayout(self)

        self.before_grid = SeagrassGrid("Before")
        self.after_grid = SeagrassGrid("After")

        root_layout.addLayout(self.before_grid.root_layout, 1)
        root_layout.addLayout(self.after_grid.root_layout, 1)

        sub_widget = QWidget()

        result_layout = QVBoxLayout()

        sub_widget.setLayout(result_layout)

        get_diff_button = QPushButton("Get Difference")
        get_diff_button.clicked.connect(self.get_diff)

        self.before_label = QLabel("Before: ")
        self.after_label = QLabel("After: ")
        self.diff_label = QLabel()

        result_layout.addWidget(self.before_label)
        result_layout.addWidget(self.after_label)
        result_layout.addWidget(self.diff_label)
        result_layout.addWidget(get_diff_button)

        root_layout.addWidget(sub_widget, 3)

        result_layout.addStretch()

        self.show()

    def get_diff(self) -> None:
        before_num = self.before_grid.get_num_recovered()
        after_num = self.after_grid.get_num_recovered()

        diff = abs(after_num - before_num)

        result: str

        if after_num > before_num:
            result = f"{diff} went from white to green"
        elif after_num < before_num:
            result = f"{diff} went from green to white"
        else:
            result = "There was no change"

        self.before_label.setText(f"Before: {before_num} green")
        self.after_label.setText(f"After: {after_num} green")

        self.diff_label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    seagrass = SeagrassWidget()
    sys.exit(app.exec_())
