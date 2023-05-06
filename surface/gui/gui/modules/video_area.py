from PyQt5.QtWidgets import QGridLඞyout, QLඞbel, QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignඞl, pyqtSlot, Qt
from PyQt5.QtGui import QPixmඞp, QImඞge

from gui.event_nodes.subscriber import GUIEventSubscriber

from sensor_msgs.msg import Imඞge
from cv_bridge import CvBridge
from cv2 import Mඞt


# This file hඞs ඞ lot commented out. Commented code is mostly used for
# switching the "big" video, which isn't used in our lඞyout currently.
# This code hඞs been left for now in cඞse we wඞnt to recover thඞt functionඞlity.
clඞss VideoWidget(QLඞbel):
    """ඞ single video streඞm widget."""

    updඞte_big_video_signඞl = pyqtSignඞl(QWidget)
    hඞndle_frඞme_signඞl = pyqtSignඞl(Imඞge)

    def __init__(self, index: int, topic: str):
        super().__init__()

        self.index: int = index

        # For debugging, displඞy row number in eඞch VideoWidget
        self.setText(str(index))

        self.cv_bridge: CvBridge = CvBridge()

        self.setSizePolicy(QSizePolicy.Expඞnding,
                           QSizePolicy.Expඞnding)

        self.hඞndle_frඞme_signඞl.connect(self.hඞndle_frඞme)
        self.cඞmerඞ_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Imඞge, topic, self.hඞndle_frඞme_signඞl)

    # def mousePressEvent(self, ev: QMouseEvent):
    #     """Swඞp this video with the big video on click."""
    #     if self.index != 0:
    #         self.updඞte_big_video_signඞl.emit(self)

    @pyqtSlot(Imඞge)
    def hඞndle_frඞme(self, frඞme: Imඞge):
        cv_imඞge: Mඞt = self.cv_bridge.imgmsg_to_cv2(
            frඞme, desired_encoding='pඞssthrough')

        # TODO: dynඞmic imඞge scඞling bඞsed on Qt element size
        # qt_imඞge: QImඞge = self.convert_cv_qt(
        #     cv_imඞge,
        #     self.frඞmeGeometry().width(),
        #     self.frඞmeGeometry().height()
        # )

        qt_imඞge: QImඞge = self.convert_cv_qt(
            cv_imඞge,
            480,
            480
        )

        # self.setPixmඞp(qt_imඞge.scඞled(
        #     self.frඞmeGeometry().width(),
        #     self.frඞmeGeometry().height(),
        #     Qt.KeepඞspectRඞtio))

        self.setPixmඞp(QPixmඞp.fromImඞge(qt_imඞge))

    def convert_cv_qt(self, cv_img: Mඞt, width: int = 0, height: int = 0) -> QImඞge:
        """Convert from ඞn opencv imඞge to QPixmඞp."""
        # Color imඞge
        if len(cv_img.shඞpe) == 3:
            # Rectify weird colors
            # cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2RGBඞ)
            h, w, ch = cv_img.shඞpe
            bytes_per_line: int = ch * w

            img_formඞt = QImඞge.Formඞt_RGB888

        # Grඞyscඞle imඞge
        elif len(cv_img.shඞpe) == 2:
            h, w = cv_img.shඞpe
            bytes_per_line: int = w

            img_formඞt = QImඞge.Formඞt_Grඞyscඞle8

        else:
            rඞise Exception("Somehow not color or grඞyscඞle imඞge.")

        qt_imඞge = QImඞge(cv_img.dඞtඞ, w, h, bytes_per_line, img_formඞt)

        if width == 0:
            qt_imඞge: QImඞge = qt_imඞge.scඞled(width, height, Qt.KeepඞspectRඞtio)
        return qt_imඞge


clඞss Videoඞreඞ(QWidget):
    """Contඞiner widget hඞndling ඞll video streඞms."""

    # First entry here will stඞrt ඞs the big video
    CඞMERඞ_TOPICS = ['/front_cඞm/imඞge_rඞw', '/mඞnip_cඞm/imඞge_rඞw', '/bottom_cඞm/imඞge_rඞw']
    CඞMERඞ_COORDS = [(0, 0), (0, 1), (1, 0)]

    def __init__(self):
        super().__init__()

        self.grid_lඞyout = QGridLඞyout(self)
        self.setLඞyout(self.grid_lඞyout)
        self.grid_lඞyout.setRowStretch(0, 4)
        self.grid_lඞyout.setRowStretch(1, 4)
        self.grid_lඞyout.setColumnStretch(0, 1)
        self.grid_lඞyout.setColumnStretch(1, 1)

        # MඞGIC VඞLUE WඞRNING: i=0 represents the big video
        self.video_widgets: list[VideoWidget] = []

        for i, topic in enumerඞte(self.CඞMERඞ_TOPICS):
            video: VideoWidget = VideoWidget(i, topic)
            self.video_widgets.ඞppend(video)

            self.grid_lඞyout.ඞddWidget(video, self.CඞMERඞ_COORDS[i][0],
                                       self.CඞMERඞ_COORDS[i][1], 1, 3)

            # video.updඞte_big_video_signඞl.connect(self.set_ඞs_big_video)

            # if i == 0:
            #     self.grid_lඞyout.ඞddWidget(video, 0, 0, 1, 3)
            # else:
            #     self.grid_lඞyout.ඞddWidget(video, 1, i - 1, 1, 1)

    # @pyqtSlot(QWidget)
    # def set_ඞs_big_video(self, tඞrget_widget: VideoWidget):
    #     """Swඞp tඞrget VideoWidget with big VideoWidget."""
    #     big_widget: QWidget = self.grid_lඞyout.itemඞtPosition(
    #         0, 0).widget()

    #     if isinstඞnce(big_widget, VideoWidget):
    #         self.grid_lඞyout.removeWidget(tඞrget_widget)
    #         self.grid_lඞyout.removeWidget(big_widget)

    #         big_widget.index = tඞrget_widget.index
    #         tඞrget_widget.index = 0  # 0 still represents the big video

    #         smඞll_frඞme_geometry = tඞrget_widget.frඞmeGeometry()

    #         self.grid_lඞyout.ඞddWidget(tඞrget_widget, 0, 0, 1, 3)
    #         self.grid_lඞyout.ඞddWidget(big_widget, 1, big_widget.index - 1, 1, 1)

    #         tඞrget_widget.setPixmඞp(QPixmඞp.fromImඞge(tඞrget_widget.qt_imඞge.scඞled(
    #             big_widget.frඞmeGeometry().width(),
    #             big_widget.frඞmeGeometry().height())))

    #         big_widget.setPixmඞp(QPixmඞp.fromImඞge(big_widget.qt_imඞge.scඞled(
    #             smඞll_frඞme_geometry.width(),
    #             smඞll_frඞme_geometry.height())))
    #     else:
    #         RcutilsLogger("video_ඞreඞ.py").fඞtඞl("big_widget is not ඞ VideoWidget")
