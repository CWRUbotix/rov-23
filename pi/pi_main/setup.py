from setuptools import setup
from glob import glob
import os
import shutil


package_name = 'pi_main'


setup(
    name=package_name,
    version='0.0.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michael Carlstrom',
    maintainer_email='rmc170@case.edu',
    description='Mate ROV Main code launcher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={},
)

dirs = os.listdir(os.path.expanduser("~"))

ws = None
for dir in dirs:
    if "ws" in dir:
        if ws is not None:
            raise KeyError("Multiple Workspaces detected in home cannot pick")
        ws = dir

if ws is None:
    raise ValueError("No workspace found")

print(os.listdir(ws))

# Robot Upstart wants *.launch.py so this copies around that
src = os.path.join('~', ws, 'src', 'pi', package_name, 'launch', 'pi_launch.py')
src_home = os.path.expanduser(src)
dst_path = os.path.join('~', ws, 'install',
                        package_name, 'share', package_name, 'launch')
dst_home = os.path.expanduser(dst_path)
dst = os.path.join(dst_home, 'pi.launch.py')

try:
    os.makedirs(dst_home)
except FileExistsError:
    pass
shutil.copy2(src_home, dst_home)
