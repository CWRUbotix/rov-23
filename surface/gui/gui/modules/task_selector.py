from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from gui.event_nodes.client import GUIEventClient
from gui.event_nodes.subscriber import GUIEventSubscriber

from rov_interfaces.srv import TaskRequest
from rov_interfaces.msg import TaskFeedback
from gui.modules.module import Module

from rclpy.impl.rcutils_logger import RcutilsLogger


class TaskSelector(Module):
    """Module widget that handles task selection with a dropdown."""

    # Declare signals with "object" params b/c we don't have access to
    # the ROS service object TaskRequest_Response
    handle_scheduler_response_signal: pyqtSignal = pyqtSignal(TaskRequest.Response)
    update_task_dropdown_signal: pyqtSignal = pyqtSignal(TaskFeedback)

    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        self.setLayout(layout)

        # Add 'Task: ' label #
        label: QLabel = QLabel()
        label.setText('Task: ')
        layout.addWidget(label)

        # Add dropdown #
        # Create PyQt element
        self.combo_box: QComboBox = QComboBox()
        self.combo_box.setMinimumWidth(150)
        self.combo_box.addItem('Manual Control')
        self.combo_box.addItem('Auto Docking')
        self.combo_box.addItem('Coral Modeling')
        layout.addWidget(self.combo_box)

        # Connect signals
        self.combo_box.currentIndexChanged.connect(self.gui_changed_task)

        # Create ROS nodes #
        # Create client (in separate thread to let GUI load before it connects)
        self.handle_scheduler_response_signal.connect(
            self.handle_scheduler_response)
        self.task_changed_client: GUIEventClient = GUIEventClient(
            TaskRequest, 'task_request', self.handle_scheduler_response_signal)

        # Server doesn't spin, so we init in main thread
        self.update_task_dropdown_signal.connect(self.update_task_dropdown)
        self.task_changed_server: GUIEventSubscriber = GUIEventSubscriber(
            TaskFeedback, 'task_feedback', self.update_task_dropdown_signal)

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

    @ pyqtSlot(TaskRequest.Response)
    def handle_scheduler_response(self, response: TaskRequest.Response):
        """Handle scheduler response to request sent from gui_changed_task."""
        RcutilsLogger("task_selector.py").info(response.response)

    @ pyqtSlot(TaskFeedback)
    def update_task_dropdown(self, message: TaskFeedback):
        """Update the task selector dropdown when task changed by scheduler."""
        self.combo_box.setCurrentIndex(message.task_id)
        self.task_changed_server.get_logger().info(
            f'GUI received task changed to: {self.combo_box.currentText()}' +
            f' at {self.combo_box.currentIndex()}')

    def kill_all_executors(self):
        self.task_changed_server.kill_executor()
