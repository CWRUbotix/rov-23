from tca9555 import TCA9555

# Initialize with standard I2C-bus address of TCA9555 a.k.a 0x20
gpio = TCA9555()

# Print startup-config as human-readable
# print(gpio.format_config())

# # Set pins 0, 1, 2 as output
# # gpio.set_output(bits=(0,1,2)) # maybe this is set_bits()???

# # Write value 5 to bits 0, 1, 2
# gpio.int_to_bits(bits=(0,1,2), val=5)

# # Read value from bits 0, 1, 2 
# print(gpio.int_from_bits(bits=(0,1,2)))  # 5

# # Check if bit 0 is high
# gpio.is_high(0)

# # Set bit 1 and 2
# gpio.set_bits(bits=(1, 2))

# # Unset bits 2
# gpio.unset_bits(bits=2)