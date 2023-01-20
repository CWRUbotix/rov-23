import rclpy

from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from event_nodes.client import GUIEventClient
from event_nodes.server import GUIEventServer
from interfaces.srv import TaskRequest


class TaskSelector(QWidget):
    """Module widget that handles task selection with a dropdown."""
    # Declare signals with "object" params b/c we don't have access to
    # the ROS service object TaskRequest_Response
    handle_scheduler_response_signal: pyqtSignal = pyqtSignal(object)
    update_task_dropdown_signal: pyqtSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        rclpy.init()  # We'll need to create ROS nodes

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        # Add 'Task: ' label #
        label: QLabel = QLabel()
        label.setText('Task: ')
        layout.addWidget(label)

        # Add dropdown #
        # Create PyQt element
        self.combo_box: QComboBox = QComboBox()
        self.combo_box.addItem('Manual Control')
        self.combo_box.addItem('Auto Docking')
        self.combo_box.addItem('Coral Modeling')
        layout.addWidget(self.combo_box)

        # Connect signals
        self.combo_box.currentIndexChanged.connect(self.gui_changed_task)

        # Creat ROS nodes #
        # Create client (in seperate thread to let GUI load before it connects)
        self.handle_scheduler_response_signal.connect(
            self.handle_scheduler_response)
        self.task_changed_client: GUIEventClient = GUIEventClient(
            TaskRequest, 'task_changed_by_gui', self.handle_scheduler_response_signal)

        # Server doesn't spin, so we init in main thread
        self.update_task_dropdown_signal.connect(self.update_task_dropdown)
        self.task_changed_server: GUIEventServer = GUIEventServer(
            TaskRequest, 'task_changed_by_scheduler', self.scheduler_changed_task)

        self.task_changed_server.spin_async()

    def gui_changed_task(self, i: int):
        """Tell the back about the user selecting task with ID i."""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            self.combo_box.setCurrentIndex(0)
            return

        print(
            f'Task changed to: {self.combo_box.currentText()} at {self.combo_box.currentIndex()}')

        self.task_changed_client.send_request_async({'task_id': i})

    @pyqtSlot(int)
    def update_task_dropdown(self, task_id: int):
        print('update dropdown')
        self.combo_box.setCurrentIndex(task_id)

    def scheduler_changed_task(self, request, response):
        """Responds when task scheduler changes the task."""
        print(request)
        print(response)
        print('manager changed callback')
        response.response = 'Accepted'
        self.update_task_dropdown_signal.emit(request.task_id)
        return response

    @pyqtSlot(object)
    def handle_scheduler_response(self, response):
        print(response)
