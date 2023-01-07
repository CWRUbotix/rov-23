import time
import random

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from task_selector_interfaces.action import BasicTask

class BasicTaskNode(Node):
    
    def __init__(self):
        super().__init__('basic_task_node')
        self._action_server = ActionServer(
            self,
            BasicTask,
            'example_task',
            self.execute_callback
        )
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        feedback_msg = BasicTask.Feedback()
        feedback_msg.feedback_message = "Task is executing"
        
        self.get_logger().info('Feedback:' + feedback_msg.feedback_message)
        goal_handle.publish_feedback(feedback_msg)
        
        goal_handle.succeed()
        
        result = BasicTask.Result()
        return result
    
def main(args=None):
    rclpy.init(args=args)
    
    task_controller = BasicTaskNode()
    
    rclpy.spin(task_controller)
    
if __name__ == '__main__':
    main()