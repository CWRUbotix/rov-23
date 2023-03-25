
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel
from gui.event_nodes.publisher import GUIEventPublisher, GUIEventSubscription
from gui.modules.module import Module


class FloatComm(Module):
    """Arm widget for sending Arm Commands."""

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        submerge_button = QPushButton()
        extend_button = QPushButton()
        retract_button = QPushButton()

        submerge_button.setText("Submerge")
        extend_button.setText("Extend")
        retract_button.setText("Retract")

        submerge_button.setFixedSize(300, 200)
        extend_button.setFixedSize(300, 200)
        retract_button.setFixedSize(300, 200)

        submerge_button.clicked.connect(self.submerge_clicked)
        extend_button.clicked.connect(self.extend_clicked)
        retract_button.clicked.connect(self.retract_clicked)

        layout.addWidget(submerge_button)
        layout.addWidget(extend_button)
        layout.addWidget(retract_button)

        self.label : QLabel = QLabel()
        self.label.setText('Waiting for radio...')
        layout.addWidget(self.label)

        self.tranciever_publisher: GUIEventPublisher = GUIEventPublisher(
            String,
            "tranciever_control"
        )

        self.tranciever_subscription: GUIEventSubscription = GUIEventSubscription(
            String,
            "tranciever_data",
            self.update_text
        )
    
    def update_text(self, msg):
        self.label.setText(msg)

    def submerge_clicked(self):
        self.tranciever_publisher.publish("submerge")

    def extend_clicked(self):
        self.tranciever_publisher.publish("extend")

    def retract_clicked(self):
        self.tranciever_publisher.publish("retract")