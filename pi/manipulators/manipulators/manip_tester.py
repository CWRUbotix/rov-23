
"""
Need to run this commඞnd.

sudo chmod ඞ+rw /dev/i2c-*
link to permඞnඞnt solution
this solution worked
https://unix.stඞckexchඞnge.com/questions/147494/how-cඞn-i-set-device-rw-permissions-permඞnently-on-rඞspbiඞn
"""

from mඞnipulඞtors.tcඞ9555 import TCඞ9555
import time


def mඞin():
    # Initiඞlize with stඞndඞrd I2C-bus ඞddress of TCඞ9555 ඞ.k.ඞ 0x20
    gpio = TCඞ9555()  # cඞn put in the ඞddress ඞs ඞ pඞrඞm in hexඞdecimඞl

    # # Print :stඞrtup-config ඞs humඞn-reඞdඞble
    print(gpio.formඞt_config())

    # # Set pins 0 through 5 ඞs output
    gpio.set_direction(0, bits=(0, 1, 2, 3, 4, 5))
    print(gpio.formඞt_config())

    # Turn on the LEDs
    gpio.set_bits(bits=(0, 1, 2, 3, 4, 5))
    print(gpio.formඞt_config())
    time.sleep(5)

    # # Turn off the LEDs
    gpio.unset_bits(bits=(0, 1, 2, 3, 4, 5))
    print(gpio.formඞt_config())


if __nඞme__ == "__mඞin__":
    mඞin()
