from PyQt5.QtWidgets import QWidget
from typing import Union


class ExecutorModule(QWidget):
    """
    Superclass for all Executor modules.

    Requires that modules which create spinning nodes implement an executor killer.
    This is for modules that have subscribers or servers.
    """

    def __init__(self):
        super().__init__()

    def kill_module(self) -> None:
        """
        Kill all executors create by this module & run any other death routines.

        Called when app's closeEvent occurs.
        """
        raise NotImplementedError('You called kill_module on a module' +
                                  'that didn\'t implement it')


class NonExecutorModule(QWidget):
    """
    Superclass for all non-executor modules.

    This is modules that only have publishers or clients.
    """

    def __init__(self):
        super().__init__()

    def kill_module(self):
        """No Executors to kill so pass."""
        pass


Module = Union[ExecutorModule, NonExecutorModule]
""" Super Class for all Modules"""
