import rclpy
import time
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
# Range of values Pixhawk takes in microseconds
ZERO_SPEED: int = 1500
RANGE_SPEED: int = 400
# --------------------------------------------------------------------------------------------



class AutonomousDockingControlNode(Node):

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
        # Initial conditions for image dimension
        self.image_dims = [-1, -1]

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

    def handle_frame(self, frame: Image):
        # Converts image msg to BGR w/ alpha channel
        cv_image = self.cv_bridge.imgmsg_to_cv2(frame, desired_encoding='CV_8UC4') 
        get_button_contour(cv_image)
        
        rov_msg = ROVControl()
        # TODO: Should I made a header? If so, to what?
        # rov_msg.header = header
        # Directional commands for the ROV
        rov_msg.x = None
        rov_msg.y = None
        rov_msg.z = None
        # Rotational directions for the ROV
        rov_msg.yaw = None
        rov_msg.pitch = None
        rov_msg.roll = None
        self.pixhawk_publisher.publish(rov_msg)

# Takes a OpenCV image as input, and returns a contour surrounding the button (The largest red object)
def get_button_contour(cv_img):
    # Constant value to offset CV binary threshhold
    c = 0

    # Use LAB colorspace to segment/enhance red in the original image
    Lab = cv2.cvtColor(cv_img, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(Lab)
    
    cv2.imshow("LAB Thresh", A)

    gray = A                                    # Takes the A-channel, grayscale representing the red and green in the image
    gray = cv2.GaussianBlur(gray, (7, 7), 0)    # Blurs the image to smooth the edges
    img_h, img_w = gray.shape                   # Calling this on the BGR will get (x, y, 3)
    
    # Threshold it, getting a bitmap
    gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, c)
    cv2.imshow("Gaussian", cv2.bitwise_and(cv_img, cv_img, mask=gaussian))
    cv2.imshow("Original", cv_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # The HSV colormap of the original image, but with the gaussian threshold mask applied
    gaussMaskedHSV = cv2.cvtColor(cv2.bitwise_and(cv_img, cv_img, mask=gaussian), cv2.COLOR_BGR2HSV)

    # Lower mask (0-10 red range of color)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(gaussMaskedHSV, lower_red, upper_red)

    # upper mask (170-180 red range of color)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(gaussMaskedHSV, lower_red, upper_red)
    # The final mask of the lower red and upper red combined
    finalMasked2 = mask0 + mask1

    cv2.imshow("Final Mask", finalMasked2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#TODO: Add morphological CLOSE and OPEN? 

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

#TODO: Somehow parse camera frame into an OpenCV image
# Takes and processes a camera frame
# Determines the direction that the bot should move in
    # Does position processing regarding the button

def move_direction(self, image):
    horizontal_move = NONE
    vertical_move = NONE
    contour, area = get_button_contour(image)

    # Gets the coordinates for the button's position and image dimensions
    # Once a contour has been found
    if area > 0:
        (button_x, button_y), radius = cv2.minEnclosingCircle(contour)
        self.image_dims[0], self.image_dims[1] = image.shape
    
    # Takes the dimensions of the image
    # And then determines if the button is close to the center
    if (self.frame.dimension[0] / 2 + self.frame.dimension[0] * BP) < button_x:
        horizontal_move = LEFT
    elif (self.frame.dimension[0] / 2 - self.frame.dimension[0] * BP) > button_x:
        horizontal_move = RIGHT
    else:
        horizontal_move = NONE
    
    if (self.frame.dimension[1] / 2 + self.frame.dimension[1] * BP) < button_y:
        vertical_move = DOWN
    elif (self.frame.dimension[1] / 2 - self.frame.dimension[1] * BP) > button_y:
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
