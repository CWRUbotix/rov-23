import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import RPi.GPIO as GPIO


# GPIO PIN #
PIN = 26


class Flood_Warning(Node):

    def __init__(self):
        super().__init__('flood_warning',
                         parameter_overrides=[])

        self.pub = self.create_publisher(
            Bool,
            '/flood_status',
            100
        )

    def check_input(self):
        while True:
            self.pub.publish(Bool(GPIO.input(PIN)))

            if GPIO.input(PIN) == GPIO.HIGH:
                self.get_logger().error("FLOODING DETECTED!")


def main():
    rclpy.init()

    pub = Flood_Warning()

    rclpy.spin(pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
