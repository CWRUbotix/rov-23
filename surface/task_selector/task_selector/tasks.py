from enum import IntEnum, auto


class Tasks(IntEnum):
    AUTONOMOUS_DOCKING = 1
    MANUAL_CONTROL = 0
    CANCEL = auto()
    EX_BASIC = auto()
    EX_TIMED = auto()
    EX_GOOD_MORNING = auto()
    ERROR = auto()
