import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask


class BasicTaskNode(Node):

    def __init__(self):
        super().__init__('basic_task_node',
                         parameter_overrides=[],
                         namespace='surface')
        self._action_server = ActionServer(
            self,
            BasicTask,
            'example_task',
            self.execute_callback
        )

    def execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Executing goal...')

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
            self.get_logger().info('Goal canceled')
            return BasicTask.Result()
        else:
            feedback_msg = BasicTask.Feedback()
            feedback_msg.feedback_message = "Task is executing"

            self.get_logger().info('Feedback:' + feedback_msg.feedback_message)
            goal_handle.publish_feedback(feedback_msg)

            goal_handle.succeed()

            result = BasicTask.Result()
            return result

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()

    task_controller = BasicTaskNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(task_controller, executor=executor)
