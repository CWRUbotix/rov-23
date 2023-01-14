import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher(Node):
  def __init__(self):
    super().__init__('image_publisher')
    
    self.publisher = self.create_publisher(Image, 'video_frames', 10)
    
    timer_period = 0.033
    
    self.timer = self.create_timer(timer_period, self.timer_callback)
    
    self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    
    # Used to convert between ROS and OpenCV images
    self.bridge = CvBridge()
    
  def timer_callback(self):
    ret, frame = self.cap.read()
    
    if ret == True:
        self.publisher.publish(self.bridge.cv2_to_imgmsg(frame))
        self.get_logger().info('Publishing video frame')

def main(args=None):
    rclpy.init(args=args)
    
    image_publisher = ImagePublisher()
    
    rclpy.spin(image_publisher)


if __name__ == '__main__':
    main()
