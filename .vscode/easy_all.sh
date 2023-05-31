# Next year could move root of clone
# Or Make custom vscode extension

rosdep update --rosdistro=$ROS_DISTRO --include-eol-distros
rosdep install --from-paths src --ignore-src -r -y
# Stolen from colcon build command in VsCode
colcon build --symlink-install
source install/setup.bash