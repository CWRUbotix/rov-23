import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="keyboard_driver",
                executable="keyboard_driver_node",
                output="screen",
                name="keyboard_driver_node",
            ),
        ]
    )
