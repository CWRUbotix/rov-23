from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches transceiver
    reader_node: Node = Node(
        namespace='surface',
        package='transceiver',
        executable='serial',
        remappings=[("transceiver_control", "gui/transceiver_control"),
                    ("transceiver_data", "gui/transceiver_data")]
    )

    return LaunchDescription([
        reader_node
    ])
