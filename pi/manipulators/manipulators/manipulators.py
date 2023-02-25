import rclpy
from rclpy.node import Node, Subscription
from interfaces.msg import Manip


class Manipulator(Node):

    def __init__(self):
        super().__init__('manipulator')

        self.subscription: Subscription = self.create_subscription(
            Manip,
            'manipulator_control',
            self.manip_callback,
            100
        )

        self.declare_parameters(
            namespace="",
            parameters=[
                ("claw0", rclpy.Parameter.Type.INTEGER),
                ("claw1", rclpy.Parameter.Type.INTEGER),
                ("claw2", rclpy.Parameter.Type.INTEGER),
                ("claw3", rclpy.Parameter.Type.INTEGER),
            ])
                
    def manip_callback(self, request: Manip):
        manip_id = request.manip_id
        activated = request.activated

        # pin = self.get_parameter(manip_id).get_parameter_value().integer_value

def main(args=None):
    rclpy.init(args=args)

    subscriber = Manipulator()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()