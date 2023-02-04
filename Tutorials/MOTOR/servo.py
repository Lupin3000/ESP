from micropython import const
from machine import Pin, PWM
from utime import sleep


# define constants
SERVO_GPIO_PIN = const(21)
SERVO_FREQUENCY = const(50)
DELAY = const(5)

# create PWM object
servo = PWM(Pin(SERVO_GPIO_PIN), freq=SERVO_FREQUENCY)

# define variables between 52 and 102
min_pos = 52
mid_pos = 77
max_pos = 102

while True:
    # reset to middle
    servo.duty(mid_pos)
    sleep(DELAY)

    for pos in (min_pos, mid_pos, max_pos):
        print(pos)
        servo.duty(pos)
        sleep(DELAY)
