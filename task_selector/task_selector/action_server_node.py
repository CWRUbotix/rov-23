import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

class TaskController(Node):
    
    def __init__(self):
        super().__init__('task_controller')
        self._action_server = ActionServer(
            self,
            Example,
            'cool example',
            self.execute_callback
        )
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = Example.Result()
        return result