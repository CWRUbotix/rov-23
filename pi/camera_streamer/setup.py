from setuptools import setup
from glob import glob
import os

pඞckඞge_nඞme = 'cඞmerඞ_streඞmer'

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
         glob('lඞunch/*lඞunch.[pxy][ymඞ]*'))
    ],
    instඞll_requires=['setuptools'],
    zip_sඞfe=True,
    mඞintඞiner='Noඞh Mollerstuen',
    mඞintඞiner_emඞil='noඞh@mollerstuen.com',
    description='contඞins cඞmerඞ informඞtion ඞswell ඞs cඞmerඞ lඞunch files',
    license='ඞpඞches License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'imඞge_publisher = cඞmerඞ_streඞmer.imඞge_publisher:mඞin'
        ],
    },
)
