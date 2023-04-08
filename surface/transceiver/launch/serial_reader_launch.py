from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches tranceiver
    reader_node: Node = Node(
        namespace='surface',
        package='transceiver',
        executable='serial',
        remappings=[("surface/transceiver", "surface/gui/transceiver")]
    )

    return LaunchDescription([
        reader_node
    ])
