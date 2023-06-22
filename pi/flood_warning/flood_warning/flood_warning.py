import RPi.GPIO as GPIO
import rclpy 
from std_msgs.msg import Bool
from rclpy.node import Node, Publisher

# GPIO PIN #
PIN = 26

class FloodWarning(Node):

    def __init__(self):
        super().__init__('flood_warning',
                         parameter_overrides=[])
        
        self.publisher: Publisher = self.create_publisher(
            Bool,
            'flood_status',
            100
        )

        # GPIO.BCM because we use a Compute Module
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.IN)
        self.listen()

    def listen(self):
        while True:

            if GPIO.input(PIN) == GPIO.HIGH:
                self.get_logger().warn("Flooding detected")
                self.publisher.publish(Bool(data=True))


def main():
    rclpy.init()
    node = FloodWarning()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()