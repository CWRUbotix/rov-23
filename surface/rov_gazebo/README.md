# Installation

## 1. Ignition gazebo

```
$ sudo apt-get install ros-galactic-ros-ign
```

## 2. Ros Ign Bridge

```
$ sudo apt-get install ros-galactic-ros-ign-bridge
```

## 3. Ardupilot lib

https://github.com/srmainwaring/ardupilot_gazebo/wiki

# Instruction

## 1. Build

```
$ cd ~/rov_23_ws
$ colcon build
```

## 2. Make sdf file for simulation

```
$ cd ~/rov_23_ws/src/surface/rov_gazebo/worlds
$ python3 make_sdf.py
```

## 3. Run launch file

```
$ cd ~/rov_23_ws
$ ros2 launch rov_gazebo sim.launch.py
```

## 4. Play simulation

press play button or space bar at gazebo window

## 5. Start thruster

Directory doesn't matter here. 24 means the power of the thruster.

```
$ ign topic -t "/model/rov/joint/thruster_top_front_left_body_blade_joint/cmd_force" -m ignition.msgs.Double  -p "data: 24"
```

# Reference

## Thruster map

https://www.ardusub.com/introduction/features.html

## Simulation

https://www.ardusub.com/developers/sitl.html
