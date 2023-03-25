import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import BasicTask


class BasicTaskTimedNode(Node):

    def __init__(self):
        super().__init__('basic_task_timed',
                         parameter_overrides=[],
                         namespace='surface')
        self._action_server = ActionServer(
            self,
            BasicTask,
            'timed_task',
            self.execute_callback,
            cancel_callback=self.cancel_callback
        )

    def execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Executing goal...')

        feedback_msg = BasicTask.Feedback()
        for x in range(10):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return BasicTask.Result()
            else:
                feedback_msg.feedback_message = str(10 - x) + " seconds left"

                self.get_logger().info(
                    'Feedback:' + feedback_msg.feedback_message)
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1)

        goal_handle.succeed()

        result = BasicTask.Result()
        return result

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()

    task_controller = BasicTaskTimedNode()
    executor = MultiThreadedExecutor()
    rclpy.spin(task_controller, executor=executor)
