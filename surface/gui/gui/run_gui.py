import sys

from PyQt5.QtWidgets import QApplication

from app import App


def run_gui():
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec_())


# Only for 'python run_gui.py', not used by ROS launch files
if __name__ == '__main__':
    run_gui()
