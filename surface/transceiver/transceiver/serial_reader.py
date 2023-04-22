import serial
import rclpy
from rclpy.node import Node
from interfaces.msg import FloatCommand


class SerialReader(Node):

    def __init__(self):
        super().__init__('serial_reader',
                         parameter_overrides=[])
        self.publisher = self.create_publisher(FloatCommand, 'transceiver_data', 10)
        self.listener = self.create_subscription(
            FloatCommand,
            'transceiver_control',
            self.control_callback,
            10)
        timer_period = .5
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = FloatCommand()
        msg.command = self.ser.readline().decode()
        self.publisher.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        # self.i += 1

    def control_callback(self, msg: FloatCommand):
        msg_encode: bytes = msg.command.encode()
        self.ser.write(msg_encode)
        self.get_logger().info(f'Command sent via serial monitor: {msg_encode}')


def main():
    rclpy.init()

    serial_reader = SerialReader()

    rclpy.spin(serial_reader)


if __name__ == '__main__':
    main()
