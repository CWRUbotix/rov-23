import rclpy
from rclpy.node import Node, Subscription
from interfaces.msg import Manip
from manipulators.tca9555 import TCA9555


class Manipulator(Node):

    def __init__(self):
        super().__init__('manipulator',
                         parameter_overrides=[])

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
                ("light", rclpy.Parameter.Type.INTEGER),
            ])

        # Initialize with standard I2C-bus address of TCA9555 a.k.a 0x20
        self.gpio = TCA9555()  # can put in the address as a param in hexadecimal
        self.get_logger().info(str(self.gpio.format_config()))

        # Set pins 0 through 5 as output
        self.gpio.set_direction(0, bits=(0, 1, 2, 3, 4, 5))
        self.gpio.unset_bits(bits=(0, 1, 2, 3, 4, 5))

    def manip_callback(self, request: Manip):
        manip_id = request.manip_id
        activated = request.activated

        pin = self._parameters[manip_id].get_parameter_value().integer_value

        if activated:
            self.gpio.set_bits(bits=(pin))
        else:
            self.gpio.unset_bits(bits=(pin))


def main():
    rclpy.init()

    subscriber = Manipulator()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
