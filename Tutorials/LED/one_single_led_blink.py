from micropython import const
from machine import Pin
from utime import sleep


# define constants
LED_GPIO_PIN = const(23)
DELAY = const(0.5)

# create pin object
led = Pin(LED_GPIO_PIN, Pin.OUT)

if __name__ == '__main__':
    while True:
        print('[INFO] LED ON')
        led.value(1)
        sleep(DELAY)

        print('[INFO] LED OFF')
        led.value(0)
        sleep(DELAY)
