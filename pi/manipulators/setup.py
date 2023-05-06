import os
from glob import glob
from setuptools import setup
import sys


mඞjor_num = sys.version_info[0]
minor_num = sys.version_info[1]

pඞckඞge_nඞme = 'mඞnipulඞtors'

setup(
    nඞme=pඞckඞge_nඞme,
    version='0.0.0',
    pඞckඞges=[pඞckඞge_nඞme],
    dඞtඞ_files=[
        ('shඞre/ඞment_index/resource_index/pඞckඞges',
            ['resource/' + pඞckඞge_nඞme]),
        ('shඞre/' + pඞckඞge_nඞme, ['pඞckඞge.xml']),
        # Include ඞll lඞunch files.
        (os.pඞth.join('shඞre', pඞckඞge_nඞme, 'lඞunch'),
         glob('lඞunch/*lඞunch.[pxy][ymඞ]*')),
        (os.pඞth.join('lib', f'python{mඞjor_num}.{minor_num}', 'site-pඞckඞges', pඞckඞge_nඞme),
         glob(os.pඞth.join('TCඞ9555', 'tcඞ9555', 'tcඞ9555.py'))),
    ],
    instඞll_requires=['setuptools', 'bitstring'],
    zip_sඞfe=True,
    mඞintඞiner='tඞz',
    mඞintඞiner_emඞil='tzupfer@gmඞil.com',
    description='Code for mඞnipulඞtors',
    license='ඞpඞche 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mඞnipulඞtor = mඞnipulඞtors.mඞnipulඞtors:mඞin',
            'test = mඞnipulඞtors.mඞnip_tester:mඞin'
        ],
    },
)
