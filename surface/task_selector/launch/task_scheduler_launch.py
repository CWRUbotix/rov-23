from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches main task scheduler
    requestor_node: Node = Node(
        package='task_selector',
        executable='requestor'
    )

    # JoyToHawk
    manual_control_node: Node = Node(
        package='task_selector',
        executable='manual_control_node'
    )

    # example of node requesting tasks
    ex_request_client_node: Node = Node(
        package='task_selector',
        executable='ex_request_client'
    )

    # # example task- run a 10 second timer
    # ex_timed_task_node: Node = Node(
    #     package='task_selector',
    #     executable='ex_timed_task'
    # )

    # # example task- say the task is finished
    # ex_basic_task_node: Node = Node(
    #     package='task_selector',
    #     executable='ex_basic_task'
    # )

    # example task- say good morning
    ex_morning_task_node: Node = Node(
        package='task_selector',
        executable='ex_morning_task'
    )

    return LaunchDescription([
        requestor_node,
        manual_control_node,
        ex_request_client_node,
        # ex_timed_task_node,
        # ex_basic_task_node,
        ex_morning_task_node
    ])
