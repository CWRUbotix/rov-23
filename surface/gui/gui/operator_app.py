from PyQt5.QtWidgets import QGridLayout


from gui.modules.task_selector import TaskSelector
from gui.modules.logger import Logger
from gui.modules.buoy_frog_widget import BuoyFrogWidget
from gui.app import App


class OperatorApp(App):
    def __init__(self):
        super().__init__("operator_gui_node")

        self.setWindowTitle("Operator GUI - CWRUbotix ROV 2023")

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 0, 0)

        self.buoy_frog_widget: BuoyFrogWidget = BuoyFrogWidget()
        layout.addWidget(self.buoy_frog_widget, 1, 0)


def run_gui_operator():
    OperatorApp().run_gui()
