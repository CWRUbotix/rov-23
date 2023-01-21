#!/bin/bash

# Install git and curl
sudo apt install git
sudo apt install curl

# Setting locale
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

# Ubuntu Universe install
sudo apt install software-properties-common
sudo add-apt-repository universe

# Ubuntu Universe check
apt-cache policy | grep universe

# Adding ROS 2 repo to system
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade

# Install galactic distro of ROS2
# Should maybe switch to using $ROS_DISTRO
sudo apt install ros-galactic-desktop

# Add setup.bash to .bashrc only if it isn't already there
# Will have fun conflicts if you also have ros1 setup.bash in your .bashrc
LINE='source /opt/ros/galactic/setup.bash'
if ! grep -qF "$LINE" ~/.bashrc ; 
    then echo "$LINE" >> ~/.bashrc  ;
    source ~/.bashrc
fi