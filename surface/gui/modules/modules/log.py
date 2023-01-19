from math import floor
from typing import List
from threading import Thread

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPlainTextEdit, QTextEdit
from PyQt5.QtGui import QFont, QTextCursor, QColor
from event_nodes.subscriber import GUIEventSubscriber

from rcl_interfaces.msg import Log
import rclpy

SEVERITY_LEVELS = [
    {
        'name': 'Unset',
        'color': QColor(0, 0, 0)
    },
    {
        'name': 'Debug',
        'color': QColor(50, 50, 50)
    },
    {
        'name': 'Info',
        'color': QColor(150, 150, 150)
    },
    {
        'name': 'Warn',
        'color': QColor(150, 150, 0)
    },
    {
        'name': 'Error',
        'color': QColor(255, 0, 0)
    },
    {
        'name': 'Fatal',
        'color': QColor(168, 0, 0)
    }
]


class Logger(QWidget):
    def __init__(self):
        super().__init__()

        layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(layout)

        settings_layout: QHBoxLayout = QHBoxLayout()
        layout.addLayout(settings_layout)

        self.checkboxes: List[QCheckBox] = []
        for severity in SEVERITY_LEVELS:
            box: QCheckBox = QCheckBox(severity['name'])
            self.checkboxes.append(box)
            settings_layout.addWidget(box)
            box.setChecked(True)

        self.textbox: QTextEdit = QTextEdit()
        layout.addWidget(self.textbox)
        self.textbox.setReadOnly(True)
        self.textbox.setLineWrapMode(QTextEdit.NoWrap)

        self.font: QFont = self.textbox.font()
        self.font.setFamily("Courier")
        self.font.setPointSize(11)

        self.subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Log, '/rosout', self.print_log)

        subscriber_thread: Thread = Thread(
            target=self.spin_subscriber, daemon=True)
        subscriber_thread.start()

    def spin_subscriber(self):
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self.subscriber)
        executor.spin()

    def print_log(self, message):
        severity_index = floor(message.level / 10)
        if severity_index < 0 or severity_index > 5:
            severity_index = 5  # Unset severity

        # Make sure we've chosen to view this message type
        if not self.checkboxes[severity_index].isChecked():
            return

        self.textbox.moveCursor(QTextCursor.End)
        self.textbox.setCurrentFont(self.font)
        self.textbox.setTextColor(SEVERITY_LEVELS[severity_index]['color'])

        self.textbox.insertPlainText(
            f'[{SEVERITY_LEVELS[severity_index]["name"]}]\t{message.msg}\n')
