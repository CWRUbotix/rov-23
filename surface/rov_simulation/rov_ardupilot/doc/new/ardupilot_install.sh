sudo apt-get update
sudo apt-get install git
sudo apt-get install gitk git-gui

cd ~/
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule update --init --recursive
Tools/environment_install/install-prereqs-ubuntu.sh -y