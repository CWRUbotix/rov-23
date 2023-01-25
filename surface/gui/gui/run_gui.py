import sys

from PyQt5.QtWidgets import QApplication

from app import App

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())
