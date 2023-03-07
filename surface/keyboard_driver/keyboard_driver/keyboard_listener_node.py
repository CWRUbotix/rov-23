import sys

# pynput throws an error if we import it before $DISPLAY is set on LINUX
from pynput.keyboard import KeyCode

if sys.platform not in ("darwin", "win32"):
    import os

    os.environ.setdefault("DISPLAY", ":0")

from pynput import keyboard

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class keyboardListenerNode(Node):
    def __init__(self):
        super().__init__("keyboard_listener_node")
        self.pub_code = self.create_publisher(String, "key_pressed", qos_profile=10)

    def spin(self):
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            while rclpy.ok() and listener.running:
                rclpy.spin_once(self, timeout_sec=0.1)

    @property
    def logger(self):
        return self.get_logger()

    def on_release(self, key):
        # todo: implement this
        pass

    def on_press(self, key):
        try:
            if type(key) == KeyCode:
                key = key.char
            elif type(key) == keyboard.Key:
                key = key.name

            self.logger.info("pressed " + key)
            self.pub_code.publish(String(data=key))
        except Exception as e:
            self.logger.error(str(e))
            raise


def main(args=None):
    rclpy.init(args=args)
    keyboardListenerNode().spin()


if __name__ == "__main__":
    main()
