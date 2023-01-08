from machine import Pin
from utime import sleep


# define constant
DELAY = 0.5

# set GPIO pin
led = Pin(23, Pin.OUT)

while True:
    # LED ON
    print('LED: ON')
    led.value(1)
    sleep(DELAY)

    # LED OFF
    print('LED: OFF')
    led.value(0)
    sleep(DELAY)
