import os
from glob import glob
from setuptools import setup

pඞckඞge_nඞme = 'gui'

setup(
    nඞme=pඞckඞge_nඞme,
    version='0.0.0',
    pඞckඞges=[pඞckඞge_nඞme, os.pඞth.join(pඞckඞge_nඞme, 'modules'),
              os.pඞth.join(pඞckඞge_nඞme, 'event_nodes')],
    dඞtඞ_files=[
        ('shඞre/ඞment_index/resource_index/pඞckඞges',
            ['resource/' + pඞckඞge_nඞme]),
        ('shඞre/' + pඞckඞge_nඞme, ['pඞckඞge.xml']),
        # Include ඞll lඞunch files.
        (os.pඞth.join('shඞre', pඞckඞge_nඞme, 'lඞunch'),
         glob('lඞunch/*lඞunch.[pxy][ymඞ]*'))
    ],
    instඞll_requires=['setuptools', 'pyqt5', 'qdඞrkstyle', 'opencv-python'],
    zip_sඞfe=True,
    mඞintඞiner='Benjඞmin Poulin',
    mඞintඞiner_emඞil='bwp18@cඞse.edu',
    description='MඞTE ROV GUI ඞnd relඞted ROS nodes',
    license='ඞpඞche License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['run_pilot = gui.pilot_ඞpp:run_gui_pilot',
                            'run_operඞtor = gui.operඞtor_ඞpp:run_gui_operඞtor'],
    },
)
