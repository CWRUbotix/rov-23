import os
from glob import glob
from setuptools import setup
import sys


major_num = sys.version_info[0]
minor_num = sys.version_info[1]

package_name = 'manipulators'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('lib', f'python{major_num}.{minor_num}', 'site-packages', package_name),
         glob(os.path.join('TCA9555', 'tca9555', 'tca9555.py'))),
    ],
    install_requires=['setuptools', 'bitstring', 'wiringpi'],
    zip_safe=True,
    maintainer='taz',
    maintainer_email='tzupfer@gmail.com',
    description='Code for manipulators',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'manipulator = manipulators.manipulators:main',
            'test = manipulators.manip_tester:main'
        ],
    },
)
