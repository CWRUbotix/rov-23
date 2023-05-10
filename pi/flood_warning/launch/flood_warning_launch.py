from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches flood_warning node
    pixhawk_com_node: Node = Node(
        package='flood_warning',
        executable='flood_warning',
    )

    return LaunchDescription([pixhawk_com_node])
