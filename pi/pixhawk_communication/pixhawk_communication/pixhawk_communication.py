# from pymavlink import mavutil

# # Start a connection listening on a UDP port
# pixhawk: mavutil.mavserial = mavutil.mavlink_connection('/dev/ttyUSB0')
# pixhawk.wait_heartbeat()

# # Once connected, use 'the_connection' to get and send messages

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PixhawkCommunication(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
