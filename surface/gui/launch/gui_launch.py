from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """Asynchronously launches gui node."""
    gui_node: Node = Node(
        package='gui',
        executable='run_app',
        parameters=[
                {'theme': LaunchConfiguration('theme', default='')}]
    )

    return LaunchDescription([gui_node])
