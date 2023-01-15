from micropython import const
from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep_ms


# declare constants
NEO_PIXEL_COUNT = const(90)
LED_GPIO = const(23)

# create neo pixel object
nps = NeoPixel(Pin(LED_GPIO), NEO_PIXEL_COUNT)


def set_all() -> None:
    # random values
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    for item in range(0, NEO_PIXEL_COUNT):
        nps[item] = (red, green, blue)
        nps[item - 1] = (red, green, blue)
        nps[item - 4] = (0, 0, 0)
        nps.write()
        sleep_ms(1)


# define some variables
max_count = 15
start_count = 0

while start_count < max_count:
    print(f'round {start_count} of {max_count}')
    set_all()
    start_count += 1
