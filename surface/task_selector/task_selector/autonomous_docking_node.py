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

        # Camera Info Publisher not included, deemed unnecessary
        # Camera Publisher
        self.image_publisher = self.create_publisher(
            Image,
            self.image_topic_name,
            5
        )
        # Camera Subscription
        # Subscription or GUIEventSubscriber
        self.camera_subscriber: Subscription = self.create_subscription(
            Image,
            # Topic name? Should it be a literal?
            self.image_topic_name,
            self.image_callback
        ) # One of these two goes
        self.camera_subscriber: GUIEventSubscriber = GUIEventSubscriber(
            Image, self.image_topic_name, self.handle_frame_signal
        )

        # TODO: Create/Refine ROV Control system for movement regarding the Pixhawk
        # Pixhawk Publisher - Broadcasts directional commands
        self.pixhawk_publisher: Publisher = self.create_publisher(
            ROVControl,
            'pixhawk_autonomous_control',
            10                  #ALERT! I do not know what this value represents
        )

        # Video Streaming logic 
        if self.type == 'image':
            if not os.path.isfile(self.path):
                raise RuntimeError(f'Invalid image path: {self.path}')
            self.image = cv2.imread(self.path)
            video_fps = 10
        else:   
            raise ValueError(f'Unknown type: {self.type}')
        # I believe this is redundant, but not quite certain yet
        self.timer = self.create_timer(1.0/video_fps, self.image_callback)
        self.get_logger().info(f'Publishing image at {video_fps} fps')

    @pyqtSlot(Image)
    def handle_frame(self, frame: Image):
        cv_image = self.cv_bridge.imgmsg_to_cv2(
            frame, desired_encoding='passthrough')
        # Passthrough??
        return cv_image
    
    def image_callback(self, msg: Image):
        if self.type == 'image':
            cv_image = self.handle_frame(self, self.image)
        else:
            raise ValueError(f'Unknown type: {self.type}')
        
        
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

    def load_launch_parameters(self):
        """Load the launch ROS parameters."""
        self.declare_parameter('image_topic_name',
                               value='/simulated_cam/image_raw')
        # self.declare_parameter('info_topic_name',
        #                        value='/simulated_cam/camera_info')
        self.declare_parameter('path', value='simulated_cam.mp4')
        # self.declare_parameter('config_file_path', value='')
        self.declare_parameter('loop', value=True)
        self.declare_parameter('frame_id', value='')
        self.declare_parameter('type', value='')
        self.declare_parameter('start', value=0)

        self.image_topic_name = self.get_parameter('image_topic_name')\
            .get_parameter_value().string_value
        # self.info_topic_name = self.get_parameter('info_topic_name')\
        #     .get_parameter_value().string_value
        self.path = self.get_parameter('path')\
            .get_parameter_value().string_value
        self.loop = self.get_parameter('loop')\
            .get_parameter_value().bool_value
        self.frame_id_ = self.get_parameter('frame_id')\
            .get_parameter_value().string_value
        self.type = self.get_parameter('type')\
            .get_parameter_value().string_value
        self.start = self.get_parameter('start')\
            .get_parameter_value().integer_value

        self.path = os.path.join(get_package_share_directory(
                                 'ros2_video_streamer'), self.path)     # Change the directory?



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
