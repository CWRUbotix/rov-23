from enum import IntEnum


class Tasks(IntEnum):
    MANUAL_CONTROL = 0
    AUTO_DOCKING = 1
    CANCEL = -1
    ERROR = -2
    # EX_BASIC = auto()
    # EX_TIMED = auto()
    # EX_GOOD_MORNING = auto()
