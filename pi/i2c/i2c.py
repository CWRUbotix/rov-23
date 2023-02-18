"""
Need to run this command:
sudo chmod a+rw /dev/i2c-*
"""

from TCA9555.tca9555 import TCA9555

# Initialize with standard I2C-bus address of TCA9555 a.k.a 0x20
gpio = TCA9555() # can put in the address as a param in hexadecimal

# Print :startup-config as human-readable
print(gpio.format_config())

# Set pins 0 through 5 as output
# gpio.set_direction(1, bits=(0, 1, 2, 3, 4, 5)) # Turns the lights off

# gpio.set_direction(0, bits=(0, 1, 2, 3, 4, 5)) # Turns the lights on
# gpio.set_direction(1, bits=(0, 1, 2)) # Turns the lights on
gpio.set_direction(0, bits=(2)) # Turns the lights on


