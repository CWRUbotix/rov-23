from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel

import rclpy
import threading

from event_nodes.client import GUIEventClient
from event_nodes.server import GUIEventServer
from interfaces.srv import TaskRequest


class TaskSelector(QWidget):
    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()

        ## Add 'Task: ' label ##
        label: QLabel = QLabel()
        label.setText('Task: ')
        layout.addWidget(label)

        ## Add dropdown ##
        # Create PyQt element
        self.comboBox: QComboBox = QComboBox()
        self.comboBox.addItem('Manual Control')
        self.comboBox.addItem('Auto Docking')
        self.comboBox.addItem('Coral Modeling')
        layout.addWidget(self.comboBox)

        # Connect signals
        self.comboBox.currentIndexChanged.connect(self.guiChangedTask)

        self.setLayout(layout)

        rclpy.init()

        self.taskChangedClient = GUIEventClient(
            TaskRequest, 'task_changed_by_gui')
        self.taskChangedServer = GUIEventServer(
            TaskRequest, 'task_changed_by_manager', self.managerChangedTask)

        executor = rclpy.executors.MultiThreadedExecutor()
        executor.add_node(self.taskChangedServer)

        executor_thread = threading.Thread(target=executor.spin, daemon=True)
        executor_thread.start()

    def guiChangedTask(self, i: int):
        print(
            f'Task changed to: {self.comboBox.currentText()} at {self.comboBox.currentIndex()}')
        response = self.taskChangedClient.send_request(
            {'task_id': i})
        print(response)

    def managerChangedTask(self, request, response):
        print('manager changed callback')
        self.comboBox.setCurrentIndex(request.task_id)
        response.response = 'Accepted'
        return response
