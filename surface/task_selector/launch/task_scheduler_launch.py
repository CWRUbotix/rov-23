from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    requestor_node: Node = Node(
        package='task_selector',
        executable='requestor'
    )

    ex_request_client_node: Node = Node(
        package='task_selector',
        executable='ex_request_client'
    )

    ex_timed_task_node: Node = Node(
        package='task_selector',
        executable='ex_timed_task'
    )

    ex_basic_task_node: Node = Node(
        package='task_selector',
        executable='ex_basic_task'
    )

    ex_morning_task_node: Node = Node(
        package='task_selector',
        executable='ex_morning_task'
    )

    return LaunchDescription([
        requestor_node,
        ex_request_client_node,
        ex_timed_task_node,
        ex_basic_task_node,
        ex_morning_task_node
    ])
