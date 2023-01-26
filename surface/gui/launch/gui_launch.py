import launch
import os
from pathlib import Path


def generate_launch_description():
    """Asynchronously ROS launch the GUI."""
    # This nonsense gets the relative path from this launch file (in the share
    # dir) to run_gui.py (in the src dir).
    run_gui_path = os.path.join(Path(__file__).parent.resolve(), '..', '..', '..',
                                '..', '..', 'src', 'surface', 'gui', 'gui', 'run_gui.py')

    # We run a bash command to start run_gui.py as a separate process
    # We must use a separate process:
    #   Cannot be a thread b/c PyQt needs to run in the main thread
    #   Cannot run in *this* main thread b/c that blocks other things
    #       from running in a launch file that includes this launch file
    #   Cannot use an official multiprocessing.Process b/c those require
    #       importing run_gui.py which makes the whole path thing even jankier
    os.system('python3 ' + run_gui_path + ' &')

    return launch.LaunchDescription([])
