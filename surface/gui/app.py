from PyQt5.QtWidgets import QWidget, QGridLayout

import rclpy

from modules.task_selector import TaskSelector


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ROV 2023')
        self.resize(1850, 720)

        layout: QGridLayout = QGridLayout()

        taskSelector: TaskSelector = TaskSelector()

        layout.addWidget(taskSelector)

        self.setLayout(layout)

    def closeEvent(self, event):
        # This shutdown should kill all nodes the GUI makes
        # rclpy.init() still needs to be called in each file that constructs a node
        rclpy.shutdown()

        event.accept()
