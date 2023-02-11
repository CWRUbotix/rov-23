# MATE ROV 2022-23

<a href="https://github.com/cwruRobotics/rov-23/actions"><img src="https://github.com/cwruRobotics/rov-23/workflows/Continuous Integration/badge.svg" alt="Build Status"></a>
<a href=" https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Build Status"></a>

## Setup
[Follow this environment setup guide!](https://github.com/cwruRobotics/rov-23/wiki/Environment-Setup)

Then create a workspace:

Access WSL by opening VSCode, pressing `ctrl`+`` ` `` (below the `esc` key), clicking the dropdown arrow on the right and selecting `Ubuntu (WSL)`. You can also view your WSL files by opening `File Explorer > Linux (bottom left) > Ubuntu > home > your Ubuntu username`.

Run
```
mkdir -p rov_23_ws/src
```

```
cd rov_23_ws/src
```

```
git clone git@github.com:cwruRobotics/rov-23.git .
```
(the period is important)

If you've never contributed to a git repository before, you might receive an error message saying you don't have access. In that case visit [this tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) to set up SSH for local GitHub access.

Return to ws directory
```
cd ../
```
Install dependecies
```
rosdep install --from-paths src --ignore-src -r -y
```
Build
```
colcon build
```

## Directory Structure
All packages to be installed on the surface computer live in the `surface` directory.

All packages to be installed on the pi compute module live in the `pi` directory.

All packages to be installed on the float live in the `float` directory.

## Documentation Structure
Documentation will take place at 3 levels:
- High Level - Overarching Design Document outlining our general structure and what goes where.

- Device Level - ROS Docs as set out in the ROS2 standards.

- Inline Level - Inline Documentation to the level that someone who has some basic code knowledge can understand what the code does.
