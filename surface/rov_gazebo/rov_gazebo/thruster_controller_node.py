# Copyright 2023 CWRUbotix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist


class ThrusterControllerNode(Node):
    def __init__(self):
        super().__init__("thruster_controller_node")
        self.thrusters = [
            {"location": "top_front_left", "power": 0.0},
            {"location": "top_front_right", "power": 0.0},
            {"location": "top_back_left", "power": 0.0},
            {"location": "top_back_right", "power": 0.0},
            {"location": "bottom_front_left", "power": 0.0},
            {"location": "bottom_front_right", "power": 0.0},
            {"location": "bottom_back_left", "power": 0.0},
            {"location": "bottom_back_right", "power": 0.0},
        ]
        self.xyzrpy = {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
            "roll": 0.0,
            "pitch": 0.0,
            "yaw": 0.0,
        }

        self.publishers_ = []
        self.subscriber_ = self.create_subscription(
            Twist, "/cmd_vel", self.control, qos_profile=10
        )

    def create_publishers(self, msg_type, qos_profile=10):
        for thruster in self.thrusters:
            topic = (
                "model/rov/joint/thruster_"
                + thruster["location"]
                + "_body_blade_joint/cmd_thrust"
            )
            self.publishers_.append(self.create_publisher(msg_type, topic, qos_profile))

    def control(self, msg):
        self.x_control(msg.linear.x)
        self.y_control(msg.linear.y)
        self.z_control(msg.linear.z)
        self.roll_control(msg.angular.x)
        self.pitch_control(msg.angular.y)
        self.yaw_control(msg.angular.z)

    def x_control(self, speed):
        if self.xyzrpy["x"] != speed:
            multiplier = 3
            prev_thruster_input = self.xyzrpy["x"] * multiplier
            thruster_input = speed * multiplier
            diff = thruster_input - prev_thruster_input
            # first: add diff
            self.thrusters[0]["power"] += diff
            # second: subtract diff
            self.thrusters[1]["power"] -= diff
            # third: subtract diff
            self.thrusters[2]["power"] -= diff
            # fourth: add diff
            self.thrusters[3]["power"] += diff

            self.xyzrpy["x"] = speed
            self.publish_power()

    def y_control(self, speed):
        if self.xyzrpy["y"] != speed:
            multiplier = 3
            prev_thruster_input = self.xyzrpy["y"] * multiplier
            thruster_input = speed * multiplier
            diff = thruster_input - prev_thruster_input
            # first: subtract diff
            self.thrusters[0]["power"] -= diff
            # second: subtract diff
            self.thrusters[1]["power"] -= diff
            # third: subtract diff
            self.thrusters[2]["power"] -= diff
            # fourth: subtract diff
            self.thrusters[3]["power"] -= diff

            self.xyzrpy["y"] = speed
            self.publish_power()

    def z_control(self, speed):
        multiplier = 3
        for publisher in self.publishers_[4:8]:
            thruster_input = speed * multiplier
            publisher.publish(Float64(data=thruster_input))

    def roll_control(self, speed):
        pass

    def pitch_control(self, speed):
        pass

    def yaw_control(self, speed):
        pass

    def publish_power(self):
        for i in range(len(self.thrusters)):
            self.publishers_[i].publish(Float64(data=self.thrusters[i]["power"]))

    def spin(self):
        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)

    print("Keyboard controller node started")

    node = ThrusterControllerNode()
    node.create_publishers(Float64)

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
