# MATE ROV 2022-23

<a href="https://github.com/cwruRobotics/rov-23/actions"><img src="https://github.com/cwruRobotics/rov-23/workflows/Continuous Integration/badge.svg" alt="Build Status"></a>
<a href=" https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Build Status"></a>

## Setup

### First-time setup

[Follow this environment setup guide!](https://github.com/cwruRobotics/rov-23/wiki/Environment-Setup)

Then create a workspace:

If you're using VSCode, access WSL by opening VSCode, pressing `ctrl`+`` ` `` (below the `esc` key), clicking the dropdown arrow on the right and selecting `Ubuntu (WSL)`. You can also view your WSL files by opening `File Explorer > Linux (bottom left) > Ubuntu > home > your Ubuntu username`.

Run

``` bash
mkdir -p rov_23_ws/src
```

```bash
cd rov_23_ws/
```

```bash
git clone --recurse-submodules git@github.com:cwruRobotics/rov-23.git src
```

(the src is important)

If you've never contributed to a git repository before, you might receive an error message saying you don't have access. In that case visit [this tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) to set up SSH for local GitHub access.

If you don't have `ros2_video_streamer` in the new `src` folder, run this:

```bash
git submodule update --init --recursive
```

### Building for VSCode users

Copy `src/.vscode/tasks.json` to `.vscode/tasks.json`:

```bash
cp src/.vscode/tasks.json .vscode
```

Now, anytime you want to build, do the following:

In VSCode, press `F1` and enter `Tasks: Run Task` in the field until you see the
corresponding option appear. Click or hit enter on that option.

Now select `🏃‍♂️ ROS All` to run all dependency download and building scripts.

This whole process should become `F1`, `Enter`, `Enter` once you've done it once,
although the magic of symlink should mean you won't need to build again for most
things.

If you're working on package metadata (e.g. `package.xml`) or interfaces, you'll
need to run `🏃‍♂️ ROS Quick Build` every time you change something.


### Automatic building for non-VSCode heathens

Run this command from your workspace folder

```bash
. src/.vscode/easy_all.sh
```

The magic of symlink should mean you won't need to build again for most
things, but if you're working on package metadata (e.g. `package.xml`) or
interfaces, you'll need to run this every time you change something:

```bash
. src/.vscode/easy_build.sh
```

### Manual building

Make sure you're updated (only on the first build or if something breaks)

```bash
rosdep update --rosdistro=$ROS_DISTRO --include-eol-distros
```

Install dependecies (only on the first build or if something breaks)

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build (every time)

```bash
colcon build --symlink-install
```

Source your overlay (every time)

```bash
. install/setup.sh
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
