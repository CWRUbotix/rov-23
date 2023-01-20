from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel

import rclpy

from event_nodes.client import GUIEventClient
from event_nodes.server import GUIEventServer
from interfaces.srv import TaskRequest


class TaskSelector(QWidget):
    """Module widget that handles task selection with a dropdown"""

    def __init__(self):
        super().__init__()
        rclpy.init()  # We'll need to create ROS nodes

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        ## Add 'Task: ' label ##
        label: QLabel = QLabel()
        label.setText('Task: ')
        layout.addWidget(label)

        ## Add dropdown ##
        # Create PyQt element
        self.combo_box: QComboBox = QComboBox()
        self.combo_box.addItem('Manual Control')
        self.combo_box.addItem('Auto Docking')
        self.combo_box.addItem('Coral Modeling')
        layout.addWidget(self.combo_box)

        # Connect signals
        self.combo_box.currentIndexChanged.connect(self.gui_changed_task)

        ## Creat ROS nodes ##
        # Create client (in seperate thread to let GUI load before it connects)
        self.task_changed_client: GUIEventClient = GUIEventClient(
            TaskRequest, 'task_changed_by_gui')

        # Server doesn't spin, so we init in main thread
        self.task_changed_server: GUIEventServer = GUIEventServer(
            TaskRequest, 'task_changed_by_scheduler', self.scheduler_changed_task)

        self.task_changed_server.spin_async()

    def gui_changed_task(self, i: int):
        """Tell the back about the user selecting task with ID i"""

        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            self.combo_box.setCurrentIndex(0)
            return

        print(
            f'Task changed to: {self.combo_box.currentText()} at {self.combo_box.currentIndex()}')

        response = self.task_changed_client.send_request_async(
            {'task_id': i}, self.handle_scheduler_response)

    def scheduler_changed_task(self, request, response):
        """Callback for when the task manager changed the task"""
        print('manager changed callback')
        self.combo_box.setCurrentIndex(request.task_id)
        response.response = 'Accepted'
        return response

    def handle_scheduler_response(self, response):
        print(response)
