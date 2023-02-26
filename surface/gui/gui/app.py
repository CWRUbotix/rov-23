import typing
import qdarkstyle
import sys
import signal

import rclpy
from rclpy.node import Node

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QCloseEvent

from gui.modules.module import Module


class App(Node, QWidget):
    """Main app window."""

    def __init__(self, node_name: str):
        super().__init__(
            node_name=node_name,
            parameter_overrides=[],
            namespace='surface/gui')
        super(QWidget, self).__init__()

        self.declare_parameter('theme', '')
        self.modules: list[Module] = []

        self.resize(1850, 720)

    # Variable name a0 because it's overloading parent closeEvent method
    def closeEvent(self, a0: QCloseEvent):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        for module in self.modules:
            module.kill_module()

        # Shutdown rclpy
        rclpy.shutdown()
        a0.accept()

def run_gui(gui_class: typing.Callable[[], App]):
    rclpy.init()

    # Kills with Control + C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app: QApplication = QApplication(sys.argv)

    gui_window = gui_class()

    if gui_window.get_parameter('theme').get_parameter_value().string_value == "dark":
        # https://doc.qt.io/qt-5/qwidget.html#setStyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    elif gui_window.get_parameter('theme').get_parameter_value().string_value == "watermelon":
        # UGLY But WORKS
        app.setStyleSheet("QWidget { background-color: green; color: pink; }")

    gui_window.show()
    sys.exit(app.exec_())
