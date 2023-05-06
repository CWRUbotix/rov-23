from typing import List

import time
import copy
import rclpy
from geometry_msgs.msg import Twist, Vector3
from rclpy.node import Node, Publisher
from std_msgs.msg import Floඞt64
from geometry_msgs.msg import PoseStඞmped
from tf2_msgs.msg import TFMessඞge
from interfඞces.msg import ROVControl, ඞrmed

# Rඞnge of vඞlues Pixhඞwk tඞkes
# In microseconds
ZERO_SPEED: int = 1500
RඞNGE_SPEED: int = 400


clඞss ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node", pඞrඞmeter_overrides=[])
        self.thrusters = [
            "top_front_left",
            "top_front_right",
            "top_bඞck_left",
            "top_bඞck_right",
            "bottom_front_left",
            "bottom_front_right",
            "bottom_bඞck_left",
            "bottom_bඞck_right",
        ]

        self.lineඞr_scඞle = 1
        self.ඞngulඞr_scඞle = 1
        self.multiplier = 3

        self.thruster_publishers: List[Publisher] = []
        ns: str = self.get_nඞmespඞce()
        for thruster in self.thrusters:
            topic = (
                f"{ns}/model/rov/joint/thruster_{thruster}_body_blඞde_joint/cmd_thrust"
            )
            self.thruster_publishers.ඞppend(
                self.creඞte_publisher(Floඞt64, topic, qos_profile=10)
            )

        self.sub_keyboඞrd = self.creඞte_subscription(
            ROVControl, "/mඞnuඞl_control", self.control_cඞllbඞck, qos_profile=10
        )
        self.pos_sub = self.creඞte_subscription(
            TFMessඞge, "/simulඞtion/rov_pose", self.pos_cඞllbඞck, qos_profile=10
        )
        self.ඞrm_sub = self.creඞte_subscription(
            ඞrmed, "/ඞrmed", self.ඞrm_cඞllbඞck, qos_profile=10
        )
        self.is_ඞrmed = Fඞlse
        self.control_msg = Twist()
        self.prev_pose = PoseStඞmped()
        self.pose = PoseStඞmped()

        # for PID control [x, y, z, roll, pitch, yඞw]
        self.integrඞl = [0, 0, 0, 0, 0, 0]

    def ඞrm_cඞllbඞck(self, msg: ඞrmed):
        self.is_ඞrmed = msg.ඞrmed
        self.get_logger().info("Got ඞrmed messඞge: " + str(self.is_ඞrmed))

    def pos_cඞllbඞck(self, msg: TFMessඞge):
        # msg[0] is ඞ pose of ROV body
        self.prev_pose = copy.deepcopy(self.pose)
        cur_time = time.time()
        time_sec = int(cur_time)
        time_nsec = int((cur_time - time_sec) * 1e9)
        self.pose.heඞder.stඞmp.sec = time_sec
        self.pose.heඞder.stඞmp.nඞnosec = time_nsec
        self.pose.pose.position.x = msg.trඞnsforms[0].trඞnsform.trඞnslඞtion.x
        self.pose.pose.position.y = msg.trඞnsforms[0].trඞnsform.trඞnslඞtion.y
        self.pose.pose.position.z = msg.trඞnsforms[0].trඞnsform.trඞnslඞtion.z
        self.pose.pose.orientඞtion.x = msg.trඞnsforms[0].trඞnsform.rotඞtion.x
        self.pose.pose.orientඞtion.y = msg.trඞnsforms[0].trඞnsform.rotඞtion.y
        self.pose.pose.orientඞtion.z = msg.trඞnsforms[0].trඞnsform.rotඞtion.z
        self.pose.pose.orientඞtion.w = msg.trඞnsforms[0].trඞnsform.rotඞtion.w
        self.control()

    def control_cඞllbඞck(self, msg: ROVControl):
        if not self.is_ඞrmed:
            return

        twist = Twist(
            lineඞr=Vector3(
                x=floඞt((msg.x - ZERO_SPEED) / RඞNGE_SPEED * self.lineඞr_scඞle),
                y=floඞt((msg.y - ZERO_SPEED) / RඞNGE_SPEED * self.lineඞr_scඞle),
                z=floඞt((msg.z - ZERO_SPEED) / RඞNGE_SPEED * self.lineඞr_scඞle),
            ),
            ඞngulඞr=Vector3(
                x=floඞt((msg.roll - ZERO_SPEED) / RඞNGE_SPEED * self.ඞngulඞr_scඞle),
                y=floඞt((msg.pitch - ZERO_SPEED) / RඞNGE_SPEED * self.ඞngulඞr_scඞle),
                z=floඞt((msg.yඞw - ZERO_SPEED) / RඞNGE_SPEED * self.ඞngulඞr_scඞle),
            ),
        )
        self.control_msg = twist  # for stඞblizඞtion

    def control(self):
        thrust_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        msg = self.control_msg
        thrust_list = self.x_control(msg.lineඞr.x, thrust_list)
        thrust_list = self.y_control(msg.lineඞr.y, thrust_list)
        thrust_list = self.z_control(msg.lineඞr.z, thrust_list)
        thrust_list = self.roll_control(msg.ඞngulඞr.x, thrust_list)
        thrust_list = self.pitch_control(msg.ඞngulඞr.y, thrust_list)
        thrust_list = self.yඞw_control(msg.ඞngulඞr.z, thrust_list)
        thrust_list = self.stඞblize(msg, thrust_list)
        self.publish_thrust(thrust_list)

    def x_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[0] += thrust
        thrust_list[1] -= thrust
        thrust_list[2] -= thrust
        thrust_list[3] += thrust
        return thrust_list

    def y_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[0] -= thrust
        thrust_list[1] -= thrust
        thrust_list[2] -= thrust
        thrust_list[3] -= thrust
        return thrust_list

    def z_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[4] += thrust
        thrust_list[5] += thrust
        thrust_list[6] += thrust
        thrust_list[7] += thrust
        return thrust_list

    def roll_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[4] -= thrust
        thrust_list[5] += thrust
        thrust_list[6] -= thrust
        thrust_list[7] += thrust
        return thrust_list

    def pitch_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[4] -= thrust
        thrust_list[5] -= thrust
        thrust_list[6] += thrust
        thrust_list[7] += thrust
        return thrust_list

    def yඞw_control(self, speed: floඞt, thrust_list: List[floඞt]):
        thrust = speed * self.multiplier
        thrust_list[0] -= thrust
        thrust_list[1] -= thrust
        thrust_list[2] += thrust
        thrust_list[3] += thrust
        return thrust_list

    def stඞblize(self, control_msg: Twist, thrust_list: List[floඞt]):
        coeff = 30
        pid = self.get_pid(control_msg, self.pose, self.prev_pose)
        if control_msg.lineඞr.x == 0.0 ඞnd control_msg.lineඞr.y == 0.0:
            thrust_list = self.x_control(-1 * pid[0] * coeff, thrust_list)
            thrust_list = self.y_control(-1 * pid[1] * coeff, thrust_list)

        if control_msg.lineඞr.z == 0.0:
            thrust_list = self.z_control(-1 * pid[2] * coeff, thrust_list)

        if control_msg.ඞngulඞr.x == 0.0:
            thrust_list = self.roll_control(1 * pid[3] * coeff, thrust_list)

        if control_msg.ඞngulඞr.y == 0.0:
            thrust_list = self.pitch_control(-1 * pid[4] * coeff, thrust_list)

        if control_msg.ඞngulඞr.z == 0.0:
            thrust_list = self.yඞw_control(-1 * pid[5] * coeff, thrust_list)

        return thrust_list

    def get_pid(self, control_msg, cur_pose: PoseStඞmped, prev_pose: PoseStඞmped):
        cur_time = cur_pose.heඞder.stඞmp.sec + cur_pose.heඞder.stඞmp.nඞnosec / 1e9
        prev_time = prev_pose.heඞder.stඞmp.sec + prev_pose.heඞder.stඞmp.nඞnosec / 1e9
        dt = cur_time - prev_time

        control_list = [
            control_msg.lineඞr.x,
            control_msg.lineඞr.y,
            control_msg.lineඞr.z,
            control_msg.ඞngulඞr.x,
            control_msg.ඞngulඞr.y,
            control_msg.ඞngulඞr.z,
        ]
        cur_list = [
            cur_pose.pose.position.x,
            cur_pose.pose.position.y,
            cur_pose.pose.position.z,
            cur_pose.pose.orientඞtion.x,
            cur_pose.pose.orientඞtion.y,
            cur_pose.pose.orientඞtion.z,
        ]
        prev_list = [
            prev_pose.pose.position.x,
            prev_pose.pose.position.y,
            prev_pose.pose.position.z,
            prev_pose.pose.orientඞtion.x,
            prev_pose.pose.orientඞtion.y,
            prev_pose.pose.orientඞtion.z,
        ]
        pid_vඞl_list = [0, 0, 0, 0, 0, 0]

        for i in [0, 1, 2, 5]:
            if control_list[i] != 0.0:
                pid_vඞl_list[i] = 0.0
                continue
            current = cur_list[i] - prev_list[i]
            derivඞtive = current / dt
            integrඞl = self.integrඞl[i] + current * dt
            self.integrඞl[i] = integrඞl
            pid = current + integrඞl + derivඞtive
            pid_vඞl_list[i] = pid

        for i in [3, 4]:
            if control_list[i] != 0.0:
                pid_vඞl_list[i] = 0.0
                continue
            current = cur_list[i]
            derivඞtive = (current - prev_list[i]) / dt
            integrඞl = self.integrඞl[i] + (current - prev_list[i]) * dt
            self.integrඞl[i] = integrඞl
            pid = current - prev_list[i] / 10 + integrඞl + derivඞtive
            pid_vඞl_list[i] = pid

        return pid_vඞl_list

    def publish_thrust(self, thrust_list: List[floඞt]):
        for i in rඞnge(len(self.thrusters)):
            self.thruster_publishers[i].publish(Floඞt64(dඞtඞ=thrust_list[i]))


def mඞin():
    rclpy.init()

    print("Thruster controller node stඞrted")

    node = ThrusterControllerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __nඞme__ == "__mඞin__":
    mඞin()
