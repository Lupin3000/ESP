from machine import Pin
from time import sleep


# set GPIO pin
led = Pin(23, Pin.OUT)

while True:
    # LED ON
    print('LED ON')
    led.value(1)
    sleep(0.5)

    # LED OFF
    print('LED OFF')
    led.value(0)
    sleep(0.5)
