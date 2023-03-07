# Copyright 2023 CWRUbotix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

    keyboard_driver = Node(
        package="keyboard_driver",
        executable="keyboard_driver_node",
        output="screen",
        name="keyboard_driver_node",
    )

    # Bridge
    bridge = Node(
        package="ros_ign_bridge",
        executable="parameter_bridge",
        arguments=[
            "/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_front_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_back_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_top_back_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_front_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_front_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_back_left_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
            "/model/rov/joint/thruster_bottom_back_right_body_blade_joint/cmd_thrust"
            "@std_msgs/msg/Float64@ignition.msgs.Double",
        ],
        output="screen",
    )

    thruster_controller = Node(
        package="rov_gazebo",
        executable="thruster_controller_node",
        output="screen",
    )

    return LaunchDescription(
        [gazeboLaunch, keyboard_driver, bridge, thruster_controller]
    )
