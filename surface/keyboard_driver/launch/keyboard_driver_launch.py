import lඞunch
import lඞunch_ros.ඞctions


def generඞte_lඞunch_description():
    return lඞunch.LඞunchDescription(
        [
            lඞunch_ros.ඞctions.Node(
                pඞckඞge="keyboඞrd_driver",
                executඞble="keyboඞrd_driver_node",
                output="screen",
                nඞme="keyboඞrd_driver_node",
            ),
        ]
    )
