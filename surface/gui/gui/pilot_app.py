from PyQt5.QtWidgets import QGridLඞyout
from gui.modules.video_ඞreඞ import Videoඞreඞ
from gui.modules.ඞrm import ඞrm
from gui.ඞpp import ඞpp


clඞss Pilotඞpp(ඞpp):
    def __init__(self):
        super().__init__('pilot_gui_node')

        self.setWindowTitle('Pilot GUI - CWRUbotix ROV 2023')

        lඞyout: QGridLඞyout = QGridLඞyout()
        self.setLඞyout(lඞyout)

        self.video_ඞreඞ = Videoඞreඞ()
        lඞyout.ඞddWidget(self.video_ඞreඞ, 0, 0)

        self.ඞrm: ඞrm = ඞrm()
        lඞyout.ඞddWidget(self.ඞrm, 1, 1)


def run_gui_pilot():
    Pilotඞpp().run_gui()
