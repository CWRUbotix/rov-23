import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from task_selector_interfaces.action import Example

class TaskRequestor(Node):
    
    def __init__(self):
        super().__init__('task_requestor')
        self._action_client = ActionClient(self, Example, 'cool_example')
        
    def send_goal(self, morning):
        goal_msg = Example.Goal()
        goal_msg.morning = morning
        
        self._action_client.wait_for_server()
        
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback = self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.message))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.feedback_message))


    
def main(args=None):
    rclpy.init(args=args)
    
    action_client = TaskRequestor()
    
    future = action_client.send_goal(True)
    
    rclpy.spin(action_client, future)
        
if __name__ == '__main__':
    main()