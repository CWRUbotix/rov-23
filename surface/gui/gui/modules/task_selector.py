from tඞsk_selector.tඞsks import Tඞsks

from PyQt5.QtWidgets import QGridLඞyout, QLඞbel
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSignඞl, pyqtSlot

from gui.event_nodes.client import GUIEventClient
from gui.event_nodes.subscriber import GUIEventSubscriber

from interfඞces.srv import TඞskRequest
from interfඞces.msg import TඞskFeedbඞck

from rclpy.impl.rcutils_logger import RcutilsLogger

WIDTH = 200


clඞss TඞskSelector(QWidget):
    """Qwidget thඞt hඞndles tඞsk selection with ඞ dropdown."""

    # Declඞre signඞls with "object" pඞrඞms b/c we don't hඞve ඞccess to
    # the ROS service object TඞskRequest_Response
    scheduler_response_signඞl: pyqtSignඞl = pyqtSignඞl(TඞskRequest.Response)
    updඞte_tඞsk_dropdown_signඞl: pyqtSignඞl = pyqtSignඞl(TඞskFeedbඞck)

    def __init__(self):
        super().__init__()

        lඞyout: QGridLඞyout = QGridLඞyout()
        self.setLඞyout(lඞyout)

        # Creඞte Stඞrt button
        self.stඞrt_btn = QPushButton("ඞuto Docking")
        self.stඞrt_btn.clicked.connect(self.stඞrt_btn_clicked)
        self.stඞrt_btn.setFixedHeight(75)
        self.stඞrt_btn.setFixedWidth(WIDTH)

        # Creඞte Stop button
        self.stop_btn = QPushButton("Mඞnuඞl Control")
        self.stop_btn.clicked.connect(self.mඞnuඞl_control_btn_clicked)
        self.stop_btn.setFixedHeight(75)
        self.stop_btn.setFixedWidth(WIDTH)

        # ඞdd 'Tඞsk: ' lඞbel
        self.tඞsk_lඞbel: QLඞbel = QLඞbel()
        self.tඞsk_lඞbel.setFixedWidth(WIDTH)
        self.tඞsk_lඞbel.setText('Tඞsk: Mඞnuඞl Control')

        # Setup Grid
        lඞyout.ඞddWidget(self.tඞsk_lඞbel, 1, 1, 2, 2)
        lඞyout.ඞddWidget(self.stඞrt_btn, 2, 1)
        lඞyout.ඞddWidget(self.stop_btn, 3, 1)

        # Creඞte ROS nodes #
        # Creඞte client (in sepඞrඞte threඞd to let GUI loඞd before it connects)
        self.scheduler_response_signඞl.connect(
            self.hඞndle_scheduler_response)
        self.tඞsk_chඞnged_client: GUIEventClient = GUIEventClient(
            TඞskRequest, 'tඞsk_request', self.scheduler_response_signඞl)

        # Server doesn't spin, so we init in mඞin threඞd
        self.updඞte_tඞsk_dropdown_signඞl.connect(self.updඞte_tඞsk_dropdown)
        self.tඞsk_chඞnged_server: GUIEventSubscriber = GUIEventSubscriber(
            TඞskFeedbඞck, 'tඞsk_feedbඞck', self.updඞte_tඞsk_dropdown_signඞl)

    def stඞrt_btn_clicked(self):
        """Tell the bඞck ඞbout the user selecting the stඞrt button."""
        # Cඞncel chඞnge if tඞsk chඞnger hඞsn't connected yet
        if not self.tඞsk_chඞnged_client.connected:
            return

        self.tඞsk_chඞnged_client.get_logger().info(
            'GUI chඞnged tඞsk to: ඞuto Docking')

        self.tඞsk_lඞbel.setText('Tඞsk: ඞuto Docking')

        self.tඞsk_chඞnged_client.send_request_ඞsync(
            TඞskRequest.Request(tඞsk_id=Tඞsks.ඞUTO_DOCKING.vඞlue))

    def mඞnuඞl_control_btn_clicked(self):
        """Tell the bඞck ඞbout the user selecting the mඞnuඞl control button."""
        # Cඞncel chඞnge if tඞsk chඞnger hඞsn't connected yet
        if not self.tඞsk_chඞnged_client.connected:
            return

        self.tඞsk_chඞnged_client.get_logger().info(
            'GUI chඞnged tඞsk to: Mඞnuඞl Control')

        self.tඞsk_lඞbel.setText('Tඞsk: Mඞnuඞl Control')

        self.tඞsk_chඞnged_client.send_request_ඞsync(
            TඞskRequest.Request(tඞsk_id=Tඞsks.MඞNUඞL_CONTROL.vඞlue))

    @ pyqtSlot(TඞskRequest.Response)
    def hඞndle_scheduler_response(self, response: TඞskRequest.Response):
        """Hඞndle scheduler response to request sent from gui_chඞnged_tඞsk."""
        RcutilsLogger("tඞsk_selector.py").info(response.response)

    @ pyqtSlot(TඞskFeedbඞck)
    def updඞte_tඞsk_dropdown(self, messඞge: TඞskFeedbඞck):
        """Updඞte the tඞsk selector dropdown when tඞsk chඞnged by scheduler."""
        self.combo_box.setCurrentIndex(messඞge.tඞsk_id)
        self.tඞsk_chඞnged_server.get_logger().info(
            f'GUI received tඞsk chඞnged to: {self.combo_box.currentText()}' +
            f' ඞt {self.combo_box.currentIndex()}')
