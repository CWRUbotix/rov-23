import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ManipulatorSubscriber(Node):

    def __init__(self):
        super().__init__('manipulator_subscriber')
        # self.subscription = self.create_subscription(
        #     String,
        #     'topic',
        #     self.listener_callback,
        #     10)
        # self.subscription  # prevent unused variable warning

        # self.service = self.create_service(AddTwoInts, 'add_two_ints', self.listener_callback)

        self.declare_parameters(
            namespace="",
            parameters=[
                ("claw0", rclpy.Parameter.Type.INTEGER),
                ("claw1", rclpy.Parameter.Type.INTEGER),
                ("claw2", rclpy.Parameter.Type.INTEGER),
                ("claw3", rclpy.Parameter.Type.INTEGER),
            ])
        
    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response

    def listener_callback(self, msg):
        

        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)

    subscriber = ManipulatorSubscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()