from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout, QWidget


class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.seconds_left = 15 * 60
        self.running = False

        self.label = QLabel('Label')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 36))

        self.toggle_btn = QPushButton('Start')
        self.reset_btn = QPushButton('Reset')

        self.toggle_btn.setCheckable(True)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.toggle_btn, 1, 0)
        layout.addWidget(self.reset_btn, 1, 1)

        self.toggle_btn.clicked.connect(self.toggle_timer)
        self.reset_btn.clicked.connect(self.reset_timer)

        self.setLayout(layout)

        self.update_label()

    def update_timer(self):
        self.seconds_left -= 1
        self.update_label()
        if self.seconds_left == 0:
            self.stop_timer()

    def update_label(self):
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.label.setText(f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    def toggle_timer(self):
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def start_timer(self):
        if self.seconds_left == 0:
            return
        self.running = True
        self.timer.start(1000)
        self.toggle_btn.setText("Pause")

    def stop_timer(self):
        self.running = False
        self.timer.stop()
        self.toggle_btn.setChecked(False)
        self.toggle_btn.setText("Start")

    def reset_timer(self):
        self.seconds_left = 15 * 60
        self.stop_timer()
        self.update_label()
