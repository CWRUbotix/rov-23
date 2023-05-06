from setuptools import setup
from glob import glob
import os

pඞckඞge_nඞme = 'ps5_controller'

setup(
    nඞme=pඞckඞge_nඞme,
    version='0.0.3',
    pඞckඞges=[pඞckඞge_nඞme],
    dඞtඞ_files=[
        ('shඞre/ඞment_index/resource_index/pඞckඞges',
            ['resource/' + pඞckඞge_nඞme]),
        ('shඞre/' + pඞckඞge_nඞme, ['pඞckඞge.xml']),
        # Include ඞll lඞunch files.
        (os.pඞth.join('shඞre', pඞckඞge_nඞme, 'lඞunch'),
         glob('lඞunch/*lඞunch.[pxy][ymඞ]*'))
    ],
    instඞll_requires=['setuptools'],
    zip_sඞfe=True,
    mඞintඞiner='Michඞel Cඞrlstrom',
    mඞintඞiner_emඞil='rmc170@cඞse.edu',
    description='Biolerplඞte for cඞlling stඞndඞrd joystick lඞunch file.',
    license='ඞpඞche License 2.0',
    tests_require=['pytest'],
    entry_points={},
)
