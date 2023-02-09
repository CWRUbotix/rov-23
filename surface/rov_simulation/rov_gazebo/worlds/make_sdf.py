import os
from ament_index_python.packages import get_package_share_directory

rov_gazebo_path: str = get_package_share_directory("rov_gazebo")

filenameWorld: str = "world.sdf"
filenameXacro: str = "rov.xacro"
filenameURDF: str = "rov.urdf"
filenameSDF: str = "rov.sdf"
filenameYaml: str = "rov_description_params.yaml"
filenameRovInWorld: str = "rov_in_world.sdf"

path_to_world: str = os.path.join(rov_gazebo_path, "worlds", filenameWorld)
path_to_xacro: str = os.path.join(rov_gazebo_path, "worlds", filenameXacro)
path_to_urdf: str = os.path.join(rov_gazebo_path, "worlds", filenameURDF)
path_to_sdf: str = os.path.join(rov_gazebo_path, "worlds", filenameSDF)
path_to_yaml: str = os.path.join(rov_gazebo_path, "worlds", filenameYaml)
path_to_rov_in_world: str = os.path.join(rov_gazebo_path, "worlds", filenameRovInWorld)

with open(path_to_urdf, "w") as f:
    urdf = os.popen("xacro " + path_to_xacro + " params_path:=" + path_to_yaml).read()
    f.writelines(urdf)

with open(path_to_sdf, "w") as f:
    sdf = os.popen("gz sdf -p " + path_to_urdf).read().splitlines(True)
    f.writelines(sdf)

with open(path_to_world, "r") as f:
    contents = f.readlines()
    # Put the SDF model in the appropriate place in the world file
    contents[-34:-34] = sdf[1:-2]

with open(path_to_rov_in_world, "w") as f:
    f.writelines(contents)
