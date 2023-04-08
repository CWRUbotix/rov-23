import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory("manipulators"),
        "config",
        "manip_params.yaml"
        )

    manip_node = Node(
        package="manipulators",
        executable="manipulator",
        name="manip_params",
        parameters=[config]
    )

    ld.add_action(manip_node)
    return ld
