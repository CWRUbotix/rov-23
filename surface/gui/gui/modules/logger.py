from math import floor
from typing import List

from rcl_interfaces.msg import Log

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QTextEdit
from PyQt5.QtGui import QFont, QTextCursor, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from event_nodes.subscriber import GUIEventSubscriber

# Names and log text colors for each message severity
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
    """Logging widget for displaying ROS logs."""

    print_log_signal: pyqtSignal = pyqtSignal(Log)

    def __init__(self):
        super().__init__()

        layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(layout)

        # Layout for severity checkboxes
        settings_layout: QHBoxLayout = QHBoxLayout()
        layout.addLayout(settings_layout)

        self.checkboxes: List[QCheckBox] = []
        for severity in SEVERITY_LEVELS:
            box: QCheckBox = QCheckBox(severity['name'])
            box.setChecked(True)
            self.checkboxes.append(box)
            settings_layout.addWidget(box)

        self.textbox: QTextEdit = QTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.textbox)

        self.font: QFont = self.textbox.font()
        self.font.setFamily("Courier")
        self.font.setPointSize(11)

        self.print_log_signal.connect(self.print_log)
        self.subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Log, '/rosout', self.print_log_signal)
        self.subscriber.spin_async()

    @pyqtSlot(Log)
    def print_log(self, message: Log) -> None:
        """Print message to log widget if user is viewing message's type."""
        # Message severities are 0, 10, 20, etc.
        # We divide by 10 to get index for SEVERITY_LEVELS
        severity_index = floor(message.level / 10)
        if severity_index < 0 or severity_index > 5:
            severity_index = 0  # Unset severity

        # Make sure we've chosen to view this message type
        if not self.checkboxes[severity_index].isChecked():
            return

        self.textbox.moveCursor(QTextCursor.End)
        self.textbox.setCurrentFont(self.font)
        self.textbox.setTextColor(SEVERITY_LEVELS[severity_index]['color'])

        self.textbox.insertPlainText(
            f'[{SEVERITY_LEVELS[severity_index]["name"]}]\t{message.msg}\n')

    def kill_all_executors(self):
        self.subscriber.kill_executor()
