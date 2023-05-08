from PyQt5.QtWidgets import QGridLayout, QTabWidget, QWidget

from gui.modules.task_selector import TaskSelector
from gui.modules.logger import Logger
from gui.modules.seagrass import SeagrassWidget
from gui.modules.buoy_frog_widget import BuoyFrogWidget
from gui.modules.timer import Timer
from gui.app import App


class OperatorApp(App):
    def __init__(self):
        super().__init__("operator_gui_node")

        self.setWindowTitle("Operator GUI - CWRUbotix ROV 2023")

        tabs = QTabWidget()

        # Main tab
        main_tab = QWidget()
        main_layout: QGridLayout = QGridLayout()
        main_tab.setLayout(main_layout)

        self.timer: Timer = Timer()
        main_layout.addWidget(self.timer, 0, 1)

        self.task_selector: TaskSelector = TaskSelector()
        main_layout.addWidget(self.task_selector, 1, 1)

        self.logger: Logger = Logger()
        main_layout.addWidget(self.logger, 1, 0)

        # Add tabs to root
        root_layout: QGridLayout = QGridLayout()
        self.setLayout(root_layout)

        tabs.addTab(main_tab, "Main")
        tabs.addTab(SeagrassWidget(), "Seagrass")
        tabs.addTab(BuoyFrogWidget(), "Buoy/Frog Recorder")

        root_layout.addWidget(tabs)


def run_gui_operator():
    OperatorApp().run_gui()
