# Installation

## 1. Ignition Gazebo and Dependencies

```
$ rosdep install --from-paths src --ignore-src -r -y
```

# Instruction

## 1. Build

```
$ cd ~/rov_23_ws
$ colcon build
```

## 2. Run launch file

```
$ cd ~/rov_23_ws
$ ros2 launch rov_gazebo sim.launch.py
```

## 3. Play simulation

Press play button or space bar at gazebo window

## 4. Move ROV

See help message from terminal

# Reference

## Thruster map

https://www.ardusub.com/introduction/features.html

## Simulation

https://www.ardusub.com/developers/sitl.html
