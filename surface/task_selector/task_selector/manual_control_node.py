import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask
from interfaces.msg import ROVControl
from sensor_msgs.msg import Joy


class ManualControlNode(Node):
    # Maybe should be ENUMS?

    # joy_msg: Joy
    passing: bool = False
    # Button meanings for PS5 Control might be different for others
    X_BUTTON:        int = 0
    O_BUTTON:        int = 1
    TRI_BUTTON:      int = 2
    SQUARE_BUTTON:   int = 3
    L1:              int = 4
    R1:              int = 5
    L2:              int = 6
    R2:              int = 7
    PAIRING_BUTTON:  int = 8
    MENU:            int = 9
    PS_BUTTON:       int = 10
    LJOYPRESS:       int = 11
    RJOYPRESS:       int = 12

    # Joystick Directions 1 is up/left -1 is down/right
    # X is forward/backward Y is left/right
    # L2 and R2 1 is not pressed and -1 is pressed
    LJOYY:           int = 0
    LJOYX:           int = 1
    L2PRESS_PERCENT: int = 2
    RJOYY:           int = 3
    RJOYX:           int = 4
    R2PRESS_PERCENT: int = 5
    DPADHOR:         int = 6
    DPADVERT:        int = 7

    def __init__(self):
        super().__init__('manual_control_node',
                         parameter_overrides=[])

        self._action_server = ActionServer(
            self,
            BasicTask,
            'manual_control',
            self.execute_callback
        )
        self.pixhawk_publisher = self.create_publisher(
            ROVControl,
            'pixhawk_direction_values',
            10
        )
        # TODO add manipulators
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.controller_callback,
            100
        )

    def controller_callback(self, msg: Joy):
        if (self.passing):
            axes = msg.axes
            buttons = msg.buttons
            # TODO someone else should check to make sure these are correct
            # as in pitch yaw roll spin the right way
            rov_msg = ROVControl()
            rov_msg.header = msg.header
            # Left Joystick XY
            rov_msg.x = self.joystick_profiles(axes[self.LJOYX])
            rov_msg.y = self.joystick_profiles(axes[self.LJOYY])
            # Right Joystick Z
            rov_msg.z = self.joystick_profiles(axes[self.RJOYX])
            # TODO math wrong
            # Not sure if it spins correct way around z
            rov_msg.yaw = self.joystick_profiles(l2_r2_math(axes[self.L2PRESS_PERCENT],
                                                            axes[self.R2PRESS_PERCENT]))
            rov_msg.pitch = float(-buttons[self.L1] + buttons[self.R1])
            rov_msg.roll = axes[self.DPADVERT]
            self.pixhawk_publisher.publish(rov_msg)

    # Used to create smoother adjustments
    def joystick_profiles(self, val: float):
        return val * abs(val)

    # TODO what is a goal_handle????
    def execute_callback(self, goal_handle):
        self.get_logger().info('Starting Manual Control')

        if goal_handle.is_cancel_requested:
            self.passing = False

            goal_handle.canceled()
            self.get_logger().info('Ending Manual Control')
            return BasicTask.Result()
        else:
            self.passing = True

            feedback_msg = BasicTask.Feedback()
            feedback_msg.feedback_message = "Task is executing"
            goal_handle.publish_feedback(feedback_msg)
            goal_handle.succeed()
            return BasicTask.Result()

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def l2_r2_math(l2: float, r2: float):
    return (l2 - r2)/2


def main():
    rclpy.init()

    manual_control = ManualControlNode()
    executor = MultiThreadedExecutor()

    rclpy.spin(manual_control, executor=executor)
