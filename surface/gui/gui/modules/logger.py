from typing import List

from rcl_interfaces.msg import Log
from rclpy.logging import LoggingSeverity

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QTextEdit
from PyQt5.QtGui import QFont, QTextCursor, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from gui.event_nodes.subscriber import GUIEventSubscriber

# Names and log text colors for each message severity
SEVERITY_LEVELS_DICT = {LoggingSeverity.UNSET: QColor(0, 0, 0),
                        LoggingSeverity.DEBUG: QColor(50, 50, 50),
                        LoggingSeverity.INFO: QColor(150, 150, 150),
                        LoggingSeverity.WARN: QColor(150, 150, 0),
                        LoggingSeverity.ERROR: QColor(255, 0, 0),
                        LoggingSeverity.FATAL: QColor(168, 0, 0)}


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
        for severity_key in SEVERITY_LEVELS_DICT:
            box: QCheckBox = QCheckBox(severity_key.name)
            box.setChecked(True)
            self.checkboxes.append(box)
            settings_layout.addWidget(box)

        self.textbox: QTextEdit = QTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setLineWrapMode(QTextEdit.NoWrap)
        layout.addWidget(self.textbox)

        self.terminal_font: QFont = self.textbox.font()
        self.terminal_font.setFamily("Courier")
        self.terminal_font.setPointSize(11)

        self.print_log_signal.connect(self.print_log)
        self.subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Log, '/rosout', self.print_log_signal)

    @pyqtSlot(Log)
    def print_log(self, message: Log) -> None:
        """Print message to log widget if user is viewing message's type."""
        # Message severities are 0, 10, 20, etc.
        # We divide by 10 to get index for checkboxes
        severity_key = LoggingSeverity(message.level)
        index = int(message.level / 10)
        # TODO maybe could do some dict for LoggingSeverity and checkboxes to save division
        # Make sure we've chosen to view this message type
        if not self.checkboxes[index].isChecked():
            return

        self.textbox.moveCursor(QTextCursor.End)
        self.textbox.setCurrentFont(self.terminal_font)
        self.textbox.setTextColor(SEVERITY_LEVELS_DICT[severity_key])
        self.textbox.insertPlainText(f'[{severity_key.name}]\t{message.msg}\n')

    def kill_all_executors(self):
        self.subscriber.kill_executor()
