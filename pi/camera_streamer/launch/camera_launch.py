from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # Symlinks are auto-generated by V4L2
    # ls /dev/v4l/by-id to see all the available symlinks
    # ls /dev/v4l/by-path for usb slot based symlinks

    # USB 3.0 front (fisheye)
    front_cam_node: Node = Node(
        exec_name="front_cam",
        package="v4l2_camera",
        executable="v4l2_camera_node",
        namespace="front_cam",
        parameters=[
            {"video_device":
             "/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera_2020042501-video-index0"},
            {"image_size": [640, 480]},
            {"time_per_frame": [1, 30]}
        ],
        remappings=[("/pi/front_cam/image_raw", "/front_cam/image_raw")]
    )

    # USB 3.0 bottom
    bottom_cam_node: Node = Node(
        exec_name="bottom_cam",
        package="v4l2_camera",
        executable="v4l2_camera_node",
        namespace="bottom_cam",
        parameters=[
            {"video_device":
             "/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera-video-index0"},
            {"image_size": [640, 480]},
            {"time_per_frame": [1, 30]}
        ],
        remappings=[("/pi/bottom_cam/image_raw", "/bottom_cam/image_raw")]
    )

    return LaunchDescription([
        front_cam_node,
        bottom_cam_node
    ])
