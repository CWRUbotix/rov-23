from datetime import datetime, timezone
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget
from gui.event_nodes.publisher import GUIEventPublisher
from gui.event_nodes.subscriber import GUIEventSubscriber
from interfaces.msg import FloatCommand
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from time import sleep


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

        set_hour_button = QPushButton()
        set_hour_button.setText("Set hour")
        set_hour_button.setFixedSize(100, 200)
        set_hour_button.clicked.connect(self.set_hour_clicked)
        layout.addWidget(set_hour_button)

        set_minute_button = QPushButton()
        set_minute_button.setText("Set minute")
        set_minute_button.setFixedSize(100, 200)
        set_minute_button.clicked.connect(self.set_minute_clicked)
        layout.addWidget(set_minute_button)

        set_second_button = QPushButton()
        set_second_button.setText("Set second")
        set_second_button.setFixedSize(100, 200)
        set_second_button.clicked.connect(self.set_second_clicked)
        layout.addWidget(set_second_button)

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

    def set_hour_clicked(self):
        utc = datetime.now(timezone.utc)
        self.transceiver_publisher.publish(FloatCommand(command="h" + chr(utc.hour + 50)))

    def set_minute_clicked(self):
        utc = datetime.now(timezone.utc)
        self.transceiver_publisher.publish(FloatCommand(command="m" + chr(utc.minute + 50)))

    def set_second_clicked(self):
        utc = datetime.now(timezone.utc)
        self.transceiver_publisher.publish(FloatCommand(command="s" + chr(utc.second + 50)))
