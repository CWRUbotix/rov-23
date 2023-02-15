import serial
import rclpy
from rclpy.node import Node

class SerialReader(Node):
    
    def __init__(self):
        super().__init__('serial_reader')
        self.publisher = self.create_publisher(String, 'tranciever_data', 10)
        timer_period = 1
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = self.ser.readline()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    serial_reader = SerialReader

    rclpy.spin(serial_reader)

if __name__ == '__main__':
    main()