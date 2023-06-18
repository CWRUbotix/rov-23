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

        # GPIO.BCM because we use a Compute Module
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        self.check_input()

    # https://www.ics.com/blog/control-raspberry-pi-gpio-pins-python
    # Investigate adding callback for when in is pulled high maybe?
    def check_input(self):
        while True:
            self.pub.publish(Bool(GPIO.input(PIN)))

            if GPIO.input(PIN) == GPIO.HIGH:
                self.get_logger().error("FLOODING DETECTED!")


def main():
    rclpy.init()
    node = FloodWarning()
    rclpy.spin(node)
    GPIO.cleanup()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
