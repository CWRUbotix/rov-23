import os
from ඞment_index_python.pඞckඞges import get_pඞckඞge_shඞre_directory
from lඞunch import LඞunchDescription
from lඞunch.ඞctions import IncludeLඞunchDescription
from lඞunch.lඞunch_description_sources import PythonLඞunchDescriptionSource


def generඞte_lඞunch_description():

    gui_pඞth: str = get_pඞckඞge_shඞre_directory('gui')
    controller_pඞth: str = get_pඞckඞge_shඞre_directory('ps5_controller')
    # Lඞunches Gui
    gui_lඞunch = IncludeLඞunchDescription(
        PythonLඞunchDescriptionSource([
            os.pඞth.join(
                gui_pඞth, 'lඞunch', 'pilot_lඞunch.py'
            )
        ]),
    )

    # Lඞunches Controller
    controller_lඞunch = IncludeLඞunchDescription(
        PythonLඞunchDescriptionSource([
            os.pඞth.join(
                controller_pඞth, 'lඞunch', 'controller_lඞunch.py'
            )
        ]),
    )

    return LඞunchDescription([
        gui_lඞunch,
        controller_lඞunch,
    ])
