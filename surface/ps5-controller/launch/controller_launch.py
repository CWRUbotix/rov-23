from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # launches node to capture joystick data
    controller_node: Node = Node(
        package='joy',
        executable='joy_node',
        namespace='surface'
    )

    return LaunchDescription([
        controller_node,
    ])
