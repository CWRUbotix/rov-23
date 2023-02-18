import rclpy
import qdarkstyle
import sys
import signal

from PyQt5.QtWidgets import QApplication

from src.surface.gui.gui.app import App


def run_app():
    rclpy.init()

    # Kills with Control + C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    window = App()
    if window.get_parameter('theme').get_parameter_value().string_value == "dark":
        # https://doc.qt.io/qt-5/qwidget.html#setStyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    elif window.get_parameter('theme').get_parameter_value().string_value == "watermelon":
        # UGLY But WORKS
        app.setStyleSheet("QWidget { background-color: green; color: pink; }")

    window.show()
    sys.exit(app.exec_())
