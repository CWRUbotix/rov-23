import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    realsense_path: str = get_package_share_directory('realsense')

    # Launches Realsense
    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                realsense_path, 'launch', 'realsense_launch.py'
            )
        ]),
    )

    return LaunchDescription([
        realsense_launch,
    ])
