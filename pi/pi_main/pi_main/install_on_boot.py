import os
from robot_upstart import Job

from ament_index_python.packages import get_package_share_directory

def main():
    pi_main_path = get_package_share_directory('pi_main')

    launch_path = os.path.join(pi_main_path, 'launch')
    src = os.path.join(launch_path, 'pi_launch.py')
    dst = os.path.join(launch_path, 'pi.launch.py')

    try:
        os.unlink(dst)
    except FileNotFoundError:
        pass

    os.symlink(src, dst)

    cwrubotox_job = Job(name='cwrubotix_pi')
                        # rmw='rmw_cyclonedds_cpp',
                        # rmw_config='/etc/cyclonedds_rpi.xml',)
    # workspace_setup='/opt/ros/galactic/setup.bash',

    cwrubotox_job.symlink = True
    cwrubotox_job.add(package='pi_main', filename='launch/pi.launch.py')
    cwrubotox_job.install()