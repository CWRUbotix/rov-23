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
        
        self.manip_states: dict = {
            "claw0": False, 
            "claw1": False, 
            "claw2": False, 
            "claw3": False 
        }

        self.last_manip_states: dict = {
            "claw0": False, 
            "claw1": False, 
            "claw2": False, 
            "claw3": False 
        }
        
    def manip_callback(self, request: Manip):
        manip_id = request.manip_id
        activated = request.activated
        
        # self.get_logger().info("activated="+str(activated))

        if activated and activated != self.last_manip_states[manip_id]:
            new_manip_state = not self.manip_states[manip_id]

            self.manip_states[manip_id] = new_manip_state
        self.get_logger().info("manip_id="+str(manip_id)+" manip_active="+str(new_manip_state))

        pin = self.get_parameter(manip_id).get_parameter_value().integer_value

        self.last_manip_states[manip_id] = activated

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