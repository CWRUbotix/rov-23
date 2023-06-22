
from PyQt5.QtWidgets import QTextEdit, QHBoxLayout, QWidget
from gui.event_nodes.subscriber import GUIEventSubscriber
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from std_msgs.msg import Bool


class FloodStatus(QWidget):

    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 60

    flood_signl = pyqtSignal(Bool)

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        self.flood_text = QTextEdit()

        self.flood_text.setText("No Flooding")

        self.flood_text.setMinimumWidth(self.BUTTON_WIDTH)
        self.flood_text.setMinimumHeight(self.BUTTON_HEIGHT)

        layout.addWidget(self.flood_text)

        self.flood_signl.connect(self.update_text)

        self.arm_publisher: GUIEventSubscriber = GUIEventSubscriber(
            Bool,
            "/flood_status",
            self.flood_signal
        )

    @pyqtSlot(Bool)
    def update_text(self, msg: Bool):
        self.flood_text.setText("Flooding Detected")

