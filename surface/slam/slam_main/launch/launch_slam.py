# Modified from https://github.com/introlab/rtabmap_ros/blob/ros2/launch/ros2/realsense_d400.launch.py

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    parameters = [{
          'frame_id': 'camera_link',
          'subscribe_depth': True,
          'subscribe_odom_info': False,
          'visual_odometry': True,
          'approx_sync': True,
          'approx_sync_max_interval': 0.01}]

    remappings = [
          ('rgb/image', '/camera/color/image_raw'),
          ('rgb/camera_info', '/camera/color/camera_info'),
          ('depth/image', '/camera/aligned_depth_to_color/image_raw')]

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(
                    get_package_share_directory('realsense'), 'launch', 'realsense_launch.py'
                )
            ]),
            launch_arguments={"align_depth.enable": "true"}.items()
        ),

        Node(
            package='rtabmap_ros', executable='rgbd_odometry', output='screen',
            parameters=parameters,
            remappings=remappings,
            # prefix=["xterm -e gdb -ex run --args"]
            ),

        Node(
            package='rtabmap_ros', executable='rtabmap', output='screen',
            parameters=parameters,
            remappings=remappings,
            arguments=['-d']),

        Node(
            package='rtabmap_ros', executable='rtabmapviz', output='screen',
            parameters=parameters,
            remappings=remappings),
    ])
