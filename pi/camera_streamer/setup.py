from setuptools import setup
from glob import glob
import os

package_name = 'camera_streamer'

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
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Noah Mollerstuen',
    maintainer_email='noah@mollerstuen.com',
    description='contains camera information aswell as camera launch files',
    license='Apaches License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'image_publisher = camera_streamer.image_publisher:main'
        ],
    },
)
