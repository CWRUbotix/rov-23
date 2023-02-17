from pymavlink import mavutil

import rclpy
from rclpy.node import Node, Subscription

from rov_interfaces.msg import Armed, ROVControl


class PixhawkCommunication(Node):

    def __init__(self):
        super().__init__('pixhawk_communication')
        self.arm_sub: Subscription = self.create_subscription(
            Armed,
            'armed',
            self.arm_callback,
            1)
        self.rov_control_sub: Subscription = self.create_subscription(
            ROVControl,
            "pixhawk_manual_control",
            self.rov_control_callback,
            100
        )
        # TODO should setup some mask for pixhawk
        # https://docs.px4.io/main/en/companion_computer/pixhawk_companion.html
        self.pixhawk: mavutil.mavserial = mavutil.mavlink_connection("/dev/ttyPixhawk")
        self.pixhawk.wait_heartbeat()

    def arm_callback(self, msg: Armed):
        self.pixhawk.mav.command_long_send(
            self.pixhawk.target_system,
            self.pixhawk.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            # ternary for this bit for deciding arm
            # 1 is armed 0 is disarmed
            1 if msg.armed else 0,
            0, 0, 0, 0, 0, 0)
        self.pixhawk.motors_armed_wait() if msg.armed else self.pixhawk.motors_disarmed_wait()
        self.get_logger().info("ROV Armed") if self.pixhawk.motors_armed() else self.get_logger().info("ROV disarmed")

    def rov_control_callback(self, msg: ROVControl):
        # TODO send manual control
        # https://mavlink.io/en/messages/common.html#COMMAND_LONG
        # self.pixhawk.mav.command_long_send(
        #     self.pixhawk.target_system,
        #     self.pixhawk.target_component
        #     mavutil.mavlink.MAVLINK_MSG_ID_MANUAL_CONTROL,
        #     msg.x,
        #     msg.y,
        #     msg.z,
        # )
        self.get_logger().info("control callback")


def main():
    rclpy.init()
    pixhawk_com = PixhawkCommunication()
    rclpy.spin(pixhawk_com)
