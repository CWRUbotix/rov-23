import sys
import numpy as np
from typing import List
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QLabel

class SeagrassButton(QPushButton):
    def __init__(self, size: int):
        super(SeagrassButton, self).__init__()

        self.setFixedSize(size, size)

        self.color: str = "green"
        self.setStyleSheet("background-color :" + self.color)

        self.clicked.connect(self.on_click)

        self.recovered = True

    def on_click(self):
        self.toggle_button_color()

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
    def __init__(self):
        self.root_layout = QGridLayout()
        self.all_buttons: List[QPushButton] = []

        N = 8

        for row in range(N): 
           for col in range(N): 
                
                seagrass_button = SeagrassButton(size=50)
                self.root_layout.addWidget(seagrass_button, row, col)
                self.all_buttons.append(seagrass_button)

    def get_num_recovered(self) -> int:
        num_recovered: List[bool] = [button.recovered for button in self.all_buttons]

        return np.count_nonzero(num_recovered)

class Seagrass(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.resize(1200, 600)

        self.root_layout = QHBoxLayout(self)

        self.before_grid = SeagrassGrid()
        self.after_grid = SeagrassGrid()

        self.root_layout.addLayout(self.before_grid.root_layout)
        self.root_layout.addLayout(self.after_grid.root_layout)

        # Panel with result text and get difference button
        result_layout = QVBoxLayout()
        result_layout.addStretch()

        get_diff_button = QPushButton("Get Difference")
        get_diff_button.clicked.connect(self.get_diff)

        self.before_label = QLabel("Before: ")
        self.after_label = QLabel("After: ")
        self.diff_label = QLabel()

        result_layout.addWidget(self.before_label)
        result_layout.addWidget(self.after_label)
        result_layout.addWidget(self.diff_label)
        result_layout.addWidget(get_diff_button)

        self.root_layout.addLayout(result_layout)

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
