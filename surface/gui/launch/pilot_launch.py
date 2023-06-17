from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """Asynchronously launches pilot's gui node."""
    gui_node: Node = Node(
        package='gui',
        executable='run_pilot',
        parameters=[
                {'theme': LaunchConfiguration('theme', default='')}],
        remappings=[("/surface/gui/armed", "/armed"),
                    ("/surface/gui/camera_switch", "/surface/camera_switch")]
    )

    return LaunchDescription([gui_node])
