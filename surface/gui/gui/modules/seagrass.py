import sys
import numpy as np

from enum import Enum
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame


class SeagrassWidget(QWidget):
    def __init__(self):
        super().__init__()

        root_layout: QHBoxLayout = QHBoxLayout(self)

        self.after_grid: SeagrassGrid = SeagrassGrid(self)
        self.before_grid: SeagrassGrid = SeagrassGrid(self, self.after_grid)

        # Before layout
        before_layout: QVBoxLayout = QVBoxLayout()
        before_layout.addWidget((QLabel("Before")), alignment=Qt.AlignCenter)

        before_btns_layout: QHBoxLayout = QHBoxLayout()

        set_all_green: QPushButton = QPushButton("Set All Green")
        set_all_green.setMaximumWidth(120)
        set_all_green.clicked.connect(lambda: self.before_grid.reset_grid(Color.GREEN))

        set_all_white: QPushButton = QPushButton("Set All White")
        set_all_white.setMaximumWidth(120)
        set_all_white.clicked.connect(lambda: self.before_grid.reset_grid(Color.WHITE))

        before_btns_layout.addWidget(set_all_green)
        before_btns_layout.addWidget(set_all_white)

        before_layout.addLayout(before_btns_layout)
        before_layout.addWidget(self.before_grid.frame)

        before_layout.addStretch()

        # After layout        
        after_layout: QVBoxLayout = QVBoxLayout()
        after_layout.addWidget(QLabel("After"), alignment=Qt.AlignCenter)

        after_bttn_layout: QHBoxLayout = QHBoxLayout()

        match_before: QPushButton = QPushButton("Match Before")
        match_before.setMaximumWidth(120)
        match_before.clicked.connect(self.before_grid.update_connected_grid)

        after_bttn_layout.addWidget(match_before)

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

        # # Add all sections to main layout
        root_layout.addLayout(before_layout, 1)
        root_layout.addLayout(after_layout, 1)
        root_layout.addWidget(result_widget, 3)

        result_layout.addStretch()

        self.show()

    def update_result_text(self) -> None:
        before_num: int = self.before_grid.get_num_recovered()
        after_num: int = self.after_grid.get_num_recovered()

        diff: int = abs(after_num - before_num)

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


class Color(Enum):
    GREEN = "green"
    WHITE = "white"


class SeagrassGrid():
    def __init__(self, parent_widget: SeagrassWidget, connected_grid = None):
        self.parent_widget: SeagrassWidget = parent_widget
        self.connected_grid: SeagrassGrid = connected_grid

        grid_widget: QWidget = QWidget()
        grid_widget.setMaximumWidth(200)

        grid_layout: QGridLayout = QGridLayout()
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        grid_widget.setLayout(grid_layout)

        self.frame: QFrame = QFrame()
        self.frame.setLayout(grid_layout)
        self.frame.setStyleSheet("border: 1px solid gray")

        self.all_buttons: List[QPushButton] = []
        N = 8

        for row in range(N):
            for col in range(N):
                seagrass_button: SeagrassButton = SeagrassButton(size=50)

                seagrass_button.clicked.connect(self.update_connected_grid)
                seagrass_button.clicked.connect(self.update_result_text)

                grid_layout.addWidget(seagrass_button, row, col)
                self.all_buttons.append(seagrass_button)

    def reset_grid(self, color: Color) -> None:
        for button in self.all_buttons:
            button.set_color(color)

        if self.connected_grid:
            self.update_connected_grid()

        self.parent_widget.update_result_text()

    def get_num_recovered(self) -> int:
        num_recovered: List[bool] = [button.recovered for button in self.all_buttons]

        return np.count_nonzero(num_recovered)

    def update_connected_grid(self) -> None:
        if self.connected_grid == None:
            return

        for button1, button2 in zip(self.all_buttons, self.connected_grid.all_buttons):

            while button2.color != button1.color:
                button2.toggle_button_color()

    def update_result_text(self) -> None:
        self.parent_widget.update_result_text()


class SeagrassButton(QPushButton):
    def __init__(self, size: int):
        super(SeagrassButton, self).__init__()

        self.setFixedSize(size, size)

        self.color: Color = Color.GREEN
        self.set_color(self.color)

        self.clicked.connect(self.on_click)

        self.recovered = True

    def on_click(self) -> None:
        self.toggle_button_color()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    seagrass = SeagrassWidget()
    sys.exit(app.exec_())
