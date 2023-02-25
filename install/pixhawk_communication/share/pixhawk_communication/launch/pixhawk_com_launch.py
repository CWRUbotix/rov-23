from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    # launches PI to Pixhawk Communication
    pixhawk_com_node: Node = Node(
        package='pixhawk_communication',
        executable='pixhawk_com',
        parameters=[
                {'communication': LaunchConfiguration('communication', default='/dev/ttyPixhawk')}]
    )

    return LaunchDescription([pixhawk_com_node])
