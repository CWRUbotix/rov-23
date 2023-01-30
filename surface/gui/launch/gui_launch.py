import launch
from launch_ros.actions import Node


def generate_launch_description():
    """Asynchronously ROS launch the GUI."""

    gui_node: Node = Node(
        package='gui',
        executable='gui'
    )

    return launch.LaunchDescription([gui_node])
