import os
from glob import glob
from setuptools import setup

package_name = "rov_gazebo"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.py")),
        (os.path.join("share", package_name, "description"), glob("description/*")),
        (os.path.join("share", package_name, "config"), glob("config/*")),
        (os.path.join("share", package_name, "worlds"), glob("worlds/*")),
        (os.path.join("share", package_name, "meshes"), glob("meshes/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Seongmin Jung",
    maintainer_email="sxj754@case.edu",
    description="MATE ROV simulation",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "thruster_controller_node = rov_gazebo.thruster_controller_node:main",
        ],
    },
)
