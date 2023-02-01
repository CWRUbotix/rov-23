import sys

from PyQt5.QtWidgets import QApplication

from gui.app import App


def run_gui():
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())
