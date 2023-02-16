
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from gui.event_nodes.publisher import GUIEventPublisher
from gui.modules.module import Module

from rov_interfaces.msg import Armed


class Arm(Module):
    """Logging widget for displaying ROS logs."""

    armed_msg: Armed = Armed()

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        arm_button = QPushButton()
        disarm_button = QPushButton()

        arm_button.setText("Arm")
        disarm_button.setText("Disarm")

        arm_button.clicked.connect(self.arm_clicked)
        disarm_button.clicked.connect(self.disarm_clicked)

        layout.addWidget(arm_button)
        layout.addWidget(disarm_button)

        self.arm_publisher: GUIEventPublisher = GUIEventPublisher(
            Armed,
            "armed"
        )

    def arm_clicked(self):
        self.armed_msg.armed = True
        self.arm_publisher.publish(self.armed_msg)

    def disarm_clicked(self):
        self.armed_msg.armed = False
        self.arm_publisher.publish(self.armed_msg)
