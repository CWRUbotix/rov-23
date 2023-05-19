from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    manip_node = Node(
        package="manipulators",
        executable="manipulator",
        parameters=[
            {"claw0": 0},
            {"claw1": 1},
            {"claw2": 2},
            {"claw3": 3}
        ],
        remappings=[("/pi/manipulator_control", "/manipulator_control")]
    )

    return LaunchDescription([
        manip_node
    ])
