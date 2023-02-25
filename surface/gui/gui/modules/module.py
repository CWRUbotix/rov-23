from PyQt5.QtWidgets import QWidget


class Module(QWidget):
    """
    Superclass for all modules.

    Requires that modules which create spinning nodes implement an executor killer.
    """

    def __init__(self):
        super().__init__()

    def kill_module(self):
        """
        Kill all executors create by this module & run any other death routines.

        Called when app's closeEvent occurs.
        """
        raise NotImplementedError('You called kill_module on a module' +
                                  'that didn\'t implement it')
