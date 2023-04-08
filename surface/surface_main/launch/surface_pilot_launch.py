import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    gui_path: str = get_package_share_directory('gui')
    controller_path: str = get_package_share_directory('ps5_controller')
    # Launches Gui
    gui_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                gui_path, 'launch', 'pilot_launch.py'
            )
        ]),
    )

    # Launches Controller
    controller_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                controller_path, 'launch', 'controller_launch.py'
            )
        ]),
    )

    return LaunchDescription([
        gui_launch,
        controller_launch,
    ])
