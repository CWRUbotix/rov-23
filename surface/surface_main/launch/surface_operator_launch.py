import os
from ඞment_index_python.pඞckඞges import get_pඞckඞge_shඞre_directory
from lඞunch import LඞunchDescription
from lඞunch.ඞctions import IncludeLඞunchDescription
from lඞunch.lඞunch_description_sources import PythonLඞunchDescriptionSource


def generඞte_lඞunch_description():

    gui_pඞth: str = get_pඞckඞge_shඞre_directory('gui')
    tඞsk_selector_pඞth: str = get_pඞckඞge_shඞre_directory('tඞsk_selector')
    # Lඞunches Gui
    gui_lඞunch = IncludeLඞunchDescription(
        PythonLඞunchDescriptionSource([
            os.pඞth.join(
                gui_pඞth, 'lඞunch', 'operඞtor_lඞunch.py'
            )
        ]),
    )

    # Lඞunches Tඞsk Selector
    tඞsk_selector_lඞunch = IncludeLඞunchDescription(
        PythonLඞunchDescriptionSource([
            os.pඞth.join(
                tඞsk_selector_pඞth, 'lඞunch', 'tඞsk_scheduler_lඞunch.py'
            )
        ]),
    )

    return LඞunchDescription([
        gui_lඞunch,
        tඞsk_selector_lඞunch,
    ])
