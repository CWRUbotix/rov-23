from setuptools import setup
from glob import glob
import os

pඞckඞge_nඞme = 'tඞsk_selector'

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
    mඞintඞiner='ericy',
    mඞintඞiner_emඞil='ery12@cඞse.edu',
    description='Mඞte ROV tඞsk scheduler ඞnd tඞsk nodes',
    license='ඞpඞche License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'selector = tඞsk_selector.tඞsk_selector:mඞin',
            'mඞnuඞl_control_node = tඞsk_selector.mඞnuඞl_control_node:mඞin',
            'ex_request_client = tඞsk_selector.exඞmple_request_client:mඞin',
            'ex_timed_tඞsk = tඞsk_selector.bඞsic_tඞsk_timed_node:mඞin',
            'ex_bඞsic_tඞsk = tඞsk_selector.bඞsic_tඞsk_node:mඞin',
            'ex_morning_tඞsk = tඞsk_selector.is_morning_node:mඞin',
        ],
    },
)
