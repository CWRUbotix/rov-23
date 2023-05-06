from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QTabWidget, QWidget


from gui.modules.task_selector import TaskSelector
from gui.modules.logger import Logger
from gui.modules.buoy_frog_widget import BuoyFrogWidget
from gui.app import App


class OperatorApp(App):
    def __init__(self):
        super().__init__("operator_gui_node")

        self.setWindowTitle("Operator GUI - CWRUbotix ROV 2023")

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tab1: QWidget = QWidget()
        self.tab2: BuoyFrogWidget = BuoyFrogWidget()

        # Create first tab
        self.tab1Layout: QGridLayout = QGridLayout()

        self.logger: Logger = Logger()
        self.tab1Layout.addWidget(self.logger, 0, 0)

        self.task_selector: TaskSelector = TaskSelector()
        self.tab1Layout.addWidget(self.task_selector, 0, 1)

        self.tab1.setLayout(self.tab1Layout)

        # Add tabs
        self.tabs.addTab(self.tab1, "Task Selector")
        self.tabs.addTab(self.tab2, "Buoy/Frog Recorder")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


def run_gui_operator():
    OperatorApp().run_gui()
