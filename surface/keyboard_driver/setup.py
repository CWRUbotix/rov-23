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
    install_requires=["setuptools", "pynput"],
    zip_safe=True,
    maintainer="Seongmin Jung",
    maintainer_email="sxj754@case.edu",
    description="MATE ROV keyboard driver",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "keyboard_driver_node = keyboard_driver.keyboard_driver_node:main",
        ],
    },
)
