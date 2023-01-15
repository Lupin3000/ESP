from micropython import const
from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep


# declare constants
NEO_PIXEL_COUNT = const(90)
LED_GPIO = const(23)

# create neo pixel object
nps = NeoPixel(Pin(LED_GPIO), NEO_PIXEL_COUNT)


def clear_all() -> None:
    for item in range(NEO_PIXEL_COUNT):
        nps[item] = (0, 0, 0)
        nps.write()
        sleep(0.005)


def set_all() -> None:
    for item in range(NEO_PIXEL_COUNT):
        # random values
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        nps[item] = (red, green, blue)
        nps.write()
        sleep(0.005)


# define some variables
max_count = 15
start_count = 0

while start_count < max_count:
    print(f'round {start_count} of {max_count}')
    set_all()
    clear_all()
    start_count += 1
