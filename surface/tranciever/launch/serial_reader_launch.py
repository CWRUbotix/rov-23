from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches main task scheduler
    reader_node: Node = Node(
        package='tranciever',
        executable='selector'
    )

    return LaunchDescription([
        reader_node
    ])
