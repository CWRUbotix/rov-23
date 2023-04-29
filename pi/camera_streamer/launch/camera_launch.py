from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # USB 3.0
    front_cam_node: Node = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        namespace="front_cam",
        parameters=[
            {"video_device":
             "/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera-video-index0"},
            {"image_size": [640, 480]}
        ]
    )

    # h264 (fisheye)
    bottom_cam_node: Node = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        namespace="bottom_cam",
        parameters=[
            {"video_device":
             "/dev/v4l/by-id/usb-H264_USB_Camera_H264_USB_Camera_2020032801-video-index0"},
            {"image_size": [640, 480]}
        ]
    )

    return LaunchDescription([
        front_cam_node,
        bottom_cam_node
    ])
