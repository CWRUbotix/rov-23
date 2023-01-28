from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import rclpy

from event_nodes.client import GUIEventClient
from event_nodes.subscriber import GUIEventSubscriber
from interfaces.srv import TaskRequest
from interfaces.msg import TaskFeedback
from modules.module import Module


class TaskSelector(Module):
    """Module widget that handles task selection with a dropdown."""

    # Declare signals with "object" params b/c we don't have access to
    # the ROS service object TaskRequest_Response
    handle_scheduler_response_signal: pyqtSignal = pyqtSignal(object)
    update_task_dropdown_signal: pyqtSignal = pyqtSignal(object)

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
            TaskRequest, 'task_request', self.handle_scheduler_response_signal)

        # Server doesn't spin, so we init in main thread
        self.update_task_dropdown_signal.connect(self.update_task_dropdown)
        self.task_changed_server: GUIEventSubscriber = GUIEventSubscriber(
            TaskFeedback, 'task_feedback', self.update_task_dropdown_signal)

        self.task_changed_server.spin_async()

    def gui_changed_task(self, i: int):
        """Tell the back about the user selecting task with ID i."""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            self.combo_box.setCurrentIndex(0)
            return

        self.task_changed_client.get_logger().info(
            f'GUI changed task to: {self.combo_box.currentText()}' +
            f' at {self.combo_box.currentIndex()}')

        self.task_changed_client.send_request_async({'task_id': i})

    @ pyqtSlot(object)
    def handle_scheduler_response(self, response):
        """Handle scheduler response to request sent from gui_changed_task."""
        print(response)

    @ pyqtSlot(object)
    def update_task_dropdown(self, message):
        """Update the task selector dropdown when task changed by scheduler."""
        self.combo_box.setCurrentIndex(message.task_id)
        self.task_changed_server.get_logger().info(
            f'GUI recieved task changed to: {self.combo_box.currentText()}' +
            f' at {self.combo_box.currentIndex()}')

    def kill_all_executors(self):
        self.task_changed_server.kill_executor()
