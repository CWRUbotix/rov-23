import launch
from gui.run_gui import run_gui
from multiprocessing import Process


def generate_launch_description():
    """Asynchronously ROS launch the GUI."""

    p = Process(target=run_gui, args=())
    p.start()
    return launch.LaunchDescription([])
