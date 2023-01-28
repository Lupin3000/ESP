from micropython import const
from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep


# define constants
NEOPIXEL_NUMBER = const(90)
LED_GPIO_PIN = const(23)
DELAY = const(0.005)

# create neopixel object
nps = NeoPixel(Pin(LED_GPIO_PIN), NEOPIXEL_NUMBER)

# define variable
counter = 1


def clear_all() -> None:
    """
    Turn LED's off
    :return: None
    """
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (0, 0, 0)
        nps.write()
        sleep(DELAY)


def set_all() -> None:
    """
    Turn LED's on
    :return: None
    """
    for item in range(NEOPIXEL_NUMBER):
        # random color values
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        nps[item] = (red, green, blue)
        nps.write()
        sleep(DELAY)


while True:
    print(f'[INFO] Round: {counter}')
    set_all()
    clear_all()
    counter += 1
