cd ../
git clone --recursive https://github.com/ArduPilot/ardupilot.git
cd ardupilot

Tools/environment_install/install-prereqs-ubuntu.sh -y

. ~/.profile

./waf configure --board sitl
./waf sub
./waf install
./waf --targets bin/ardusub --upload

./ardusub -M gazebo