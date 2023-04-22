import sys
import numpy as np
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QLabel

class SeagrassButton(QPushButton):
    def __init__(self, size: int):
        super(SeagrassButton, self).__init__()

        self.setFixedSize(size, size)

        self.color: str = "green"
        self.setStyleSheet("background-color :" + self.color)

        self.clicked.connect(self.toggle_button_color)

        self.recovered = True

    def toggle_button_color(self):
        new_color: str

        if self.color == "white":
            new_color = "green"
        else:
            new_color = "white"

        self.color = new_color
        self.recovered = not self.recovered

        self.setStyleSheet("background-color :" + new_color)

class SeagrassGrid():
    def __init__(self, text:str=""):
        self.root_layout = QVBoxLayout()

        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)

        self.root_layout.addWidget(label)

        grid = QGridLayout()
        self.root_layout.addLayout(grid)

        self.all_buttons: List[QPushButton] = []

        N = 8

        for row in range(N): 
           for col in range(N): 
                
                seagrass_button = SeagrassButton(size=50)
                grid.addWidget(seagrass_button, row, col)
                self.all_buttons.append(seagrass_button)

    def get_num_recovered(self) -> int:
        num_recovered: List[bool] = [button.recovered for button in self.all_buttons]

        return np.count_nonzero(num_recovered)

class Seagrass(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(1200, 400)

        root_layout = QHBoxLayout(self)

        self.before_grid = SeagrassGrid("Before")
        self.after_grid = SeagrassGrid("After")

        root_layout.addLayout(self.before_grid.root_layout)
        root_layout.addStretch()
        root_layout.addLayout(self.after_grid.root_layout)

        # Panel with result text and get difference button
        sub_widget = QWidget()
        sub_widget.setMinimumWidth(200)

        result_layout = QVBoxLayout()
        result_layout.addStretch()

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

        root_layout.addWidget(sub_widget)

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

    seagrass = Seagrass()
    sys.exit(app.exec_())
