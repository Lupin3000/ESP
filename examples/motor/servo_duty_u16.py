from micropython import const
from machine import Pin, PWM
from utime import sleep


SERVO_GPIO_PIN = const(21)
SERVO_FREQUENCY = const(50)
DELAY = const(1)


if __name__ == '__main__':
    servo = PWM(Pin(SERVO_GPIO_PIN), freq=SERVO_FREQUENCY)

    # define variables (between 3276 and 6553)
    min_pos = 3276
    mid_pos = 4915
    max_pos = 6553

    while True:
        # reset to middle
        print('[INFO] reset to middle position')
        servo.duty_u16(mid_pos)
        sleep(DELAY)

        for pos in (min_pos, mid_pos, max_pos):
            print(f'[INFO] set position {pos}')
            servo.duty_u16(pos)
            sleep(DELAY)
