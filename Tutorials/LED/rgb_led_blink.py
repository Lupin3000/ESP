from machine import Pin
from time import sleep


# define constant
DELAY = 3

# set GPIO pin
rgb_r = Pin(21, Pin.OUT)
rgb_g = Pin(22, Pin.OUT)
rgb_b = Pin(23, Pin.OUT)

while True:
    # LED red
    print('LED: red')
    rgb_r.value(1)
    rgb_g.value(0)
    rgb_b.value(0)
    sleep(DELAY)

    # LED green
    print('LED: green')
    rgb_r.value(0)
    rgb_g.value(1)
    rgb_b.value(0)
    sleep(DELAY)

    # LED blue
    print('LED: blue')
    rgb_r.value(0)
    rgb_g.value(0)
    rgb_b.value(1)
    sleep(DELAY)

    # LED red + green
    print('LED: red & green')
    rgb_r.value(1)
    rgb_g.value(1)
    rgb_b.value(0)
    sleep(DELAY)

    # LED red + blue
    print('LED: red & blue')
    rgb_r.value(1)
    rgb_g.value(0)
    rgb_b.value(1)
    sleep(DELAY)

    # LED blue + green
    print('LED: blue & green')
    rgb_r.value(0)
    rgb_g.value(1)
    rgb_b.value(1)
    sleep(DELAY)

    # LED red + blue + green
    print('LED: red & blue & green')
    rgb_r.value(1)
    rgb_g.value(1)
    rgb_b.value(1)
    sleep(DELAY)
