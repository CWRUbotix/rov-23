import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication

class PushButton(QPushButton):
    def __init__(self, text, parent=None):
        super(PushButton, self).__init__(text, parent)

        # self.setText(text)
        # self.setMinimumSize(QSize(50, 50))
        # self.setMaximumSize(QSize(50, 50))

class SeaGrass(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        root_layout = QWidget()
        self.layout = QGridLayout(root_layout)

        N = 8

        for row in range(N): 
           for col in range(N): 
                
                button = QPushButton("0", self)
                button.clicked.connect(self.on_click)

                self.layout.addWidget(button, row, col)

        self.show()

    def on_click(self):
        print("PyQt5 button click")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    sea_grass = SeaGrass()
    sys.exit(app.exec_())
