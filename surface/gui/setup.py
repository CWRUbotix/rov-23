import os
from glob import glob
from setuptools import setup

package_name = 'gui'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, os.path.join(package_name, 'modules'),
              os.path.join(package_name, 'event_nodes')],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools', 'pyqt5', 'qdarkstyle', 'opencv-python'],
    zip_safe=True,
    maintainer='Benjamin Poulin',
    maintainer_email='bwp18@case.edu',
    description='MATE ROV GUI and related ROS nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['run_pilot = gui.pilot_app:run_gui_pilot',
                            'run_operator = gui.operator_app:run_gui_operator'],
    },
)
