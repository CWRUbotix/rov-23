
sudo apt-get install rapidjson-dev  libignition-gazebo5-dev

sudo rm -r ~/ardupilot_gazebo

cd ~/
git clone https://github.com/ArduPilot/ardupilot_gazebo.git -b ignition-edifice
cd ardupilot_gazebo
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4

#LINEPLUGIN='export GZ_SIM_SYSTEM_PLUGIN_PATH=$HOME/ardupilot_gazebo/build:${GZ_SIM_SYSTEM_PLUGIN_PATH}'
FIRSTLINE='export IGN_CONFIG_PATH=/usr/share/ignition'

# Ignigtion Gazebo configs
# Then OpenGl Disabling for VMs
STUFF='export IGN_CONFIG_PATH=/usr/share/ignition

export IGN_RENDERING_RESOURCE_PATH=/usr/share/ignition/ignition-rendering5

export IGN_GAZEBO_RESOURCE_PATH=\
$HOME/ardupilot_gazebo/models:\
$HOME/ardupilot_gazebo/worlds

export IGN_GAZEBO_SYSTEM_PLUGIN_PATH=\
/usr/lib/x86_64-linux-gnu/ign-gazebo-5/plugins:\
$HOME/ardupilot_gazebo/build



export MESA_DEBUG=1
export MESA_GL_VERSION_OVERRIDE=4.1
export MESA_GLSL_VERSION_OVERRIDE=410
export MESA_EXTENSION_OVERRIDE="\
  -GL_ARB_buffer_storage \
  -GL_ARB_multi_draw_indirect \
  -GL_ARB_texture_buffer_range \
  -GL_ARB_compute_shader \
  -GL_ARB_ES3_compatibility \
  "'

if ! grep -qF "$FIRSTLINE" ~/.bashrc ; 
    then 
        echo "$STUFF" >> ~/.bashrc;
fi
source ~/.bashrc
