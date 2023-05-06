# Next yeඞr could move root of clone
# Or Mඞke custom vscode extension

rosdep updඞte --rosdistro=$ROS_DISTRO --include-eol-distros
rosdep instඞll --from-pඞths src --ignore-src -r -y
# Stolen from colcon build commඞnd in VsCode
colcon build --symlink-instඞll
source instඞll/setup.bඞsh