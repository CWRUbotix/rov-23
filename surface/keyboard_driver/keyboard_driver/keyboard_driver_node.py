import rclpy

from rclpy.node import Node
from pynput import keyboard
from interfaces.msg import KeyboardStatus
from geometry_msgs.msg import Twist, Vector3


# key bindings
FORWARD = "w"
BACKWARD = "s"
LEFT = "a"
RIGHT = "d"
UP = "2"
DOWN = "x"

ROLL_LEFT = "j"
ROLL_RIGHT = "l"
PITCH_UP = "i"
PITCH_DOWN = "k"
YAW_LEFT = "h"
YAW_RIGHT = ";"

HELP = "p"

HELP_MSG = """
Use keyboard to control ROV

Key Bindings:
   [2]
   [w]            [i]
[a][s][d]   [h][j][k][l][;]
   [x]

[w] = Forward
[s] = Backward
[a] = Left
[d] = Right
[2] = Up
[x] = Down

[j] = Roll Left
[l] = Roll Right
[i] = Pitch Up
[k] = Pitch Down
[h] = Yaw Left
[;] = Yaw Right

[p] = Show this help"""


class keyboardListenerNode(Node):
    def __init__(self):
        super().__init__("keyboard_listener_node")
        self.status = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "roll_left": False,
            "roll_right": False,
            "pitch_up": False,
            "pitch_down": False,
            "yaw_left": False,
            "yaw_right": False,
        }
        self.pub_status = self.create_publisher(
            KeyboardStatus, "keyboard_status", qos_profile=10
        )
        self.pub_twist = self.create_publisher(Twist, "cmd_vel", qos_profile=10)
        self.tmr_twist = self.create_timer(0.1, self.on_tmr)
        self.linear_scale = 1
        self.angular_scale = 1
        self.logger.info(HELP_MSG)

    def on_tmr(self):
        twist = Twist(
            linear=Vector3(
                x=float(
                    (self.status["forward"] - self.status["backward"])
                    * self.linear_scale
                ),
                y=float(
                    (self.status["left"] - self.status["right"]) * self.linear_scale
                ),
                z=float((self.status["up"] - self.status["down"]) * self.linear_scale),
            ),
            angular=Vector3(
                x=float(
                    (self.status["roll_right"] - self.status["roll_left"])
                    * self.angular_scale
                ),
                y=float(
                    (self.status["pitch_down"] - self.status["pitch_up"])
                    * self.angular_scale
                ),
                z=float(
                    (self.status["yaw_left"] - self.status["yaw_right"])
                    * self.angular_scale
                ),
            ),
        )
        self.pub_twist.publish(twist)

    @property
    def logger(self):
        return self.get_logger()

    def on_press(self, key):
        try:
            if type(key) == keyboard.KeyCode:
                key = key.char
            elif type(key) == keyboard.Key:
                key = key.name

            if key == FORWARD:
                self.status["forward"] = True
            if key == BACKWARD:
                self.status["backward"] = True
            if key == LEFT:
                self.status["left"] = True
            if key == RIGHT:
                self.status["right"] = True
            if key == UP:
                self.status["up"] = True
            if key == DOWN:
                self.status["down"] = True
            if key == ROLL_LEFT:
                self.status["roll_left"] = True
            if key == ROLL_RIGHT:
                self.status["roll_right"] = True
            if key == PITCH_UP:
                self.status["pitch_up"] = True
            if key == PITCH_DOWN:
                self.status["pitch_down"] = True
            if key == YAW_LEFT:
                self.status["yaw_left"] = True
            if key == YAW_RIGHT:
                self.status["yaw_right"] = True
            if key == HELP:
                self.logger.info(HELP_MSG)

            self.pub_status.publish(KeyboardStatus(**self.status))

        except Exception as e:
            self.logger.error(str(e))
            raise

    def on_release(self, key):
        try:
            if type(key) == keyboard.KeyCode:
                key = key.char
            elif type(key) == keyboard.Key:
                key = key.name

            if key == FORWARD:
                self.status["forward"] = False
            if key == BACKWARD:
                self.status["backward"] = False
            if key == LEFT:
                self.status["left"] = False
            if key == RIGHT:
                self.status["right"] = False
            if key == UP:
                self.status["up"] = False
            if key == DOWN:
                self.status["down"] = False
            if key == ROLL_LEFT:
                self.status["roll_left"] = False
            if key == ROLL_RIGHT:
                self.status["roll_right"] = False
            if key == PITCH_UP:
                self.status["pitch_up"] = False
            if key == PITCH_DOWN:
                self.status["pitch_down"] = False
            if key == YAW_LEFT:
                self.status["yaw_left"] = False
            if key == YAW_RIGHT:
                self.status["yaw_right"] = False

            self.pub_status.publish(KeyboardStatus(**self.status))

        except Exception as e:
            self.logger.error(str(e))
            raise

    def spin(self):
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            while rclpy.ok() and listener.running:
                rclpy.spin_once(self, timeout_sec=0.1)


def main(args=None):
    rclpy.init(args=args)
    keyboardListenerNode().spin()


if __name__ == "__main__":
    main()
