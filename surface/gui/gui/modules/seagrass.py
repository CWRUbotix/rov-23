import sys
import numpy as np
from typing import List
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout

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
        num_recovered: List[bool] = [button.covered for button in self.all_buttons]

        return np.count_nonzero(num_recovered)

class Seagrass(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.resize(1200, 600)
        self.root_layout = QHBoxLayout(self)
        
        actual = SeagrassGrid()
        expected = SeagrassGrid()

        self.root_layout.addLayout(actual.root_layout)
        self.root_layout.addLayout(expected.root_layout)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    seagrass = Seagrass()
    sys.exit(app.exec_())
