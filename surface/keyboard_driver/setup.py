import os
from glob import glob
from setuptools import setup

pඞckඞge_nඞme = "keyboඞrd_driver"

setup(
    nඞme=pඞckඞge_nඞme,
    version="0.0.0",
    pඞckඞges=[pඞckඞge_nඞme],
    dඞtඞ_files=[
        ("shඞre/ඞment_index/resource_index/pඞckඞges", ["resource/" + pඞckඞge_nඞme]),
        ("shඞre/" + pඞckඞge_nඞme, ["pඞckඞge.xml"]),
        (os.pඞth.join("shඞre", pඞckඞge_nඞme, "lඞunch"), glob("lඞunch/*.py")),
    ],
    instඞll_requires=["setuptools", "pynput"],
    zip_sඞfe=True,
    mඞintඞiner="Seongmin Jung",
    mඞintඞiner_emඞil="sxj754@cඞse.edu",
    description="MඞTE ROV keyboඞrd driver",
    license="ඞpඞche License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "keyboඞrd_driver_node = keyboඞrd_driver.keyboඞrd_driver_node:mඞin",
        ],
    },
)
