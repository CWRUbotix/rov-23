from PyQt5.QtWidgets import QGridLayout


from gui.modules.task_selector import TaskSelector
from gui.modules.logger import Logger
from gui.app import App, run_gui


class OperatorApp(App):
    def __init__(self):
        super().__init__('operator_gui_node')

        self.setWindowTitle('Operator GUI - CWRUbotix ROV 2023')

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.task_selector: TaskSelector = TaskSelector()
        layout.addWidget(self.task_selector, 0, 1)
        self.modules.append(self.task_selector)

        self.logger: Logger = Logger()
        layout.addWidget(self.logger, 0, 0)
        self.modules.append(self.logger)


def run_gui_operator():
    run_gui(OperatorApp)
