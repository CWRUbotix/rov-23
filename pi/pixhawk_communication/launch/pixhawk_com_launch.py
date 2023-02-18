from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # launches PI to Pixhawk Communicatoni
    pixhawk_com_node: Node = Node(
        package='pixhawk_communication',
        executable='pixhawk_com'
    )

    return LaunchDescription([
        pixhawk_com_node
    ])
