from PyQt5.QtWidgets import QWidget


class Module(QWidget):
    """
    Superclass for all modules.

    Requires that modules which create spinning nodes implement an executor killer.
    """

    # TODO make sure this is safe to be gone
    # def __init__(self):
    #     super().__init__()
    # rclpy.init()

    def kill_all_executors(self):
        """Kill all executors create by this module."""
        return
