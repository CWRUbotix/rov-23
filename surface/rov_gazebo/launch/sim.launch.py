import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    rov_gazebo_path: str = get_package_share_directory("rov_gazebo")
    ros_ign_gazebo_path: str = get_package_share_directory("ros_ign_gazebo")

    world_path: str = os.path.join(rov_gazebo_path, "worlds", "rov_in_world.sdf")

    # Launches Gazebo
    gazeboLaunch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(ros_ign_gazebo_path, "launch", "ign_gazebo.launch.py")]
        ),
        launch_arguments={"ign_args": world_path}.items(),
    )

    # Launches the keyboard controller
    teleop_twist_keyboard = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        output="screen",
        prefix="xterm -e",
    )

    # Bridge
    bridge = Node(
        package="ros_ign_bridge",
        executable="parameter_bridge",
        arguments=[
            "/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_force@std_msgs/msg/Float64@ignition.msgs.Double",
        ],
        output="screen",
    )

    return LaunchDescription([gazeboLaunch, teleop_twist_keyboard, bridge])
