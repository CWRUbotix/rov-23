from setuptools import setup
from glob import glob
import os


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
         glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, 'udev_rules'),
         glob('udev_rules/*')),
        (os.path.join('share', package_name, 'udev_copy'),
         glob('pi_main/udev_copy.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michael Carlstrom',
    maintainer_email='rmc170@case.edu',
    description='Mate ROV Main code launcher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'install = pi_main.install_on_boot:main',
        ],
    },
)
