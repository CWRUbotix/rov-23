import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import RPi.GPIO as GPIO


# GPIO PIN #
PIN = 26


class FloodWarning(Node):

    def __init__(self):
        super().__init__('flood_warning',
                         parameter_overrides=[])

        self.pub = self.create_publisher(
            Bool,
            '/flood_status',
            100
        )
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN, GPIO.OUT)
        self.check_input()

    def check_input(self):
        while True:
            self.pub.publish(Bool(GPIO.input(PIN)))

            if GPIO.input(PIN) == GPIO.HIGH:
                self.get_logger().error("FLOODING DETECTED!")


def main():
    FloodWarning()


if __name__ == '__main__':
    main()
