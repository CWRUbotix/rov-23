import rclpy
from rclpy.node import Node, Subscription, Publisher
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask
from interfaces.msg import ROVControl, Manip
from sensor_msgs.msg import Joy

from typing import Dict, List


# Button meanings for PS5 Control might be different for others
X_BUTTON:        int = 0  # Manipulator 0
O_BUTTON:        int = 1  # Manipulator 1
TRI_BUTTON:      int = 2  # Manipulator 2
SQUARE_BUTTON:   int = 3  # Manipulator 3
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

# Range of values Pixhawk takes
# In microseconds
ZERO_SPEED: int = 1500
RANGE_SPEED: int = 400


class ManualControlNode(Node):
    _passing: bool = False

    def __init__(self):
        super().__init__('manual_control_node',
                         parameter_overrides=[],
                         namespace='surface')
        # TODO would Service make more sense then Actions?
        self._action_server: ActionServer = ActionServer(
            self,
            BasicTask,
            'manual_control',
            self.execute_callback
        )
        self.pixhawk_publisher: Publisher = self.create_publisher(
            ROVControl,
            'pixhawk_manual_control',
            10
        )
        self.subscription: Subscription = self.create_subscription(
            Joy,
            'joy',
            self.controller_callback,
            100
        )

        # Manipulators
        self.manip_publisher: Publisher = self.create_publisher(
            Manip,
            'manipulator_control',
            10
        )

        self.manip_buttons: Dict[int, ManipButton] = {
            X_BUTTON: ManipButton("claw0"),
            O_BUTTON: ManipButton("claw1"),
            TRI_BUTTON: ManipButton("claw2"),
            SQUARE_BUTTON: ManipButton("claw3")
        }

    def controller_callback(self, msg: Joy):
        if self._passing:
            self.joystick_to_pixhawk(msg)
            self.manip_callback(msg)

    def joystick_to_pixhawk(self, msg: Joy):
        axes = msg.axes
        buttons = msg.buttons
        # TODO someone else should check to make sure these are correct
        # as in pitch yaw roll spin the right way
        rov_msg = ROVControl()
        rov_msg.header = msg.header
        # Left Joystick XY
        rov_msg.x = self.joystick_profiles(axes[LJOYX])
        rov_msg.y = self.joystick_profiles(axes[LJOYY])
        # Right Joystick Z
        rov_msg.z = self.joystick_profiles(axes[RJOYX])
        # Not sure if it spins correct way around z
        rov_msg.yaw = self.joystick_profiles((axes[L2PRESS_PERCENT] -
                                              axes[R2PRESS_PERCENT])/2)
        rov_msg.pitch = self.joystick_profiles(axes[DPADVERT])
        rov_msg.roll = self.joystick_profiles(-buttons[L1] + buttons[R1])
        self.pixhawk_publisher.publish(rov_msg)

    # Used to create smoother adjustments
    def joystick_profiles(self, val: float) -> int:
        return ZERO_SPEED + int(RANGE_SPEED * val * abs(val))

    def execute_callback(self, goal_handle: ServerGoalHandle) -> BasicTask.Result:
        self.get_logger().info('Starting Manual Control')

        if goal_handle.is_cancel_requested:
            self._passing = False

            goal_handle.canceled()
            self.get_logger().info('Ending Manual Control')
            return BasicTask.Result()
        else:
            self._passing = True

            feedback_msg = BasicTask.Feedback()
            feedback_msg.feedback_message = "Task is executing"
            goal_handle.publish_feedback(feedback_msg)
            goal_handle.succeed()
            return BasicTask.Result()

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        self._passing = False
        return CancelResponse.ACCEPT

    def manip_callback(self, msg: Joy):
        buttons: List[int] = msg.buttons

        for button_id, manip_button in self.manip_buttons.items():

            just_pressed: bool = False

            if buttons[button_id] == 1:
                just_pressed = True

            if manip_button.last_button_state is False and just_pressed:
                new_manip_state: bool = not manip_button.is_active
                manip_button.is_active = new_manip_state

                log_msg: str = f"manip_id= {manip_button.claw}, manip_active= {new_manip_state}"
                self.get_logger().info(log_msg)

            manip_button.last_button_state = just_pressed

            manip_msg: Manip = Manip(manip_id=manip_button.claw,
                                     activated=manip_button.is_active)
            self.manip_publisher.publish(manip_msg)


class ManipButton:
    def __init__(self, claw: str):
        self.claw: str = claw
        self.last_button_state: bool = False
        self.is_active: bool = False


def main():
    rclpy.init()
    manual_control = ManualControlNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(manual_control, executor=executor)
