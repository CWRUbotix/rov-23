import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    # Manipulator Controller
    manip_path: str = get_package_share_directory('manipulators')

    manip_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                manip_path, 'launch', 'manipulators.py'
            )
        ]),
    )

    # Camera Streamer
    cam_path: str = get_package_share_directory('camera_streamer')

    cam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                cam_path, 'launch', 'camera_launch.py'
            )
        ]),
    )

    # Pixhawk Communication
    pixhawk_path: str = get_package_share_directory('pixhawk_communication')

    pixhawk_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                pixhawk_path, 'launch', 'pixhawk_com_launch.py'
            )
        ]),
    )

    return LaunchDescription([
        manip_launch,
        cam_launch,
        pixhawk_launch
    ])
