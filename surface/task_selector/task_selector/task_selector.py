import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from interfaces.srv import TaskRequest
from interfaces.msg import TaskFeedback

# from interfaces.action import Example
from interfaces.action import BasicTask

from task_selector.tasks import Tasks


class TaskSelector(Node):

    def __init__(self):
        # creation of a Node with its name as input
        super().__init__('task_selector',
                         parameter_overrides=[],
                         namespace='surface')

        # create service to handle requests for task switching
        self.request_server = self.create_service(
            TaskRequest, 'gui/task_request', self.request_task_callback)

        self.feedback_server = self.create_publisher(
            TaskFeedback, 'gui/task_feedback', 10)

        # instantiates new action clients with inputs of node,
        # action type, action name
        # self.morning_action_client = ActionClient(self,
        #                                           Example,
        #                                           'say_good_morning')
        # self.timed_task_client = ActionClient(self,
        #                                       BasicTask,
        #                                       'timed_task')
        # self.basic_task_client = ActionClient(self,
        #                                       BasicTask,
        #                                       'example_task')

        self.manual_control_client = ActionClient(self,
                                                  BasicTask,
                                                  'manual_control')
        self.active = False
        self._goal_handle = None

        self.send_basic_goal(self.manual_control_client)

    def request_task_callback(self, request: TaskRequest.Request,
                              response: TaskRequest.Response):
        response.response = "Acknowledged"
        if self.active:
            self.cancel_goal()

        if request.task_id == Tasks.MANUAL_CONTROL.value:
            self.active = True
            self.send_basic_goal(self.manual_control_client)
        # elif request.task_id == Tasks.EX_GOOD_MORNING.value:
        #     self.send_morning_goal(True, True)
        # elif request.task_id == Tasks.EX_TIMED.value:
        #     self.send_basic_goal(self.timed_task_client)
        # elif request.task_id == Tasks.EX_BASIC.value:
        #     self.send_basic_goal(self.basic_task_client)
        elif request.task_id == Tasks.AUTO_DOCKING.value:
            pass
        elif request.task_id == Tasks.CANCEL.value:
            response.response = "Canceled"
        else:
            response.response = "Invalid task id"
        return response

    # Basic task client takes no input variables and only receives feedback,
    # no result data
    #
    # send_basic_goal() takes a basic client and requests for the server it's
    # attached to to run a task
    def send_basic_goal(self, client: ActionClient):
        goal_msg = BasicTask.Goal()

        if not self.active:
            self.get_logger().info('Waiting for action server...')
        client.wait_for_server()

        if not self.active:
            self.get_logger().info('Sending goal request...')
        self._send_goal_future = client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback)

        # self._send_goal_future.add_done_callback(self.basic_response_callback)

    # # A Say Good Morning server takes the time of day and cheeriness to
    # # produce a greeting
    # def send_morning_goal(self, morning: bool, cheery: bool):
    #     goal_msg = Example.Goal()
    #     goal_msg.morning = morning
    #     goal_msg.cheery = cheery

    #     self.get_logger().info('Waiting for action server...')
    #     self.morning_action_client.wait_for_server()

    #     self.get_logger().info('Sending goal request...')
    #     self._send_goal_future = self.morning_action_client.send_goal_async(
    #         goal_msg, feedback_callback=self.feedback_callback)
    #     self._send_goal_future.add_done_callback(
    #         self.morning_response_callback)

    # Checks if goal was accepted
    def basic_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._goal_handle = goal_handle

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.basic_result_callback)

    # def morning_response_callback(self, future):
    #     goal_handle = future.result()
    #     if not goal_handle.accepted:
    #         self.get_logger().info('Goal rejected')
    #         return

    #     self.get_logger().info('Goal accepted')

    #     self._get_result_future = goal_handle.get_result_async()
    #     self._get_result_future.add_done_callback(self.morning_result_callback)

    # Notify us that task is finished
    def basic_result_callback(self, future):
        self.get_logger().info("Task finished")
        self.active = False

    # # Logs greeting that the morning server sends
    # def morning_result_callback(self, future):
    #     result = future.result().result
    #     self.get_logger().info('Result: {0}'.format(result.message))
    #     self.active = False

    # Logs feedback from action server
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            'Received feedback: {0}'.format(feedback.feedback_message))

    # Only works if server runs on a multithreaded executor
    def cancel_goal(self):
        if self._goal_handle is None:
            self.get_logger().warn('Could not cancel goal because there is none')
            return

        self.get_logger().info('Canceling goal')
        # Cancel the goal
        future = self._goal_handle.cancel_goal_async()
        future.add_done_callback(self.cancel_done)

    # Logs if goal was canceled
    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal successfully canceled')
            self.active = False
        else:
            self.get_logger().info('Goal failed to cancel')


def main():
    rclpy.init()

    action_client = TaskSelector()

    rclpy.spin(action_client)
