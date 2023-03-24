import serial
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SerialReader(Node):
    
    def __init__(self):
        super().__init__('serial_reader')
        self.publisher_ = self.create_publisher(String, 'tranciever_data', 10)
        self.listener = self.create_subscription(
            String, 
            'tranciever_control', 
            self.control_callback, 
            10)
        timer_period = .5
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = self.ser.readline().decode()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    
    def control_callback(self, msg):
        self.ser.write(msg)
        self.get_logger().info('Command sent via serial monitor: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    serial_reader = SerialReader()

    rclpy.spin(serial_reader)

if __name__ == '__main__':
    main()