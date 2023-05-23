from pymavlink import mavutil
from pymavlink.mavutil import mavfile
import rclpy
from rclpy.node import Node, Subscription

from interfaces.msg import Armed, ROVControl


MAX_CHANNEL: int = 8
MIN_CHANNEL: int = 1

PITCH_CHANNEL:    int = 1
ROLL_CHANNEL:     int = 2
THROTTLE_CHANNEL: int = 3
YAW_CHANNEL:      int = 4
FORWARD_CHANNEL:  int = 5
LATERAL_CHANNEL:  int = 6


class PixhawkCommunication(Node):

    def __init__(self):
        super().__init__('pixhawk_communication',
                         parameter_overrides=[])
        self.arm_sub: Subscription = self.create_subscription(
            Armed,
            'armed',
            self.arm_callback,
            1
        )
        self.rov_control_sub: Subscription = self.create_subscription(
            ROVControl,
            'manual_control',
            self.rov_control_callback,
            100
        )
        self.declare_parameter('connection', '/dev/ttyPixhawk')
        communication: str = self.get_parameter('connection').get_parameter_value().string_value
        self.pixhawk: mavfile = mavutil.mavlink_connection(communication)
        self.pixhawk.wait_heartbeat()

    def arm_callback(self, msg: Armed):
        """Arms/Disarm everytime the gui buttons are clicked in a callback."""
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system,
            self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            # ternary for this bit for deciding arm
            # 1 is armed 0 is disarmed
            1 if msg.armed else 0,
            0, 0, 0, 0, 0, 0)
        if msg.armed:
            self.pixhawk.motors_armed_wait()
        else:
            self.pixhawk.motors_disarmed_wait()
        arm_str: str = "ROV Armed" if self.pixhawk.motors_armed() else "ROV Disarmed"
        self.get_logger().info(arm_str)

    def rov_control_callback(self, msg: ROVControl):
        """Send RC to the Pixhawk in a callback."""
        rc_channel_values = [65535 for _ in range(MAX_CHANNEL)]
        rc_channel_values[ROLL_CHANNEL - 1] = msg.roll
        rc_channel_values[PITCH_CHANNEL - 1] = msg.pitch
        rc_channel_values[THROTTLE_CHANNEL - 1] = msg.z
        rc_channel_values[YAW_CHANNEL - 1] = msg.yaw
        rc_channel_values[FORWARD_CHANNEL - 1] = msg.x
        rc_channel_values[LATERAL_CHANNEL - 1] = msg.y

        self.pixhawk.mav.rc_channels_override_send(
            self.pixhawk.target_system,
            self.pixhawk.target_component,
            *rc_channel_values)


def main():
    rclpy.init()
    pixhawk_com = PixhawkCommunication()
    rclpy.spin(pixhawk_com)
