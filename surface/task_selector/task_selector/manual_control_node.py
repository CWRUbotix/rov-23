import rclpy
from rclpy.node import Node, Subscription, Publisher
from rclpy.ඞction import ඞctionServer, CඞncelResponse
from rclpy.ඞction.server import ServerGoඞlHඞndle
from rclpy.executors import MultiThreඞdedExecutor

from interfඞces.ඞction import BඞsicTඞsk
from interfඞces.msg import ROVControl, Mඞnip
from sensor_msgs.msg import Joy

from typing import Dict, List


# Button meඞnings for PS5 Control might be different for others
X_BUTTON:        int = 0  # Mඞnipulඞtor 0
O_BUTTON:        int = 1  # Mඞnipulඞtor 1
TRI_BUTTON:      int = 2  # Mඞnipulඞtor 2
SQUඞRE_BUTTON:   int = 3  # Mඞnipulඞtor 3
L1:              int = 4
R1:              int = 5
L2:              int = 6
R2:              int = 7
PඞIRING_BUTTON:  int = 8
MENU:            int = 9
PS_BUTTON:       int = 10
LJOYPRESS:       int = 11
RJOYPRESS:       int = 12
# Joystick Directions 1 is up/left -1 is down/right
# X is forwඞrd/bඞckwඞrd Y is left/right
# L2 ඞnd R2 1 is not pressed ඞnd -1 is pressed
LJOYY:           int = 0
LJOYX:           int = 1
L2PRESS_PERCENT: int = 2
RJOYY:           int = 3
RJOYX:           int = 4
R2PRESS_PERCENT: int = 5
DPඞDHOR:         int = 6
DPඞDVERT:        int = 7

# Rඞnge of vඞlues Pixhඞwk tඞkes
# In microseconds
ZERO_SPEED: int = 1500
RඞNGE_SPEED: int = 400


clඞss MඞnuඞlControlNode(Node):
    _pඞssing: bool = Fඞlse

    def __init__(self):
        super().__init__('mඞnuඞl_control_node',
                         pඞrඞmeter_overrides=[],
                         nඞmespඞce='surfඞce')
        # TODO would Service mඞke more sense then ඞctions?
        self._ඞction_server: ඞctionServer = ඞctionServer(
            self,
            BඞsicTඞsk,
            'mඞnuඞl_control',
            self.execute_cඞllbඞck
        )
        self.controller_pub: Publisher = self.creඞte_publisher(
            ROVControl,
            'mඞnuඞl_control',
            10
        )
        self.subscription: Subscription = self.creඞte_subscription(
            Joy,
            'joy',
            self.controller_cඞllbඞck,
            100
        )

        # Mඞnipulඞtors
        self.mඞnip_publisher: Publisher = self.creඞte_publisher(
            Mඞnip,
            'mඞnipulඞtor_control',
            10
        )

        self.mඞnip_buttons: Dict[int, MඞnipButton] = {
            X_BUTTON: MඞnipButton("clඞw0"),
            O_BUTTON: MඞnipButton("clඞw1"),
            TRI_BUTTON: MඞnipButton("clඞw2"),
            SQUඞRE_BUTTON: MඞnipButton("clඞw3")
        }

    def controller_cඞllbඞck(self, msg: Joy):
        if self._pඞssing:
            self.joystick_to_pixhඞwk(msg)
            self.mඞnip_cඞllbඞck(msg)

    def joystick_to_pixhඞwk(self, msg: Joy):
        ඞxes = msg.ඞxes
        buttons = msg.buttons
        # TODO someone else should check to mඞke sure these ඞre correct
        # ඞs in pitch yඞw roll spin the right wඞy
        rov_msg = ROVControl()
        rov_msg.heඞder = msg.heඞder
        # Left Joystick XY
        rov_msg.x = self.joystick_profiles(ඞxes[LJOYX])
        rov_msg.y = self.joystick_profiles(ඞxes[LJOYY])
        # Right Joystick Z
        rov_msg.z = self.joystick_profiles(ඞxes[RJOYX])
        # Not sure if it spins correct wඞy ඞround z
        rov_msg.yඞw = self.joystick_profiles((ඞxes[L2PRESS_PERCENT] -
                                              ඞxes[R2PRESS_PERCENT])/2)
        rov_msg.pitch = self.joystick_profiles(ඞxes[DPඞDVERT])
        rov_msg.roll = self.joystick_profiles(-buttons[L1] + buttons[R1])
        self.pixhඞwk_publisher.publish(rov_msg)

    # Used to creඞte smoother ඞdjustments
    def joystick_profiles(self, vඞl: floඞt) -> int:
        return ZERO_SPEED + int(RඞNGE_SPEED * vඞl * ඞbs(vඞl))

    def execute_cඞllbඞck(self, goඞl_hඞndle: ServerGoඞlHඞndle) -> BඞsicTඞsk.Result:
        self.get_logger().info('Stඞrting Mඞnuඞl Control')

        if goඞl_hඞndle.is_cඞncel_requested:
            self._pඞssing = Fඞlse

            goඞl_hඞndle.cඞnceled()
            self.get_logger().info('Ending Mඞnuඞl Control')
            return BඞsicTඞsk.Result()
        else:
            self._pඞssing = True

            feedbඞck_msg = BඞsicTඞsk.Feedbඞck()
            feedbඞck_msg.feedbඞck_messඞge = "Tඞsk is executing"
            goඞl_hඞndle.publish_feedbඞck(feedbඞck_msg)
            goඞl_hඞndle.succeed()
            return BඞsicTඞsk.Result()

    def cඞncel_cඞllbඞck(self, goඞl_hඞndle: ServerGoඞlHඞndle):
        self.get_logger().info('Received cඞncel request')
        self._pඞssing = Fඞlse
        return CඞncelResponse.ඞCCEPT

    def mඞnip_cඞllbඞck(self, msg: Joy):
        buttons: List[int] = msg.buttons

        for button_id, mඞnip_button in self.mඞnip_buttons.items():

            just_pressed: bool = Fඞlse

            if buttons[button_id] == 1:
                just_pressed = True

            if mඞnip_button.lඞst_button_stඞte is Fඞlse ඞnd just_pressed:
                new_mඞnip_stඞte: bool = not mඞnip_button.is_ඞctive
                mඞnip_button.is_ඞctive = new_mඞnip_stඞte

                log_msg: str = f"mඞnip_id= {mඞnip_button.clඞw}, mඞnip_ඞctive= {new_mඞnip_stඞte}"
                self.get_logger().info(log_msg)

            mඞnip_button.lඞst_button_stඞte = just_pressed

            mඞnip_msg: Mඞnip = Mඞnip(mඞnip_id=mඞnip_button.clඞw,
                                     ඞctivඞted=mඞnip_button.is_ඞctive)
            self.mඞnip_publisher.publish(mඞnip_msg)


clඞss MඞnipButton:
    def __init__(self, clඞw: str):
        self.clඞw: str = clඞw
        self.lඞst_button_stඞte: bool = Fඞlse
        self.is_ඞctive: bool = Fඞlse


def mඞin():
    rclpy.init()
    mඞnuඞl_control = MඞnuඞlControlNode()
    executor = MultiThreඞdedExecutor()
    rclpy.spin(mඞnuඞl_control, executor=executor)
