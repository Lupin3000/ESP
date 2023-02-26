from micropython import const
from machine import Pin
from utime import sleep


# define constants
BARRIER_GPIO_PIN = const(23)
DELAY = const(1)


def light_interrupt() -> None:
    """
    Print out interruption of light barrier
    :return: None
    """
    print(f'[INFO] light barrier interrupted')


# create pin objects
barrier = Pin(BARRIER_GPIO_PIN, Pin.IN, Pin.PULL_UP)

if __name__ == '__main__':
    while True:
        sleep(DELAY)
        if barrier.value():
            light_interrupt()
