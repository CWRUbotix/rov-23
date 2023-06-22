from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches flood_warning node
    flood_warning_node: Node = Node(
        package='flood_warning',
        executable='flood_warning',
        remappings=[("/pi/flood_status", "/flood_status")]
    )

    return LaunchDescription([flood_warning_node])
