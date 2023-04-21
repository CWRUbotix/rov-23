from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    flood_node = Node(
        package="flood_warning",
        executable="flood_warning"
    )

    ld.add_action(flood_node)
    return ld
