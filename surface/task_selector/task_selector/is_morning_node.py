import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from rclpy.executors import MultiThreadedExecutor

from interfaces.action import Example


class IsMorning(Node):

    def __init__(self):
        super().__init__('good_morning_sayer',
                         parameter_overrides=[],
                         namespace='surface')
        self._action_server = ActionServer(
            self,
            Example,
            'say_good_morning',
            self.execute_callback
        )

    def execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('Executing goal...')

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
            self.get_logger().info('Goal canceled')
            return Example.Result()
        else:
            feedback_msg = Example.Feedback()
            feedback_msg.feedback_message = """I am thinking about what to say to you"""

            self.get_logger().info('Feedback:' + feedback_msg.feedback_message)
            goal_handle.publish_feedback(feedback_msg)

            is_morning = goal_handle.request.morning
            is_cheery = goal_handle.request.cheery

            if is_cheery:
                message = 'Good'
            else:
                message = 'Not good'

            if is_morning:
                message += ' morning!'
            else:
                message += ' not morning!'

            goal_handle.succeed()

            result = Example.Result()
            result.message = message
            return result


def main():
    rclpy.init()

    task_controller = IsMorning()
    executor = MultiThreadedExecutor()
    rclpy.spin(task_controller, executor=executor)
