from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # Launches Gui
    realsense_node = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node'
    )

    return LaunchDescription([
        realsense_node
    ])
