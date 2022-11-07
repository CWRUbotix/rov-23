sudo apt-get install rapidjson-dev  libignition-gazebo7-dev

cd ~/
git clone https://github.com/ArduPilot/ardupilot_gazebo -b ignition-garden
cd ardupilot_gazebo
mkdir build 
cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4

#LINEPLUGIN='export GZ_SIM_SYSTEM_PLUGIN_PATH=$HOME/ardupilot_gazebo/build:${GZ_SIM_SYSTEM_PLUGIN_PATH}'
LINEGZSIM='export GZ_SIM_SYSTEM_PLUGIN_PATH=~/ardupilot_gazebo/build'
if ! grep -qF "$LINEGZSIM" ~/.bashrc ; 
    then 
        echo "$LINEGZSIM" >> ~/.bashrc  ;
        #echo "$LINEGZSIM" >> ~/.bashrc;
fi
source ~/.bashrc
