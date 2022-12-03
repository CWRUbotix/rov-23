import rclpy
from rclpy.node import Node

# from rclpy.action import ActionServer


class ManipActionServer(Node):

    def __init__(self):
        super().__init__('manipulation_action_server')
        #  self._action_server = ActionServer(self,
        # Type,
        # 'fibonacci',
        # self.execute_callback)
        #

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = 1
        return result


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = ManipActionServer()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
