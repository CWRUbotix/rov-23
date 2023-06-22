import RPi.GPIO as GPIO

# GPIO PIN #
PIN = 26

def main():
    # GPIO.BCM because we use a Compute Module
    PIN = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)

    while True:
        print(GPIO.input(PIN))

        if GPIO.input(PIN) == GPIO.HIGH:
            print("Flooding detected")
            print(PIN)

if __name__ == '__main__':
    main()