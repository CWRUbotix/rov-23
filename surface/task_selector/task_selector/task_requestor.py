import time

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from task_selector_interfaces.action import Example
from task_selector_interfaces.action import BasicTask

class TaskRequestor(Node):
    
    def __init__(self):
        # creation of a Node with its name as input
        super().__init__('task_requestor')
        # instantiates new action client with inputs of node, action type, action name
        self.morning_action_client = ActionClient(self, Example, 'say_good_morning')
        self.basic_task_client = ActionClient(self, BasicTask, 'timed_task')
        
    
    
    def send_morning_goal(self, morning, cheery):
        goal_msg = Example.Goal()
        goal_msg.morning = morning
        goal_msg.cheery = cheery
        
        self.get_logger().info('Waiting for action server...')
        self.morning_action_client.wait_for_server()
        
        self.get_logger().info('Sending goal request...')
        self._send_goal_future = self.morning_action_client.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
    def send_basic_goal(self, client):
        goal_msg = BasicTask.Goal()
        
        self.get_logger().info('Waiting for action server...')
        client.wait_for_server()
        
        self.get_logger().info('Sending goal request...')
        self._send_goal_future = client.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)
        self._send_goal_future.add_done_callback(self.basic_response_callback)
        
    # Checks if goal was accepted
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')
        
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
        
    def basic_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')
        
        self._goal_handle = goal_handle
        
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.basic_result_callback)

    def basic_result_callback(self, future):
        #result = future.result().result
        self.get_logger().info("Task finished")
        #rclpy.shutdown()

    # Logs result, exits
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.message))
        #rclpy.shutdown()

    # Logs feedback from action server
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.feedback_message))
        
    # Only works if server runs on a multithreaded executor
    def cancel_goal(self):
        self.get_logger().info('Canceling goal')
        # Cancel the goal
        future = self._goal_handle.cancel_goal_async()
        future.add_done_callback(self.cancel_done)
    
    # Logs if goal was canceled
    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal successfully canceled')
        else:
            self.get_logger().info('Goal failed to cancel')
        #rclpy.shutdown()
        
    def timer_callback(self):
        self.cancel_goal()


    
def main(args=None):
    rclpy.init(args=args)
    
    action_client = TaskRequestor()
    
    action_client.send_basic_goal(action_client.basic_task_client)
    cancelled = False
    timer = 0
    while True:
        rclpy.spin_once(action_client)
        
        if timer > 8 and not cancelled:
            print("cancellation time")
            cancelled = True
            action_client.cancel_goal()
            action_client.send_morning_goal(True, True)
        else: 
            timer += 1
            print(timer)
        
        
    
    # create other action clients

    # Get the global executor
    # rclpy.spin() uses this under the hood & rclpy.shutdown() will shut this executor down
    
    # global_executor = rclpy.get_global_executor()
    # global_executor.add_node(action_client)
    # global_executor.spin()

    # different rclpy spins
        
if __name__ == '__main__':
    main()