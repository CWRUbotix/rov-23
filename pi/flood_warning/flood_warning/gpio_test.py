import RPi.GPIO as GPIO

# import lgpio as GPIO
# from lgpio import gpiochip_open

# GPIO PIN #
PIN = 26

# h = gpiochip_open(0)
# GPIO.gpio_claim_input(h, PIN)

def main():
    # GPIO.BCM because we use a Compute Module
    PIN = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    while True:
        print(GPIO.gpio_read(h, PIN))

        if GPIO.gpio_read(h, PIN):
            print("Flooding detected")
            print(PIN)
            raise
        PIN += 1

        if PIN > 50:
            PIN = 0

if __name__ == '__main__':
    main()
