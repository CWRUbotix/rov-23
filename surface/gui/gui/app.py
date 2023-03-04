import qdarkstyle
import sys
import signal

import rclpy
from rclpy.node import Node

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
import atexit


class App(Node, QWidget):
    """Main app window."""

    def __init__(self, node_name: str):
        self.app: QApplication = QApplication(sys.argv)
        rclpy.init()

        super().__init__(
            node_name=node_name,
            parameter_overrides=[],
            namespace='surface/gui')
        super(QWidget, self).__init__()

        self.declare_parameter('theme', '')
        self.resize(1850, 720)

        def kill():
            self.destroy_node()
            rclpy.shutdown()

        atexit.register(kill)

    def run_gui(self):
        # Kills with Control + C
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        if self.get_parameter('theme').get_parameter_value().string_value == "dark":
            # https://doc.qt.io/qt-5/qwidget.html#setStyle
            self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        elif self.get_parameter('theme').get_parameter_value().string_value == "watermelon":
            # UGLY But WORKS
            self.app.setStyleSheet("QWidget { background-color: green; color: pink; }")

        self.show()
        sys.exit(self.app.exec_())
