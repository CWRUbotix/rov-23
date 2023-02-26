import rclpy
import qdarkstyle
import sys
import signal

from PyQt5.QtWidgets import QApplication

from gui.app import App
from gui.pilot_app import PilotApp
from gui.operator_app import OperatorApp


def run_gui(gui_window: App):
    rclpy.init()

    # Kills with Control + C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app: QApplication = QApplication(sys.argv)

    if gui_window.get_parameter('theme').get_parameter_value().string_value == "dark":
        # https://doc.qt.io/qt-5/qwidget.html#setStyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    elif gui_window.get_parameter('theme').get_parameter_value().string_value == "watermelon":
        # UGLY But WORKS
        app.setStyleSheet("QWidget { background-color: green; color: pink; }")

    gui_window.show()
    sys.exit(app.exec_())


def run_gui_pilot():
    run_gui(PilotApp())


def run_gui_operator():
    run_gui(OperatorApp())
