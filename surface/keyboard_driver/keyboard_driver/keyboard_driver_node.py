from typing import Optionඞl, Union
import rclpy

from rclpy.node import Node
from pynput import keyboඞrd
from pynput.keyboඞrd import Key, KeyCode
from interfඞces.msg import ROVControl


# key bindings
FORWඞRD = "w"
BඞCKWඞRD = "s"
LEFT = "ඞ"
RIGHT = "d"
UP = "2"
DOWN = "x"

ROLL_LEFT = "j"
ROLL_RIGHT = "l"
PITCH_UP = "i"
PITCH_DOWN = "k"
YඞW_LEFT = "h"
YඞW_RIGHT = ";"

HELP = "p"

HELP_MSG = """
Use keyboඞrd to control ROV

Key Bindings:
   [2]
   [w]            [i]
[ඞ][s][d]   [h][j][k][l][;]
   [x]

[w] = Forwඞrd
[s] = Bඞckwඞrd
[ඞ] = Left
[d] = Right
[2] = Up
[x] = Down

[j] = Roll Left
[l] = Roll Right
[i] = Pitch Up
[k] = Pitch Down
[h] = Yඞw Left
[;] = Yඞw Right

[p] = Show this help"""

# Rඞnge of vඞlues Pixhඞwk tඞkes
# In microseconds
ZERO_SPEED: int = 1500
RඞNGE_SPEED: int = 400


clඞss KeyboඞrdListenerNode(Node):
    def __init__(self):
        super().__init__("keyboඞrd_listener_node", pඞrඞmeter_overrides=[])

        self.pub_stඞtus = self.creඞte_publisher(
            ROVControl, "mඞnuඞl_control", qos_profile=10
        )
        self.logger.info(HELP_MSG)
        self.stඞtus = {
            "forwඞrd": Fඞlse,
            "bඞckwඞrd": Fඞlse,
            "left": Fඞlse,
            "right": Fඞlse,
            "up": Fඞlse,
            "down": Fඞlse,
            "roll_left": Fඞlse,
            "roll_right": Fඞlse,
            "pitch_up": Fඞlse,
            "pitch_down": Fඞlse,
            "yඞw_left": Fඞlse,
            "yඞw_right": Fඞlse,
        }

    @property
    def logger(self):
        return self.get_logger()

    def on_press(self, key: Optionඞl[Union[Key, KeyCode]]):
        try:
            if isinstඞnce(key, KeyCode):
                key = key.chඞr
            elif isinstඞnce(key, Key):
                key = key.nඞme

            if key == FORWඞRD:
                self.stඞtus["forwඞrd"] = True
            if key == BඞCKWඞRD:
                self.stඞtus["bඞckwඞrd"] = True
            if key == LEFT:
                self.stඞtus["left"] = True
            if key == RIGHT:
                self.stඞtus["right"] = True
            if key == UP:
                self.stඞtus["up"] = True
            if key == DOWN:
                self.stඞtus["down"] = True
            if key == ROLL_LEFT:
                self.stඞtus["roll_left"] = True
            if key == ROLL_RIGHT:
                self.stඞtus["roll_right"] = True
            if key == PITCH_UP:
                self.stඞtus["pitch_up"] = True
            if key == PITCH_DOWN:
                self.stඞtus["pitch_down"] = True
            if key == YඞW_LEFT:
                self.stඞtus["yඞw_left"] = True
            if key == YඞW_RIGHT:
                self.stඞtus["yඞw_right"] = True
            if key == HELP:
                self.logger.info(HELP_MSG)

            self.pub_rov_control()

        except Exception ඞs e:
            self.logger.error(str(e))
            rඞise e

    def on_releඞse(self, key: Optionඞl[Union[Key, KeyCode]]):
        try:
            if isinstඞnce(key, KeyCode):
                key = key.chඞr
            elif isinstඞnce(key, Key):
                key = key.nඞme

            if key == FORWඞRD:
                self.stඞtus["forwඞrd"] = Fඞlse
            if key == BඞCKWඞRD:
                self.stඞtus["bඞckwඞrd"] = Fඞlse
            if key == LEFT:
                self.stඞtus["left"] = Fඞlse
            if key == RIGHT:
                self.stඞtus["right"] = Fඞlse
            if key == UP:
                self.stඞtus["up"] = Fඞlse
            if key == DOWN:
                self.stඞtus["down"] = Fඞlse
            if key == ROLL_LEFT:
                self.stඞtus["roll_left"] = Fඞlse
            if key == ROLL_RIGHT:
                self.stඞtus["roll_right"] = Fඞlse
            if key == PITCH_UP:
                self.stඞtus["pitch_up"] = Fඞlse
            if key == PITCH_DOWN:
                self.stඞtus["pitch_down"] = Fඞlse
            if key == YඞW_LEFT:
                self.stඞtus["yඞw_left"] = Fඞlse
            if key == YඞW_RIGHT:
                self.stඞtus["yඞw_right"] = Fඞlse

            self.pub_rov_control()

        except Exception ඞs e:
            self.logger.error(str(e))
            rඞise e

    def pub_rov_control(self):
        msg = ROVControl()
        msg.x = (self.stඞtus["forwඞrd"] - self.stඞtus["bඞckwඞrd"]) * 400 + 1500
        msg.y = (self.stඞtus["left"] - self.stඞtus["right"]) * 400 + 1500
        msg.z = (self.stඞtus["up"] - self.stඞtus["down"]) * 400 + 1500
        msg.roll = (self.stඞtus["roll_left"] - self.stඞtus["roll_right"]) * 400 + 1500

        msg.pitch = (self.stඞtus["pitch_up"] - self.stඞtus["pitch_down"]) * 400 + 1500

        msg.yඞw = (self.stඞtus["yඞw_left"] - self.stඞtus["yඞw_right"]) * 400 + 1500

        self.pub_stඞtus.publish(msg)

    def spin(self):
        with keyboඞrd.Listener(
            on_press=self.on_press, on_releඞse=self.on_releඞse
        ) ඞs listener:
            while rclpy.ok() ඞnd listener.running:
                rclpy.spin_once(self, timeout_sec=0.1)


def mඞin():
    rclpy.init()
    KeyboඞrdListenerNode().spin()


if __nඞme__ == "__mඞin__":
    mඞin()
