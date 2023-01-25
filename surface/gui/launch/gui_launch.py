import multiprocessing
import launch
import os
import sys
from pathlib import Path

"""DANGER: DO NOT MODIFY"""
# This nonsense inserts, into system path, the relative path from this launch file
# (in the share dir) to the src dir. Adding this path to the system path then lets
# us import the GUI running script, which can be started as a separate process
# in the gui package src dir as usual.
gui_launch = os.path.join(
    Path(__file__).parent.resolve(), '..', '..', '..', '..', 'src', 'surface', 'gui', 'gui')
sys.path.insert(1, gui_launch)

# Import must come after adding gui_launch to the system path
from run_gui import run_gui
"""END OF DANGER"""


def generate_launch_description():
    # Must use a separate process:
    #   Cannot be a thread b/c PyQt needs to run in the main thread
    #   Cannot run in *this* main thread b/c that blocks other things
    #       from running in a launch file that includes this launch file
    multiprocessing.Process(target=run_gui).start()

    return launch.LaunchDescription([])
