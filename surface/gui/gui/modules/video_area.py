from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QMouseEvent

class VideoWidget(QLabel):
    """A single video stream widget."""

    update_big_video_signal = pyqtSignal(QWidget)

    def __init__(self, row: int):
        super().__init__()

        self.row = row

        # For debugging, display row number in each VideoWidget
        self.setText(str(row))

        # TODO: For actual streaming, use something like this:
        # self.setPixmap(img.scaled(
        #     self.frameGeometry().width(),
        #     self.frameGeometry().height(),
        #     Qt.KeepAspectRatio))

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

    def mousePressEvent(self, ev: QMouseEvent):
        """Swap this video with the big video on click."""
        if self.row != -1:
            self.update_big_video_signal.emit(self)


class VideoArea(QWidget):
    """Container widget handling all video streams."""

    def __init__(self, num_video_widgets: int):
        super().__init__()

        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)
        self.grid_layout.setRowStretch(0, 3)

        self.video_widgets = []

        # MAGIC VALUE WARNING: -1 represents the big video
        for i in range(-1, num_video_widgets - 1):
            video = VideoWidget(i)
            self.video_widgets.append(video)
            video.update_big_video_signal.connect(self.set_as_big_video)

            if i == -1:
                self.grid_layout.addWidget(video, 0, 0, 1, 3)
            else:
                self.grid_layout.addWidget(video, 1, i, 1, 1)

    @pyqtSlot(QWidget)
    def set_as_big_video(self, target_widget: VideoWidget):
        """Swap target VideoWidget with big VideoWidget."""
        big_widget: QWidget = self.grid_layout.itemAtPosition(
            0, 0).widget()

        self.grid_layout.removeWidget(target_widget)
        self.grid_layout.removeWidget(big_widget)

        big_widget.row = target_widget.row
        target_widget.row = -1  # -1 still represents the big video

        self.grid_layout.addWidget(target_widget, 0, 0, 1, 3)
        self.grid_layout.addWidget(big_widget, 1, big_widget.row, 1, 1)
