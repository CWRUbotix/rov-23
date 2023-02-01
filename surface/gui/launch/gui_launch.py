import launch
from launch_ros.actions import Node


def generate_launch_description():
    """Asynchronously launches gui node."""
    gui_node: Node = Node(
        package='gui',
        executable='run_gui'
    )

    return launch.LaunchDescription([gui_node])
