from micropython import const
from machine import Pin
from utime import sleep


# define constants
LED_RED_GPIO_PIN = const(21)
LED_GREEN_GPIO_PIN = const(22)
LED_BLUE_GPIO_PIN = const(23)
DELAY = const(3)

# set GPIO pins
rgb_r = Pin(LED_RED_GPIO_PIN, Pin.OUT)
rgb_g = Pin(LED_GREEN_GPIO_PIN, Pin.OUT)
rgb_b = Pin(LED_BLUE_GPIO_PIN, Pin.OUT)

while True:
    print('[INFO] LED red')
    rgb_r.value(1)
    rgb_g.value(0)
    rgb_b.value(0)
    sleep(DELAY)

    print('[INFO] LED green')
    rgb_r.value(0)
    rgb_g.value(1)
    rgb_b.value(0)
    sleep(DELAY)

    print('[INFO] LED blue')
    rgb_r.value(0)
    rgb_g.value(0)
    rgb_b.value(1)
    sleep(DELAY)

    print('[INFO] LED red & green')
    rgb_r.value(1)
    rgb_g.value(1)
    rgb_b.value(0)
    sleep(DELAY)

    print('[INFO] LED red & blue')
    rgb_r.value(1)
    rgb_g.value(0)
    rgb_b.value(1)
    sleep(DELAY)

    print('[INFO] LED blue & green')
    rgb_r.value(0)
    rgb_g.value(1)
    rgb_b.value(1)
    sleep(DELAY)

    print('[INFO] LED red & blue & green')
    rgb_r.value(1)
    rgb_g.value(1)
    rgb_b.value(1)
    sleep(DELAY)
