# TCA9555

***

## Introduction

**TCA9555** is a Python module for interfacing the Texas Instruments [TCA9555](https://www.ti.com/lit/ds/symlink/tca9555.pdf) 16-bit I2C-based GPIO expander using a Raspberry Pi.
All public methods are **thread-safe** which allows for continuous reading / writing to the GPIO from mutliple threads.

## Installation

You have to have Python >= 2.7 with the following packages installed:

- [wiringpi](https://github.com/WiringPi/WiringPi-Python)
- [bitstring](https://github.com/scott-griffiths/bitstring)

To install these dependecies, open a terminal and type
```bash

pip install wiringpi bitstring
```
Then, to finally install **TCA9555**, move to the root folder and type
```bash

python setup.py develop
```

which will install in development mode

## Setup

To use this module, you need to enable the I2C interface of your Raspberry Pi

```bash

sudo raspi-config
```

Navigate to the `advanced options - I2C` menu and select `enable`. Now you need to connect the Raspberry Pis I2C pinout to the respective TCA9555 pins
```bash

 Role | Rpi | TCA9555
------|-----|--------
 SDA  |  3  |   23   
 SCL  |  5  |   22   
 GND  |  6  |   12   
 VCC  |  5  |   24   
```

If you do not plan to set a custom address to your TCA9555, tie address pins A0, A1 & A2 to GND as well. This will result in an IC2-bus address of 0x20 (32).
 
## Examples

### Basic usage

Below you'll find a selection of use-cases. To see all available methods, please check [here](https://github.com/leloup314/TCA9555/blob/master/tca9555/tca9555.py)

```python

# Import the class
from tca9555 import TCA9555

# Initialize with standard I2C-bus address of TCA9555 a.k.a 0x20
gpio = TCA9555()

# Print startup-config as human-readable
print(gpio.format_config())

# Set pins 0, 1, 2 as output
gpio.set_output(bits=(0,1,2))

# Write value 5 to bits 0, 1, 2
gpio.int_to_bits(bits=(0,1,2), val=5)

# Read value from bits 0, 1, 2 
print(gpio.int_from_bits(bits=(0,1,2)))  # 5

# Check if bit 0 is high
gpio.is_high(0)

# Set bit 1 and 2
gpio.set_bits(bits=(1, 2))

# Unset bits 2
gpio.unset_bits(bits=2)
```

### Multi-threaded usage

A more advanced scenario is that certain pins of the GPIO expander are used to read a value, while others are used to set registers / logic levels of other ICs.
Such a scenario is shown below

```python
# Imports
from tca9555 import TCA9555
from threading import Thread, Event

def continuous_read(pins):
    """Read continuously from *pins* until *flag* is set"""
    while not flag.is_set():
        res = gpio.int_from_bits(bits=pins)
        print(res)

# Initialize GPIO expander
gpio = TCA9555()

# Initialize flag to stop thread
flag = Event()

# Read 4 bit integer from pins 0 to 3
read_pins = (0, 1, 2, 3)

# Make thread
t = Thread(target=continuous_read, args=(read_pins,))

# Start thread
t.start()

# Continue to use gpio to set other pins
gpio.set_bits(bits=(4, 7, 15))
gpio.set_bits(bits=(5, 8, 11))
gpio.unset_bits(bits=(4, 8, 15))
gpio.int_to_bits(bits=(12, 13, 14), val=7)

# Continue working...

# Stop thread
flag.set()
t.join()
```

