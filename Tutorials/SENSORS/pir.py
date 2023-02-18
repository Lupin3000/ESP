from micropython import const
from machine import Pin
from utime import sleep


# define constants
PIR_GPIO_PIN = const(23)
DELAY_INITIAL = const(30)
DELAY_MOTION = const(5)
DELAY_NO_MOTION = const(1)


def motion_detect(motion: int) -> None:
    """
    Print motion status and sleep
    :param motion: int
    :return: None
    """
    global count

    if motion == 1:
        count += 1
        print(f'[INFO] {count}. motion detected')
        sleep(DELAY_MOTION)
    else:
        print("[INFO] no motion detected")
        sleep(DELAY_NO_MOTION)


# create pin object
pir = Pin(PIR_GPIO_PIN, Pin.IN, Pin.PULL_DOWN)

if __name__ == '__main__':
    print(f'[INFO] warm-up pir sensor for {DELAY_INITIAL} seconds')
    sleep(DELAY_INITIAL)

    print('[INFO] start pir sensor')
    count = 0

    while True:
        status = pir.value()
        motion_detect(status)
