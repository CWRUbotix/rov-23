import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    surface_path: str = get_package_share_directory('surface_main')

    pilot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                surface_path, 'launch', 'surface_pilot_launch.py'
            )
        ]),
    )

    operator_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                surface_path, 'launch', 'surface_operator_launch.py'
            )
        ]),
    )

    return LaunchDescription([
        pilot_launch,
        operator_launch,
    ])
