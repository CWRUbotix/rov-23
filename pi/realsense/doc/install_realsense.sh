# Add access to download
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u

# Install realsense2
# While Installing it might ask for password this is fine just type in the rov password
sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils
sudo apt-get update
sudo apt-get upgrade

# Good to source bashrc
source ~/.bashrc

sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
# cd ~/rov_23_ws/src/pi

# git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-development
# cd ~/rov_23_ws

# sudo apt-get install python3-rosdep -y
# sudo rosdep init # "sudo rosdep init --include-eol-distros" for Eloquent and earlier
# rosdep update # "sudo rosdep update --include-eol-distros" for Eloquent and earlier
# rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y

# # Build from source2
# colcon build
# source ~/.bashrc