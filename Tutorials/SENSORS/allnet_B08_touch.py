from micropython import const
from machine import Pin
from utime import sleep


# define constants
TOUCH_GPIO_PIN = const(23)
DELAY = const(1)


# create pin objects
touch = Pin(TOUCH_GPIO_PIN, Pin.IN)

if __name__ == '__main__':
    while True:
        sleep(DELAY)
        if touch.value():
            print(f'[INFO] board not touched')
        else:
            print(f'[INFO] board touched')
