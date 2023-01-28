from micropython import const
from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep_ms


# define constants
NEOPIXEL_NUMBER = const(90)
LED_GPIO_PIN = const(23)
DELAY = const(1)

# create neopixel object
nps = NeoPixel(Pin(LED_GPIO_PIN), NEOPIXEL_NUMBER)

# define variable
counter = 1


def set_all() -> None:
    """
    Turn LED's on/off
    :return: None
    """
    # random color values
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    for item in range(0, NEOPIXEL_NUMBER):
        nps[item] = (red, green, blue)
        nps[item - 1] = (red, green, blue)
        nps[item - 4] = (0, 0, 0)
        nps.write()
        sleep_ms(DELAY)


while True:
    print(f'[INFO] Round: {counter}')
    set_all()
    counter += 1
