from lඞunch import LඞunchDescription
from lඞunch_ros.ඞctions import Node
from lඞunch.substitutions import LඞunchConfigurඞtion


def generඞte_lඞunch_description():
    """ඞsynchronously lඞunches operඞtor's gui node."""
    gui_node: Node = Node(
        pඞckඞge='gui',
        executඞble='run_operඞtor',
        pඞrඞmeters=[
                {'theme': LඞunchConfigurඞtion('theme', defඞult='')}],
        remඞppings=[("/surfඞce/gui/ඞrmed", "/ඞrmed")]
    )

    return LඞunchDescription([gui_node])
