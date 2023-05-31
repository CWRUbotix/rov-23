from setuptools import setup
from glob import glob
import os

package_name = 'task_selector'

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
    maintainer='ericy',
    maintainer_email='ery12@case.edu',
    description='Mate ROV task scheduler and task nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'selector = task_selector.task_selector:main',
            'manual_control_node = task_selector.manual_control_node:main',
            'ex_request_client = task_selector.example_request_client:main',
            'ex_timed_task = task_selector.basic_task_timed_node:main',
            'ex_basic_task = task_selector.basic_task_node:main',
            'ex_morning_task = task_selector.is_morning_node:main',
        ],
    },
)
