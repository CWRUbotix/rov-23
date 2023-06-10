
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget
from gui.event_nodes.publisher import GUIEventPublisher

from interfaces.msg import Armed


class Arm(QWidget):
    """Arm widget for sending Arm Commands."""

    BUTTON_WIDTH = 120
    BUTTON_HEIGHT = 60
    BUTTON_STYLESHEET = 'QPushButton { font-size: 20px; }'

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        arm_button = QPushButton()
        disarm_button = QPushButton()

        arm_button.setText("Arm")
        disarm_button.setText("Disarm")

        arm_button.setMinimumWidth(self.BUTTON_WIDTH)
        disarm_button.setMinimumWidth(self.BUTTON_WIDTH)

        arm_button.setMinimumHeight(self.BUTTON_HEIGHT)
        disarm_button.setMinimumHeight(self.BUTTON_HEIGHT)

        arm_button.setStyleSheet(self.BUTTON_STYLESHEET)
        disarm_button.setStyleSheet(self.BUTTON_STYLESHEET)

        arm_button.clicked.connect(self.arm_clicked)
        disarm_button.clicked.connect(self.disarm_clicked)

        layout.addWidget(arm_button)
        layout.addWidget(disarm_button)

        self.arm_publisher: GUIEventPublisher = GUIEventPublisher(
            Armed,
            "/armed"
        )

    def arm_clicked(self):
        self.arm_publisher.publish(Armed(armed=True))

    def disarm_clicked(self):
        self.arm_publisher.publish(Armed(armed=False))
