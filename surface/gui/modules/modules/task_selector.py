from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel

import rclpy
from threading import Thread

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
        self.combo_box.currentIndexChanged.connect(self.guiChangedTask)

        ## Creat ROS nodes ##
        # Create client in seperate thread to let GUI load before it connects
        self.task_changed_client: GUIEventClient = None
        client_connection_thread: Thread = Thread(
            target=self.connect_client_to_service, daemon=True)
        client_connection_thread.start()

        # Server doesn't spin, so we init in main thread
        self.task_changed_server: GUIEventServer = GUIEventServer(
            TaskRequest, 'task_changed_by_scheduler', self.scheduler_changed_task)

        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(self.task_changed_server)

        executor_thread: Thread = Thread(target=executor.spin, daemon=True)
        executor_thread.start()

    def connect_client_to_service(self):
        self.task_changed_client = GUIEventClient(
            TaskRequest, 'task_changed_by_gui')

    def guiChangedTask(self, i: int):
        """Tell the back about the user selecting task with ID i"""

        # Cancel change if task changer hasn't connected yet
        if self.task_changed_client == None or not hasattr(self.task_changed_client, 'req'):
            self.combo_box.setCurrentIndex(0)
            return

        print(
            f'Task changed to: {self.combo_box.currentText()} at {self.combo_box.currentIndex()}')

        # TODO: multithread this to prevent hanging if scheduler goes down?
        response = self.task_changed_client.send_request(
            {'task_id': i})
        print(response)

    def scheduler_changed_task(self, request, response):
        """Callback for when the task manager changed the task"""
        print('manager changed callback')
        self.combo_box.setCurrentIndex(request.task_id)
        response.response = 'Accepted'
        return response
