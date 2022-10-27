from ast import arg, arguments
import os
from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_share_path

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.substitutions import Command
from launch_ros.descriptions import ParameterValue
def generate_launch_description():
    
    # Launches Gazebo
    gazeboLaunch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py'
            )
        ])
    )

    filename = "rov.xacro"

    # Path to Xacro file of robot
    path_to_urdf= os.path.join(get_package_share_directory('rov_description'),'urdf',filename)


    with open(path_to_urdf, 'r') as infp:
        robot_desc = infp.read()


    robot_desc = ParameterValue(
            Command(['xacro ', str(path_to_urdf)]), value_type=str
        )

    params = {
            'robot_description': robot_desc
    }

    # Publishes the state of the robot
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[params],
        arguments=[path_to_urdf] 
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        arguments=[path_to_urdf]
    )

    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity','rov',
            '-topic','/robot_description',
            '-x', '1',
            '-y', '1',
            '-z', '1',
        ]
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d' + os.path.join(get_package_share_directory('rov_gazebo'), 'config', 'rov.rviz')],

    )

    return LaunchDescription([
        gazeboLaunch,
        robot_state_publisher_node,
        #joint_state_publisher_node,
        spawn_entity_node,
        rviz,
    ]

    )