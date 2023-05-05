from micropython import const
from machine import Pin
from utime import sleep


BARRIER_GPIO_PIN = const(23)
DELAY = const(1)


if __name__ == '__main__':
    barrier = Pin(BARRIER_GPIO_PIN, Pin.IN, Pin.PULL_UP)

    while True:
        sleep(DELAY)
        if barrier.value():
            print(f'[INFO] light barrier interrupted')
        else:
            print(f'[INFO] light barrier not interrupted')
