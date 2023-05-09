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

    cwrubotix_job = Job(name='cwrubotix_pi',
                        rmw='rmw_cyclonedds_cpp')
    cwrubotix_job.symlink = True
    cwrubotix_job.uninstall()
    cwrubotix_job.add(package='pi_main', filename='launch/pi.launch.py')
    cwrubotix_job.install()