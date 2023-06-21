from setuptools import setup
import os

package_name = 'coral_viewer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
     ] + [(os.path.join('share', package_name, dp), [os.path.join(dp, f)])
          for dp, dn, fn in os.walk('coral_viewer_unity/Build/') for f in fn],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='noah',
    maintainer_email='noah@mollerstuen.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
