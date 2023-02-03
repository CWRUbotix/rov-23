from enum import Enum, auto


class Tasks(Enum):
    MANUAL_CONTROL = auto()
    CANCEL = auto()
    EX_BASIC = auto()
    EX_TIMED = auto()
    EX_GOOD_MORNING = auto()
    ERROR = auto()
