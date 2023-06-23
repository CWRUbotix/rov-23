from datetime import datetime, timezone
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget
from gui.event_nodes.publisher import GUIEventPublisher
from gui.event_nodes.subscriber import GUIEventSubscriber
from interfaces.msg import FloatCommand
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class FloatComm(QWidget):
    """Arm widget for sending Arm Commands."""

    handle_scheduler_response_signal: pyqtSignal = pyqtSignal(FloatCommand)

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        submerge_button = QPushButton()

        submerge_button.setText("Submerge")
        submerge_button.setFixedSize(300, 200)
        submerge_button.clicked.connect(self.submerge_clicked)
        layout.addWidget(submerge_button)

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        set_time_button = QPushButton()

        set_time_button.setText("Submerge")
        set_time_button.setFixedSize(300, 200)
        set_time_button.clicked.connect(self.set_time_clicked)
        layout.addWidget(set_time_button)

        self.handle_scheduler_response_signal.connect(self.handle_text)

        self.label: QLabel = QLabel()
        self.label.setText('Waiting for radio...')
        layout.addWidget(self.label)

        self.transceiver_publisher: GUIEventPublisher = GUIEventPublisher(
            FloatCommand,
            "transceiver_control"
        )

        self.transceiver_subscription: GUIEventSubscriber = GUIEventSubscriber(
            FloatCommand,
            "transceiver_data",
            self.handle_scheduler_response_signal
        )

    @pyqtSlot(FloatCommand)
    def handle_text(self, msg: FloatCommand):
        self.label.setText(msg.command)

    def submerge_clicked(self):
        self.transceiver_publisher.publish(FloatCommand(command="submerge"))

    def set_time_clicked(self):
        utc = datetime.now(timezone.utc)
        self.transceiver_publisher.publish(FloatCommand(
            command=f"set_time {utc.hour:02d} {utc.minute:02d} {utc.second:02d}"))
