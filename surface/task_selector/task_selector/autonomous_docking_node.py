import rclpy
from rclpy.node import Node, Subscription, Publisher
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask
from interfaces.msg import ROVControl
from sensor_msgs.msg import Joy

class AutonomousDockingControlNode(Node):

    def __init__(self):
        super().__init__('autonomous_docking_node',
                         parameter_overrides=[])
        self._action_server = ActionServer(
            self,
            BasicTask,
            'autonomous_docking',
            self.execute_callback
        )
        # TODO: Add Subscriber and Publisher for camera streaming
        self.camera_stream_publisher: Publisher = self.create_publisher(
            #Missing Parameters
        )
        # TODO: Create/Refine ROV Control system for movement regarding the Pixhawk

        # Method of receiving ROV positional parameters
        self.pixhawk_publisher: Publisher = self.create_publisher(
            ROVControl,
            'pixhawk_direction_values',
            10                  #ALERT! I do not know what this value represents
        )

        self.subscription: Subscription = self.create_subscription(
            # Missing Parameters
            self.docking_callback,
            100                         #ALERT! I do not know what this value represents
        )

    def docking_callback(self, msg: Joy):
        rov_msg = ROVControl()


    def execute_callback(self, goal_handle: ServerGoalHandle) -> BasicTask.Result:
        self.get_logger().info('Starting Autonomous Docking...')

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
            self.get_logger().info('Docking canceled')
            return BasicTask.Result()
        else:
            feedback_msg = BasicTask.Feedback()
            feedback_msg.feedback_message = "Task is executing"

            self.get_logger().info('Feedback: ' + feedback_msg.feedback_message)

            goal_handle.publish_feedback(feedback_msg)
            goal_handle.succeed()
            return BasicTask.Result()

    # Can I remove goal_handle as a parameter?
    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()
    docking_control = AutonomousDockingControlNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(docking_control, executor=executor)
