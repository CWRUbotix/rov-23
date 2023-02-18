# Next year could move root of clone
# Or Make custom vscode Extension

# Currently requires copying tasks.json contents into root directory .vscode/ folder
function cdroot()
{
  while [[ $PWD != '/' && ${PWD##*/} != 'rov_23_ws' ]]; do cd ..; done
}

cdroot
rosdep update --rosdistro=$ROS_DISTRO
rosdep install --from-paths src --ignore-src -r -y
# Stolen from colcon build command in VsCode
colcon build --symlink-install
source install/setup.bash

