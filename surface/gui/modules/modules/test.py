from interfaces.srv import SelectTask
from event_nodes.client import GUIEventClient
from event_nodes.server import GUIEventServer

import rclpy
import time


def client():
    rclpy.init()

    client = GUIEventClient(SelectTask, 'task_changed_by_manager')
    response = client.send_request({'task': 'Coral Modeling'})
    client.get_logger().info(f'Result of service: {"true" if response.accepted else "false"}')
    
    client.destroy_node()
    rclpy.shutdown()

def server():
    rclpy.init()

    service = GUIEventServer(SelectTask, 'task_changed_by_manager', serverCallback)

    rclpy.spin(service)

    rclpy.shutdown()

def serverCallback(request, response):
    response.accepted = (request.task == 'test task 2')

    return response