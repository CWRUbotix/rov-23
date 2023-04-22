import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout

class SeaGrass(QWidget):

    def __init__(self):
        super().__init__()
        
        self.resize(600, 600)
        self.initUI()


    def initUI(self):
        root_layout = QGridLayout(self)
        
        N = 8
        BUTTON_SIZE = 50

        for row in range(N): 
           for col in range(N): 
                
                button = QPushButton("", self)
                button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                button.clicked.connect(self.on_click)

                root_layout.addWidget(button, row, col)

        self.show()

    def on_click(self):
        print("PyQt5 button click")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    sea_grass = SeaGrass()
    sys.exit(app.exec_())
