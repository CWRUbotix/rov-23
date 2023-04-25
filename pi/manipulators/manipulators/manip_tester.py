
"""
Need to run this command.

sudo chmod a+rw /dev/i2c-*
link to permanant solution
this solution worked
https://unix.stackexchange.com/questions/147494/how-can-i-set-device-rw-permissions-permanently-on-raspbian
"""

from manipulators.tca9555 import TCA9555
import time


def main():
    # Initialize with standard I2C-bus address of TCA9555 a.k.a 0x20
    gpio = TCA9555()  # can put in the address as a param in hexadecimal

    # # Print :startup-config as human-readable
    print(gpio.format_config())

    # # Set pins 0 through 5 as output
    gpio.set_direction(0, bits=(0, 1, 2, 3, 4, 5))
    print(gpio.format_config())

    # Turn on the LEDs
    gpio.set_bits(bits=(0, 1, 2, 3, 4, 5))
    print(gpio.format_config())
    time.sleep(5)

    # # Turn off the LEDs
    gpio.unset_bits(bits=(0, 1, 2, 3, 4, 5))
    print(gpio.format_config())


if __name__ == "__main__":
    main()
