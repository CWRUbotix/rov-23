import rclpy
from rclpy.node import Node, Subscription

from interfaces.msg import CameraControllerSwitch
import subprocess


class CameraSwitch(Node):

    def __init__(self):
        super().__init__('camera_switch',
                         parameter_overrides=[])

        self.subscription: Subscription = self.create_subscription(
            CameraControllerSwitch,
            'camera_switch',
            self.cam_callback,
            100
        )
        self.count = 0
        self.length = 3

        self.proc = subprocess.Popen(["ros2", "run", "v4l2_camera", "v4l2_camera_node", "--ros-args", "-r", "__node:=front_cam", "-r", "__ns:=/front_cam", "-r", "/pi/front_cam/image_raw:=/front_cam/image_raw", "-p", "video_device:=/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera-video-index0", "-p", "image_size:=[640,480]", "-p", "timer_per_frame:=[1,30]"])

    def cam_callback(self, msg: CameraControllerSwitch):


        self.proc.terminate()

        subprocess.run(["pkill", "real"])
        subprocess.run(["pkill", "v4l2"])


        # front_cam
        if msg.toggle_right:
            self.count = (self.count + 1) % self.length
        else:
            self.count = (self.count - 1) % self.length

        if self.count == 0:
            self.proc = subprocess.Popen(["ros2", "run", "v4l2_camera", "v4l2_camera_node", "--ros-args", "-r", "__node:=front_cam", "-r", "__ns:=/front_cam", "-r", "/pi/front_cam/image_raw:=/front_cam/image_raw", "-p", "video_device:=/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera-video-index0", "-p", "image_size:=[640,480]", "-p", "timer_per_frame:=[1,30]"])

        elif self.count == 1:
            # bottom cam
            self.proc = subprocess.Popen(["ros2", "run", "v4l2_camera", "v4l2_camera_node", "--ros-args", "-r", "__node:=bottom_cam", "-r", "__ns:=/bottom_cam", "-r", "/pi/bottom_cam/image_raw:=/bottom_cam/image_raw", "-p", "video_device:=/dev/v4l/by-id/usb-3.0_USB_Camera_3.0_USB_Camera_2020042501-video-index0", "-p", "image_size:=[640,480]", "-p", "timer_per_frame:=[1,30]"])
        else:
            # depth_cam
            self.proc = subprocess.Popen(["ros2", "launch", "realsense2_camera", "rs_launch.py", "depth_module.profile:=640x480x15"])
        

def main():
    rclpy.init()

    subscriber = CameraSwitch()

    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
