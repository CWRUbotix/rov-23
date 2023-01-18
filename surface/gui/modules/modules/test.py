from interfaces.srv import TaskRequest
from event_nodes.client import GUIEventClient
from event_nodes.server import GUIEventServer

import rclpy
import time


def client():
    rclpy.init()
    client = GUIEventClient(TaskRequest, 'task_changed_by_manager')
    response = client.send_request({'task_id': 2})
    client.get_logger().info(f'Result of service: {response.response}')

    client.destroy_node()
    rclpy.shutdown()


def server():
    rclpy.init()

    service = GUIEventServer(
        TaskRequest, 'task_changed_by_gui', serverCallback)

    rclpy.spin(service)

    rclpy.shutdown()


def serverCallback(request, response):
    print(f'Changing task to {request.task_id}')

    response = 'Task request recieved by test'

    return response
