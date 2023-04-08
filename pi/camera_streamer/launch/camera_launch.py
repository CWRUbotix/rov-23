from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    front_cam_node: Node = Node(
        package="usb_cam",
        executable="usb_cam_node_exe",
        namespace="front_cam",
        parameters=[
            {"video_device": "/dev/video0"},
            {"image_width": 640},
            {"image_height": 480},
            {"pixel_format": "mjpeg"}
        ]
    )

    # Launch the front camera node
    # front_cam_node: Node = Node(
    #     package="v4l2_camera",
    #     executable="v4l2_camera_node",
    #     namespace="front_cam",
    #     parameters=[
    #         {"video_device": "/dev/video0"}
    #     ]
    # )

    # Launch the front camera node
    # bottom_cam_node: Node = Node(
    #     package="v4l2_camera",
    #     executable="v4l2_camera_node",
    #     namespace="bottom_cam",
    #     parameters=[
    #         {"video_device": "/dev/video2"}
    #     ]
    # )

    # manip_cam_node: Node = Node(
    #     package="v4l2_camera",
    #     executable="v4l2_camera_node",
    #     namespace="manip_cam",
    #     parameters=[
    #         {"video_device": "/dev/video6"}
    #     ]
    # )

    return LaunchDescription([
        front_cam_node,
        # bottom_cam_node,
        # manip_cam_node
    ])
