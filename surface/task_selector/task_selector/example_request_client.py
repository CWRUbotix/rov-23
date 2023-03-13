import time

import rclpy
from rclpy.node import Node
from interfaces.srv import TaskRequest
from task_selector.tasks import Tasks


class ExampleRequestClient(Node):

    def __init__(self):
        super().__init__('example_request_client',
                         namespace='surface')
        self.cli = self.create_client(TaskRequest, 'gui/task_request')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TaskRequest.Request()

    def send_request(self, task_id):
        enum_id = task_id.value
        self.req.task_id = enum_id
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    example_client = ExampleRequestClient()

    example_client.get_logger().info("Sending timer request")
    response = example_client.send_request(Tasks.EX_TIMED)
    example_client.get_logger().info(response.response)

    time.sleep(5)

    example_client.get_logger().info("Sending morning request")
    response = example_client.send_request(Tasks.EX_GOOD_MORNING)
    example_client.get_logger().info(response.response)

    time.sleep(2)

    example_client.get_logger().info("Sending basic request")
    response = example_client.send_request(Tasks.EX_BASIC)
    example_client.get_logger().info(response.response)

    example_client.destroy_node()
    rclpy.shutdown()
