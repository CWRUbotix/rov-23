from task_selector.tasks import Tasks

from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from gui.event_nodes.client import GUIEventClient
from gui.event_nodes.subscriber import GUIEventSubscriber

from interfaces.srv import TaskRequest
from interfaces.msg import TaskFeedback

from rclpy.impl.rcutils_logger import RcutilsLogger

WIDTH = 200


class TaskSelector(QWidget):
    """Qwidget that handles task selection with a dropdown."""

    # Declare signals with "object" params b/c we don't have access to
    # the ROS service object TaskRequest_Response
    scheduler_response_signal: pyqtSignal = pyqtSignal(TaskRequest.Response)
    update_task_dropdown_signal: pyqtSignal = pyqtSignal(TaskFeedback)

    def __init__(self):
        super().__init__()

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        # Create Start button
        self.start_btn = QPushButton("Auto Docking")
        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.start_btn.setFixedHeight(75)
        self.start_btn.setFixedWidth(WIDTH)

        # Create Stop button
        self.stop_btn = QPushButton("Manual Control")
        self.stop_btn.clicked.connect(self.manual_control_btn_clicked)
        self.stop_btn.setFixedHeight(75)
        self.stop_btn.setFixedWidth(WIDTH)

        # Add 'Task: ' label
        self.task_label: QLabel = QLabel()
        self.task_label.setFixedWidth(WIDTH)
        self.task_label.setText('Task: Manual Control')

        # Setup Grid
        layout.addWidget(self.task_label, 1, 1, 2, 2)
        layout.addWidget(self.start_btn, 2, 1)
        layout.addWidget(self.stop_btn, 3, 1)

        # Create ROS nodes #
        # Create client (in separate thread to let GUI load before it connects)
        self.scheduler_response_signal.connect(
            self.handle_scheduler_response)
        self.task_changed_client: GUIEventClient = GUIEventClient(
            TaskRequest, 'task_request', self.scheduler_response_signal)

        # Server doesn't spin, so we init in main thread
        self.update_task_dropdown_signal.connect(self.update_task_dropdown)
        self.task_changed_server: GUIEventSubscriber = GUIEventSubscriber(
            TaskFeedback, 'task_feedback', self.update_task_dropdown_signal)

    def start_btn_clicked(self):
        """Tell the back about the user selecting the start button."""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            return

        self.task_changed_client.get_logger().info(
            'GUI changed task to: Auto Docking')

        self.task_label.setText('Task: Auto Docking')

        self.task_changed_client.send_request_async(
            TaskRequest.Request(task_id=Tasks.AUTO_DOCKING.value))

    def manual_control_btn_clicked(self):
        """Tell the back about the user selecting the manual control button."""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            return

        self.task_changed_client.get_logger().info(
            'GUI changed task to: Manual Control')

        self.task_label.setText('Task: Manual Control')

        self.task_changed_client.send_request_async(
            TaskRequest.Request(task_id=Tasks.MANUAL_CONTROL.value))

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
