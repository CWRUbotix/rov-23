import os
from robot_upstart import Job
import subprocess
import sys

from ament_index_python.packages import get_package_share_directory

def main():
    pi_main_share = get_package_share_directory('pi_main')

    launch_dir = os.path.join(pi_main_share, 'launch')
    launch_src = os.path.join(launch_dir, 'pi_launch.py')
    launch_dst = os.path.join(launch_dir, 'pi.launch.py')

    try:
        os.unlink(launch_dst)
    except FileNotFoundError:
        pass

    os.symlink(launch_src, launch_dst)

    udev_script = os.path.join(pi_main_share, 'udev_copy', 'udev_copy.py')

    major_num = sys.version_info[0]
    minor_num = sys.version_info[1]
    udev_script = os.path.join(os.path.dirname(os.path.abspath(pi_main_share)),'../', 'lib', f'python{major_num}.{minor_num}',
                               'site-packages', 'pi_main', 'udev_copy.py')
    subprocess.call(['/usr/bin/sudo', 'python3', udev_script, pi_main_share])

    cwrubotix_job = Job(name='cwrubotix_pi', rmw='rmw_cyclonedds_cpp')
    cwrubotix_job.symlink = True
    cwrubotix_job.uninstall()
    cwrubotix_job.add(package='pi_main', filename='launch/pi.launch.py')
    cwrubotix_job.install()