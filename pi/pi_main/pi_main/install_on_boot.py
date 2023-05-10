import os
from robot_upstart import Job
import subprocess

from ament_index_python.packages import get_package_share_directory

def main():
    pi_main_path = get_package_share_directory('pi_main')

    launch_dir = os.path.join(pi_main_path, 'launch')
    launch_src = os.path.join(launch_dir, 'pi_launch.py')
    launch_dst = os.path.join(launch_dir, 'pi.launch.py')

    try:
        os.unlink(launch_dst)
    except FileNotFoundError:
        pass

    os.symlink(launch_src, launch_dst)

    udev_script = os.path.join(pi_main_path, 'udev_copy', 'udev_copy.py')

    subprocess.call(['/usr/bin/sudo', 'python3', udev_script, f'"{pi_main_path}"'])

    cwrubotix_job = Job(name='cwrubotix_pi', rmw='rmw_cyclonedds_cpp')
    cwrubotix_job.symlink = True
    cwrubotix_job.uninstall()
    cwrubotix_job.add(package='pi_main', filename='launch/pi.launch.py')
    cwrubotix_job.install()