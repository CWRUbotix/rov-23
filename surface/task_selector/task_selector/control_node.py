import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask
from interfaces.msg import ROVControl
from sensor_msgs.msg import Joy


class ControlNode(Node):

    # joy_msg: Joy
    passing: bool = False
    # Button meanings for PS5 Control might be different for others
    XBUTTON = 0
    OBUTTON = 1
    TRIBUTTON = 2
    SQUAREBUTTON = 3
    L1 = 4
    R1 = 5
    L2 = 6
    R2 = 7
    PAIRINGBUTTON = 8
    MENU = 9
    PSBUTTON = 10
    LJOYPRESS = 11
    RJOYPRESS = 12

    # Joystick Directions 1 is up/left -1 is down/right
    # X is forward/backward Y is left/right
    # L2 and R2 1 is not pressed and -1 is pressed
    LJOYY = 0
    LJOYX = 1
    L2PRESSPERCENT = 2
    RJOYY = 3
    RJOYX = 4
    R2PRESSPERCENT = 5
    DPADHOR = 6
    DPADVERT = 7

    def __init__(self):
        super().__init__(
            'control_node',
            parameter_overrides=[]
            )

        self._action_server = ActionServer(
            self,
            BasicTask,
            'manual_control',
            self.execute_callback
        )
        self.pixhawk_publisher = self.create_publisher(
            ROVControl,
            'PIXHawk_Direction_Values',
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
            # Trust me on this math
            # Not sure if it spins correct way around z
            rov_msg.yaw = self.joystick_profiles(
                (axes[self.L2PRESSPERCENT] - buttons[self.R2]) -
                axes[self.R2PRESSPERCENT] - buttons[self.L2])
            rov_msg.pitch = float(-buttons[self.L1] + buttons[self.R1])
            rov_msg.roll = axes[self.DPADVERT]
            self.pixhawk_publisher.publish(rov_msg)

    # Used to create smoother adjustments
    def joystick_profiles(self, val: float):
        return val * abs(val)

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


def main():
    rclpy.init()

    task_controller = ControlNode()

    executor = MultiThreadedExecutor()

    rclpy.spin(task_controller, executor=executor)
