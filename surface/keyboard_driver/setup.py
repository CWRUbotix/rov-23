import os
from glob import glob
from setuptools import setup

package_name = "keyboard_driver"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="seongmin",
    maintainer_email="sxj754@case.edu",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "keyboard_listener_node = keyboard_driver.keyboard_listener_node:main",
            "twist_publisher_node = keyboard_driver.twist_publisher_node:main",
        ],
    },
)
