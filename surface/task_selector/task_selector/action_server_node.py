import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from task_selector_interfaces.action import Example

class TaskController(Node):
    
    def __init__(self):
        super().__init__('task_controller')
        self._action_server = ActionServer(
            self,
            Example,
            'cool_example',
            self.execute_callback
        )
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        feedback_msg = Example.Feedback()
        feedback_msg.feedback_message = "I am thinking about what to say to you"
        
        self.get_logger().info('Feedback:' + feedback_msg.feedback_message)
        goal_handle.publish_feedback(feedback_msg)
        
        is_morning = goal_handle.request.morning
        is_cheery = goal_handle.request.cheery
        
        if(is_morning):
            message = "Good morning!"
        else:
            message = "Good not morning!"
        
        goal_handle.succeed()
        
        result = Example.Result()
        result.message = message
        return result
    
def main(args=None):
    rclpy.init(args=args)
    
    task_controller = TaskController()
    
    rclpy.spin(task_controller)
    
if __name__ == '__main__':
    main()