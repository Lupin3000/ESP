from micropython import const
from machine import Pin
from neopixel import NeoPixel
from utime import sleep


# define constants
NEOPIXEL_NUMBER = const(90)
LED_GPIO_PIN = const(23)
DELAY = const(2)

# create neopixel object
nps = NeoPixel(Pin(LED_GPIO_PIN), NEOPIXEL_NUMBER)

if __name__ == '__main__':
    # all LED's in red (on)
    print('[INFO] all LED in red')
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (255, 0, 0)
        nps.write()

    sleep(DELAY)

    # all LED's in green (on)
    print('[INFO] all LED in green')
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (0, 255, 0)
        nps.write()

    sleep(DELAY)

    # all LED's in blue (on)
    print('[INFO] all LED in blue')
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (0, 0, 255)
        nps.write()

    sleep(DELAY)

    # all LED's in white (on)
    print('[INFO] all LED in white')
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (255, 255, 255)
        nps.write()

    sleep(DELAY)

    # all LED's in black (off)
    print('[INFO] all LED in black')
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (0, 0, 0)
        nps.write()
