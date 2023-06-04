import rclpy
import numpy as np
import cv2
from rclpy.node import Node, Subscription, Publisher
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from interfaces.action import BasicTask
from interfaces.msg import ROVControl

# TODO: Refine correctional parameters
# TODO: Ask what this means: Chop dual cam frame in half
# --------------------------------------------------------------------------------------------
# Direction robot should move while steering
RIGHT = -1
LEFT = 1
UP = 1
DOWN = -1
NONE = 0
# --------------------------------------------------------------------------------------------
# Fraction of screen the button takes up when we stop crawling & start steering
START_WIDTH_FRACTION = 0.035
START_HEIGHT_FRACTION = 0.035
# ---------------------------------------------------------------------------------------------
# Represents size of the square the button should be in relative to height of the image
BOUND = 0.05
# Range of values Pixhawk takes in microseconds
ZERO_SPEED: int = 1500
RANGE_SPEED: int = 400
# The speed at which we adjust the ROV
CRAWL_RATE = 0.25
# The speed of which we hit the button
CHARGE_RATE = 0.5
# --------------------------------------------------------------------------------------------


class AutonomousDockingNode(Node):
    # Ideally the ROV should be level the the ground, but it should be fine either way
    def __init__(self):
        super().__init__('autonomous_docking_node',
                         parameter_overrides=[],
                         namespace='surface')
        self._action_server = ActionServer(
            self,
            BasicTask,
            'autonomous_docking',
            self.execute_callback
        )

        # Remove PyQt image retrieval
        # Object to bridge ROV Images and CV2 Images
        self.cv_bridge: CvBridge = CvBridge()
        # self.handle_frame_signal.connect(self.handle_frame)
        # Initial Image dimensions given no images have been received
        self.image_dims = (-1, -1)
        # Represents if the ROV is at a standstill
        self.stopped = False
        self.button_found = False
        self.logging = 0
        # Camera Subscription
        # Subscription or GUIEventSubscriber
        self.camera_subscriber: Subscription = self.create_subscription(
            Image,
            # Unsure what the topic name should be, i.e which camera
            '/front_cam/image_raw',
            # May not need to interface with camera using PyQt GUI module
            self.handle_frame,
            10
        )

        # TODO: Create/Refine ROV Control system for movement regarding the Pixhawk
        # Pixhawk Publisher - Broadcasts directional commands
        self.auto_docking_pub: Publisher = self.create_publisher(
            ROVControl,
            'autonomous_docking',
            10
        )

    def handle_frame(self, frame: Image):
        # Converts image msg to BGR w/ alpha channel
        cv_image = self.cv_bridge.imgmsg_to_cv2(frame, desired_encoding='passthrough')
        horizontal_direction, vertical_direction = self.move_direction(cv_image)

        rov_msg = ROVControl()

        if self.stopped:
            if self.logging == 2:
                self.get_logger().info('Charging Towards Button')
                self.logging += 1
            rov_msg.x = ZERO_SPEED + int(RANGE_SPEED * CHARGE_RATE)
            # Continues slight adjustments as ROV moves forward
            rov_msg.y = ZERO_SPEED + horizontal_direction * int(RANGE_SPEED * CRAWL_RATE)
            rov_msg.z = ZERO_SPEED + vertical_direction * int(RANGE_SPEED * CRAWL_RATE)
        
        elif horizontal_direction != 0 or vertical_direction != 0:
            if self.logging == 0:
                self.get_logger().info('Aligning ROV')
                self.logging += 1
            # TODO: Should I made a header? If so, to what?
            # rov_msg.header = header
            # Directional commands for the ROV
            # TODO: Double check x y z axes are right
            rov_msg.y = ZERO_SPEED + horizontal_direction * int(RANGE_SPEED * CRAWL_RATE)
            rov_msg.z = ZERO_SPEED + vertical_direction * int(RANGE_SPEED * CRAWL_RATE)
            
        elif self.button_found:
            if self.logging == 1:
                self.get_logger().info('Stopping ROV')
                self.logging += 1
            # Currently no delay
            self.stopped = True
        self.auto_docking_pub.publish(rov_msg)

    # Takes a OpenCV image as input and returns a contour surrounding the button
    def get_button_contour(self, cv_img):
        # Constant value to offset CV binary threshhold
        c = 0

        # Use LAB colorspace to segment/enhance red in the original image
        Lab = cv2.cvtColor(cv_img, cv2.COLOR_RGB2LAB)
        L, A, B = cv2.split(Lab)

        # Takes the A-channel, grayscale representing the red and green in the image
        gray = cv2.GaussianBlur(A, (7, 7), 0)    # Blurs the image to smooth the edges
        img_h, img_w = gray.shape                   # Calling this on the BGR will get (x, y, 3)

        # Threshold it, getting a bitmap
        gaussian = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            21,
            c
        )

        # The HSV colormap of the original image, but with the gaussian threshold mask applied
        gausMaskedHSV = cv2.cvtColor(cv2.bitwise_and(cv_img, cv_img, mask=gaussian), 
                                     cv2.COLOR_RGB2HSV)

        # Lower mask (0-10 red range of color)
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(gausMaskedHSV, lower_red, upper_red)

        # upper mask (170-180 red range of color)
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(gausMaskedHSV, lower_red, upper_red)
        # The final mask of the lower red and upper red combined
        finalMasked2 = mask0 + mask1

        # TODO: Add morphological CLOSE and OPEN?

        # Find the largest contour
        gaussContours, _ = cv2.findContours(finalMasked2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        currentArea = 0
        gauss_contour = None
        for contour in gaussContours:
            x, y, w, h = cv2.boundingRect(contour)
            if w < img_w and h < img_h and w * h > currentArea:
                currentArea = w * h
                gauss_contour = contour

        # Find the center of the circle enclosing the button

        return gauss_contour, currentArea

    def move_direction(self, image):
        contour, area = self.get_button_contour(image)
        # Indicators for what directions we should be moving
        horizontal_move = NONE
        vertical_move = NONE

        # Gets the coordinates for the button's position and image dimensions
        # Once a contour has been found
        if area > 0:
            if not self.button_found:
                self.get_logger().info('Found button')
            self.button_found = True
            (button_x, button_y), radius = cv2.minEnclosingCircle(contour)
            self.image_dims = image.shape  # (y, x)

            # Takes the dimensions of the image
            # And then determines if the button is close to the center
            if (self.image_dims[1] / 2 + BOUND * self.image_dims[1]) < button_x:
                horizontal_move = RIGHT
            elif (self.image_dims[1] / 2 - BOUND * self.image_dims[1]) > button_x:
                horizontal_move = LEFT
            else:
                horizontal_move = NONE

            if (self.image_dims[0] / 2 + BOUND * self.image_dims[0]) < button_y:
                vertical_move = DOWN
            elif (self.image_dims[0] / 2 - BOUND * self.image_dims[0]) > button_y:
                vertical_move = UP
            else:
                vertical_move = NONE

        return horizontal_move, vertical_move

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

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()
    autonomous_docking = AutonomousDockingNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(autonomous_docking, executor=executor)
