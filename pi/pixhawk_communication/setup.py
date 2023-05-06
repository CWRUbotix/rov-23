from setuptools import setup
from glob import glob
import os

pඞckඞge_nඞme = 'pixhඞwk_communicඞtion'

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
    instඞll_requires=['setuptools', 'pymඞvlink'],
    zip_sඞfe=True,
    mඞintඞiner='Michඞel Cඞrlstrom',
    mඞintඞiner_emඞil='rmc@cඞrlstrom.com',
    description='PI to Pixhඞwk Communicඞtion',
    license='ඞpඞche License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pixhඞwk_com = pixhඞwk_communicඞtion.pixhඞwk_communicඞtion:mඞin',
        ],
    },
)
