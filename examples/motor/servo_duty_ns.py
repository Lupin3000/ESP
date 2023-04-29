from micropython import const
from machine import Pin, PWM
from utime import sleep


SERVO_GPIO_PIN = const(21)
SERVO_FREQUENCY = const(50)
DELAY = const(1)


if __name__ == '__main__':
    servo = PWM(Pin(SERVO_GPIO_PIN), freq=SERVO_FREQUENCY)

    # define variables (between 1000000 and 2000000)
    min_pos = 1000000
    mid_pos = 1500000
    max_pos = 2000000

    while True:
        # reset to middle
        print('[INFO] reset to middle position')
        servo.duty_ns(mid_pos)
        sleep(DELAY)

        for pos in (min_pos, mid_pos, max_pos):
            print(f'[INFO] set position {pos}')
            servo.duty_ns(pos)
            sleep(DELAY)
