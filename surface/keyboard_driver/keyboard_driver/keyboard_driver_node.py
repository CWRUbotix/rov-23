from typing import Union
import rclpy

from rclpy.node import Node
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from rov_interfaces.msg import ROVControl


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

# Range of values Pixhawk takes
# In microseconds
ZERO_SPEED: int = 1500
RANGE_SPEED: int = 400


class keyboardListenerNode(Node):
    def __init__(self):
        super().__init__("keyboard_listener_node", parameter_overrides=[])

        self.pub_status = self.create_publisher(
            ROVControl, "manual_control", qos_profile=10
        )
        self.logger.info(HELP_MSG)

    @property
    def logger(self):
        return self.get_logger()

    def on_press(self, key: Union[Key, KeyCode, None]):
        self.keypress_helper(key)

    def on_release(self, key: Union[Key, KeyCode, None]):
        self.pub_status.publish(ROVControl())

    # Can only handle one key at a time
    def keypress_helper(self, key: Union[Key, KeyCode, None]):
        try:
            if key is None:
                return

            if isinstance(key, KeyCode):
                key_string = key.char
                if key_string is None:
                    return
            else:  # Is type Key
                key_string = key.name

            status = ROVControl()

            if key_string == FORWARD:
                status.x = ZERO_SPEED + RANGE_SPEED
            elif key_string == BACKWARD:
                status.x = ZERO_SPEED - RANGE_SPEED
            elif key_string == LEFT:
                status.y = ZERO_SPEED + RANGE_SPEED
            elif key_string == RIGHT:
                status.y = ZERO_SPEED - RANGE_SPEED
            elif key_string == UP:
                status.z = ZERO_SPEED + RANGE_SPEED
            elif key_string == DOWN:
                status.z = ZERO_SPEED - RANGE_SPEED
            elif key_string == ROLL_LEFT:
                status.roll = ZERO_SPEED + RANGE_SPEED
            elif key_string == ROLL_RIGHT:
                status.roll = ZERO_SPEED - RANGE_SPEED
            elif key_string == PITCH_UP:
                status.pitch = ZERO_SPEED + RANGE_SPEED
            elif key_string == PITCH_DOWN:
                status.pitch = ZERO_SPEED - RANGE_SPEED
            elif key_string == YAW_LEFT:
                status.yaw = ZERO_SPEED + RANGE_SPEED
            elif key_string == YAW_RIGHT:
                status.yaw = ZERO_SPEED - RANGE_SPEED

            self.pub_status.publish(status)

        except Exception as e:
            self.logger.error(str(e))
            raise

    def spin(self):
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            while rclpy.ok() and listener.running:
                rclpy.spin_once(self, timeout_sec=0.1)


def main():
    rclpy.init()
    keyboardListenerNode().spin()


if __name__ == "__main__":
    main()
