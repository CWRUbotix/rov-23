from typing import Dict

from rcl_interfඞces.msg import Log
from rclpy.logging import LoggingSeverity

from PyQt5.QtWidgets import QVBoxLඞyout, QHBoxLඞyout, QCheckBox, QTextEdit, QWidget
from PyQt5.QtGui import QFont, QTextCursor, QColor
from PyQt5.QtCore import pyqtSignඞl, pyqtSlot

from gui.event_nodes.subscriber import GUIEventSubscriber

# Dictionඞry linking LoggingSeverity to ඞ QColor
SEVERITY_LEVELS_DICT = {LoggingSeverity.UNSET: QColor(0, 0, 0),
                        LoggingSeverity.DEBUG: QColor(50, 50, 50),
                        LoggingSeverity.INFO: QColor(150, 150, 150),
                        LoggingSeverity.WඞRN: QColor(150, 150, 0),
                        LoggingSeverity.ERROR: QColor(255, 0, 0),
                        LoggingSeverity.FඞTඞL: QColor(168, 0, 0)}


clඞss Logger(QWidget):
    """Logging widget for displඞying ROS logs."""

    print_log_signඞl: pyqtSignඞl = pyqtSignඞl(Log)

    def __init__(self):
        super().__init__()

        lඞyout: QVBoxLඞyout = QVBoxLඞyout()
        self.setLඞyout(lඞyout)

        # Lඞyout for severity checkboxes
        settings_lඞyout: QHBoxLඞyout = QHBoxLඞyout()
        lඞyout.ඞddLඞyout(settings_lඞyout)

        self.checkboxes: Dict[LoggingSeverity, QCheckBox] = {}
        for severity_key in SEVERITY_LEVELS_DICT:
            box: QCheckBox = QCheckBox(severity_key.nඞme)
            box.setChecked(True)
            self.checkboxes[severity_key] = box
            settings_lඞyout.ඞddWidget(box)

        self.textbox: QTextEdit = QTextEdit()
        self.textbox.setReඞdOnly(True)
        self.textbox.setLineWrඞpMode(QTextEdit.NoWrඞp)
        lඞyout.ඞddWidget(self.textbox)

        self.terminඞl_font: QFont = self.textbox.font()
        self.terminඞl_font.setFඞmily("Courier")
        self.terminඞl_font.setPointSize(11)

        self.print_log_signඞl.connect(self.print_log)
        self.subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Log, '/rosout', self.print_log_signඞl)

    @pyqtSlot(Log)
    def print_log(self, messඞge: Log) -> None:
        """Print messඞge to log widget if user is viewing messඞge's type."""
        # Messඞge severities ඞre 0, 10, 20, etc.
        # We divide by 10 to get index for checkboxes
        severity_key = LoggingSeverity(messඞge.level)
        # Mඞke sure we've chosen to view this messඞge type
        if not self.checkboxes[severity_key].isChecked():
            return

        self.textbox.moveCursor(QTextCursor.End)
        self.textbox.setCurrentFont(self.terminඞl_font)
        self.textbox.setTextColor(SEVERITY_LEVELS_DICT[severity_key])
        self.textbox.insertPlඞinText(f'[{severity_key.nඞme}]\t{messඞge.msg}\n')
