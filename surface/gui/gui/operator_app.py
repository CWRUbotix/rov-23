from PyQt5.QtWidgets import QGridLayout, QTabWidget, QWidget, QHBoxLayout


from gui.modules.task_selector import TaskSelector
from gui.modules.logger import Logger
from gui.modules.seagrass import SeagrassWidget
from gui.app import App


class OperatorApp(App):
    def __init__(self):
        super().__init__('operator_gui_node')

        self.setWindowTitle('Operator GUI - CWRUbotix ROV 2023')

        tabs = QTabWidget()
        
        # Main tab
        main_tab = QWidget()
        main_layout: QGridLayout = QGridLayout()
        main_tab.setLayout(main_layout)

        self.task_selector: TaskSelector = TaskSelector()
        main_layout.addWidget(self.task_selector, 0, 1)

        # Seagrass tab
        seagrass_tab = QWidget()
        seagrass_tab.setContentsMargins(0, 0, 0, 0)

        seagrass_layout: QHBoxLayout = QHBoxLayout()

        seagrass_tab.setLayout(seagrass_layout)
        seagrass_layout.addWidget(SeagrassWidget())

        # Add tabs to root
        root_layout: QGridLayout = QGridLayout()
        self.setLayout(root_layout)

        tabs.addTab(main_tab, "Main")
        tabs.addTab(seagrass_tab, "Seagrass")

        root_layout.addWidget(tabs)

        self.logger: Logger = Logger()
        main_layout.addWidget(self.logger, 0, 0)


def run_gui_operator():
    OperatorApp().run_gui()
