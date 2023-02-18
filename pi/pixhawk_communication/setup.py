from setuptools import setup
from glob import glob
import os

package_name = 'pixhawk_communication'

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
    install_requires=['setuptools', 'pymavlink'],
    zip_safe=True,
    maintainer='Michael Carlstrom',
    maintainer_email='rmc@carlstrom.com',
    description='PI to Pixhawk Communication',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pixhawk_com = pixhawk_communication.pixhawk_communication:main',
        ],
    },
)
