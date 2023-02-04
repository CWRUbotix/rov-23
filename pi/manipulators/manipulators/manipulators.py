import rclpy
from rclpy.node import Node
from interfaces.srv import ManipService, TaskRequest


class Manipulator(Node):

    def __init__(self):
        super().__init__('manipulator')

        self.service = self.create_service(ManipService, "manip_service", self.listener_callback)

        self.declare_parameters(
            namespace="",
            parameters=[
                ("claw0", rclpy.Parameter.Type.INTEGER),
                ("claw1", rclpy.Parameter.Type.INTEGER),
                ("claw2", rclpy.Parameter.Type.INTEGER),
                ("claw3", rclpy.Parameter.Type.INTEGER),
            ])
        
    def listener_callback(self, request: ManipService.Request, response: ManipService.Response):
        manip_id = request.manip_id
        activated = request.activated

        self.get_logger().info("manip_id="+str(manip_id)+" activated="+str(activated))

        return response

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