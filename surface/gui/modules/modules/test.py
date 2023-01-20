import rclpy

from interfaces.srv import TaskRequest
from interfaces.msg import TaskFeedback
from event_nodes.publisher import GUIEventPublisher
from event_nodes.server import GUIEventServer


def publisher():
    rclpy.init()
    pub = GUIEventPublisher(TaskFeedback, 'task_feedback')
    pub.publish({'task_id': 2})

    pub.destroy_node()
    rclpy.shutdown()


def server():
    rclpy.init()

    service = GUIEventServer(
        TaskRequest, 'task_request', serverCallback)

    rclpy.spin(service)

    rclpy.shutdown()


def serverCallback(request, response):
    print(f'Changing task to {request.task_id}')

    response.response = 'Task request recieved by test'

    return response
