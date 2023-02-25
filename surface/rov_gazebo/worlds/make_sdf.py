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

import os
from ament_index_python.packages import get_package_share_directory

rov_gazebo_path: str = get_package_share_directory("rov_gazebo")

filenameWorld: str = "world.sdf"
filenameXacro: str = "rov.xacro"
filenameURDF: str = "rov.urdf"
filenameSDF: str = "rov.sdf"
filenameYaml: str = "rov_description_params.yaml"
filenameRovInWorld: str = "rov_in_world.sdf"

path_to_world: str = os.path.join(rov_gazebo_path, "worlds", filenameWorld)
path_to_xacro: str = os.path.join(rov_gazebo_path, "worlds", filenameXacro)
path_to_urdf: str = os.path.join(rov_gazebo_path, "worlds", filenameURDF)
path_to_sdf: str = os.path.join(rov_gazebo_path, "worlds", filenameSDF)
path_to_yaml: str = os.path.join(rov_gazebo_path, "worlds", filenameYaml)
path_to_rov_in_world: str = os.path.join(rov_gazebo_path, "worlds", filenameRovInWorld)

sensors_sdf = """
      <sensor name="imu_sensor" type="imu">
        <pose>0 0 0 3.141592653589793 0 0</pose>
        <always_on>1</always_on>
        <update_rate>1000.0</update_rate>
      </sensor>
        <sensor name="camera" type="camera">
            <camera>
                <horizontal_fov>1.047</horizontal_fov>
                <image>
                <width>320</width>
                <height>240</height>
                </image>
                <clip>
                <near>0.1</near>
                <far>100</far>
                </clip>
            </camera>
            <always_on>1</always_on>
            <update_rate>30</update_rate>
            <visualize>true</visualize>
            <topic>camera</topic>
        </sensor>
        <sensor name="depth_camera1" type="depth_camera">
          <update_rate>10</update_rate>
          <topic>depth_camera</topic>
          <camera>
            <horizontal_fov>1.05</horizontal_fov>
            <image>
              <width>256</width>
              <height>256</height>
              <format>R_FLOAT32</format>
            </image>
            <clip>
              <near>0.1</near>
              <far>100.0</far>
            </clip>
          </camera>
          </sensor>
      """

with open(path_to_urdf, "w") as f:
    urdf = os.popen("xacro " + path_to_xacro + " params_path:=" + path_to_yaml).read()
    f.writelines(urdf)

with open(path_to_sdf, "w") as f:
    sdf = os.popen("gz sdf -p " + path_to_urdf).read().splitlines(True)
    f.writelines(sdf)
    sdf[3:3] = sensors_sdf

with open(path_to_world, "r") as f:
    contents = f.readlines()
    # Put the SDF model in the appropriate place in the world file
    contents[-34:-34] = sdf[1:-2]

with open(path_to_rov_in_world, "w") as f:
    f.writelines(contents)
