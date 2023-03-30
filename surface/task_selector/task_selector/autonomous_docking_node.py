import os
import rclpy
import time
import numpy as np
import cv2
from cv2 import VideoCapture
from rclpy.node import Node, Subscription, Publisher
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from cv_bridge import CvBridge

from interfaces.action import BasicTask
from interfaces.msg import ROVControl
from sensor_msgs.msg import Image
from ament_index_python.packages import get_package_share_directory


#TODO: Refine correctional parameters
#TODO: Ask what this means: Chop dual cam frame in half
# --------------------------------------------------------------------------------------------
# Direction robot should move while steering
RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"
NONE = "NONE"
# --------------------------------------------------------------------------------------------
# Fraction of screen the button takes up when we stop crawling & start steering
START_WIDTH_FRACTION = 0.035
START_HEIGHT_FRACTION = 0.035
# --------------------------------------------------------------------------------------------
# Theoretical task durations
MAX_TASK_DURATION = 500
MIN_TASK_DURATION = 2
# ---------------------------------------------------------------------------------------------
# Ratio of the camera frame's dimenions to dimensions of the square we want the button to be in
# Currently 10 to 1
BP = 0.1
# --------------------------------------------------------------------------------------------


class AutonomousDockingControlNode(Node):

    # ??
    handle_frame_signal = pyqtSignal(Image)

    def __init__(self):
        super().__init__('autonomous_docking_node',
                         parameter_overrides=[])
        self._action_server = ActionServer(
            self, 
            BasicTask,
            'autonomous_docking',
            self.execute_callback
        )
        
        # Object to bridge ROV Images and CV2 Images
        self.cv_bridge: CvBridge = CvBridge()
        self.handle_frame_signal.connect(self.handle_frame)

        # Camera Subscription
        # Subscription or GUIEventSubscriber
        self.camera_subscriber: Subscription = self.create_subscription(
            Image,
            # Unsure what the topic name should be, i.e which camera
            # self.image_topic_name,
            self.handle_frame,
            10
        )

        # TODO: Create/Refine ROV Control system for movement regarding the Pixhawk
        # Pixhawk Publisher - Broadcasts directional commands
        self.pixhawk_publisher: Publisher = self.create_publisher(
            ROVControl,
            'pixhawk_autonomous_control',
            10                  
        )

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image = self.cv_bridge.imgmsg_to_cv2(frame, desired_encoding='CV_8UC4')  # Converts image msg to BGR w/ alpha channel
   
        rov_msg = ROVControl()
        rov_msg.header = msg.header
        # Directional commands for the ROV
        rov_msg.x = None
        rov_msg.y = None
        rov_msg.z = None
        # Rotational directions for the ROV
        rov_msg.yaw = None
        rov_msg.pitch = None
        rov_msg.roll = None
        self.pixhawk_publisher.publish(rov_msg)


    def execute_callback(self, goal_handle: ServerGoalHandle) -> BasicTask.Result:
        self.get_logger().info('Starting Autonomous Docking...')

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
            self.get_logger().info('Docking canceled')
            return BasicTask.Result()
        else:
            feedback_msg = BasicTask.Feedback()
            feedback_msg.feedback_message = "Task is executing"

            self.get_logger().info('Feedback: ' + feedback_msg.feedback_message)

            goal_handle.publish_feedback(feedback_msg)
            goal_handle.succeed()
            return BasicTask.Result()

    # Can I remove goal_handle as a parameter?
    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()
    docking_control = AutonomousDockingControlNode()
    executor = MultiThreadedExecutor()
    # Do I need to spin this node?
    rclpy.spin(docking_control, executor=executor)
