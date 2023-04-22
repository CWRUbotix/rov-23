import sys
import numpy as np
from typing import List
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout

class SeagrassGrid():
    def __init__(self):
        self.root_layout = QGridLayout()

        N = 8
        BUTTON_SIZE = 50

        for row in range(N): 
           for col in range(N): 
                
                button = QPushButton()
                button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                button.setStyleSheet("background-color : green")

                button.clicked.connect(self.on_click)

                self.root_layout.addWidget(button, row, col)
        
        self.grid: List[List[bool]] = np.full((N, N), False, dtype=bool)
 
    def on_click(self):
        print("PyQt5 button click")

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

    sea_grass = Seagrass()
    sys.exit(app.exec_())
