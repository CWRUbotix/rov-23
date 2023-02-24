sudo apt install rapidjson-dev libignition-gazebo7-dev

cd ../

git clone https://github.com/ArduPilot/ardupilot_gazebo -b ignition-garden
cd ardupilot_gazebo
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4