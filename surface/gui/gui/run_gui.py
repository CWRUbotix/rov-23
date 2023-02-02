import sys
from PyQt5.QtWidgets import QApplication
from gui.app import App
from rclpy.node import Node
import rclpy


class GUI(Node):
    def __init__(self):
        super().__init__('gui')

    def run_gui(self):
        app = QApplication(sys.argv)

        window = App()
        window.show()

        sys.exit(app.exec_())


def main():
    rclpy.init()
    GUI().run_gui()
