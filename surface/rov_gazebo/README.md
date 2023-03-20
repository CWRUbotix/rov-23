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
$ ros2 launch rov_gazebo sim_launch.py
```

## 3. Play simulation

Press play button or space bar at gazebo window

## 4. Move ROV

Don't forget to arm the ROV

See help message from terminal or use PS5 controller

# Reference

## Thruster map

https://www.ardusub.com/introduction/features.html

## Simulation

https://www.ardusub.com/developers/sitl.html
## Published Topics
/bottom_cam/image_raw

/front_cam/image_raw

/manip_cam/image_raw

/depth_cam/image_raw

/depth_cam/points
## Subscription Topics
/manual_control

/arm
