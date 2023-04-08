from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from gui.event_nodes.client import GUIEventClient
from gui.event_nodes.subscriber import GUIEventSubscriber

from interfaces.srv import TaskRequest
from interfaces.msg import TaskFeedback

from rclpy.impl.rcutils_logger import RcutilsLogger

width = 200


class TaskSelector(QWidget):
    """Qwidget that handles task selection with a dropdown."""

    # Declare signals with "object" params b/c we don't have access to
    # the ROS service object TaskRequest_Response
    handle_scheduler_response_signal: pyqtSignal = pyqtSignal(TaskRequest.Response)
    update_task_dropdown_signal: pyqtSignal = pyqtSignal(TaskFeedback)

    def __init__(self):
        super().__init__()

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        # Create Start button
        self.startBtn = QPushButton("Start Auto Docking")
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.startBtn.setFixedHeight(75)
        self.startBtn.setFixedWidth(width)


        # Create Stop button
        self.stopBtn = QPushButton("Stop Auto Docking")
        self.stopBtn.clicked.connect(self.stopBtnClicked)
        self.stopBtn.setFixedHeight(75)
        self.stopBtn.setFixedWidth(width)
       
        # Add 'Task: ' label
        self.label: QLabel = QLabel()
        self.label.setFixedWidth(width)
        self.label.setText('Task: Manual Control')
        
        # Setup Grid
        layout.addWidget(self.label, 1, 1, 2, 2)
        layout.addWidget(self.startBtn, 2, 1)
        layout.addWidget(self.stopBtn, 3, 1)


        

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

    def startBtnClicked(self):
        """Tell the back about the user selecting the start button."""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            return
        
        self.task_changed_client.get_logger().info(
            f'GUI changed task to: Auto Docking')

        self.label.setText('Task: Auto Docking')

        self.task_changed_client.send_request_async(TaskRequest.Request(task_id=1))

    def stopBtnClicked(self):
        """Tell the back about the user selecting the stop button"""
        # Cancel change if task changer hasn't connected yet
        if not self.task_changed_client.connected:
            return

        self.task_changed_client.get_logger().info(
            f'GUI changed task to: Manual Control')

        self.label.setText('Task: Manual Control')

        self.task_changed_client.send_request_async(TaskRequest.Request(task_id=0))
        
        
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
