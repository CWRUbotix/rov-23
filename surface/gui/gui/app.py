from rclpy.node import Node
import rclpy

from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication
import qdarkstyle
from PyQt5.QtGui import QCloseEvent
import sys
import signal

from gui.modules.task_selector import TaskSelector
from gui.modules.video_area import VideoArea
from gui.modules.logger import Logger


class App(Node, QWidget):
    """Main app window."""

    def __init__(self):
        super().__init__(node_name='app_node', parameter_overrides=[])
        super(QWidget, self).__init__()

        self.declare_parameter('theme', '')

        self.setWindowTitle('ROV 2023')
        self.resize(1850, 720)

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.video_area = VideoArea(4)
        layout.addWidget(self.video_area, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 1, 0)

    # Variable name a0 because it's overloading parent closeEvent method
    def closeEvent(self, a0: QCloseEvent):
        """Piggyback the PyQt window close to kill rclpy."""
        # Kill all executors
        self.task_selector.kill_all_executors()
        self.logger.kill_all_executors()

        # Shutdown rclpy
        rclpy.shutdown()
        a0.accept()


def run_app():
    rclpy.init()

    # Kills with Control + C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    window = App()
    if window.get_parameter('theme').get_parameter_value().string_value == "dark":
        # https://doc.qt.io/qt-5/qwidget.html#setStyle
        window.setStyleSheet(qdarkstyle.load_stylesheet())
    elif window.get_parameter('theme').get_parameter_value().string_value == "watermelon":
        # UGLY But WORKS
        window.setStyleSheet("QWidget { background-color: green; color: pink; }")

    window.show()
    sys.exit(app.exec_())
