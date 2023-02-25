
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from gui.event_nodes.publisher import GUIEventPublisher
from gui.modules.module import Module

from interfaces.msg import Armed


class Arm(Module):
    """Arm widget for sending Arm Commands."""

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        arm_button = QPushButton()
        disarm_button = QPushButton()

        arm_button.setText("Arm")
        disarm_button.setText("Disarm")

        arm_button.setFixedSize(300, 200)
        disarm_button.setFixedSize(300, 200)

        arm_button.clicked.connect(self.arm_clicked)
        disarm_button.clicked.connect(self.disarm_clicked)

        layout.addWidget(arm_button)
        layout.addWidget(disarm_button)

        self.arm_publisher: GUIEventPublisher = GUIEventPublisher(
            Armed,
            "armed"
        )

    def arm_clicked(self):
        self.arm_publisher.publish(Armed(armed=True))

    def disarm_clicked(self):
        self.arm_publisher.publish(Armed(armed=False))
