from micropython import const
from machine import Pin, PWM
from utime import sleep


# define constant
BUZZER_GPIO_PIN = const(23)
BUZZER_FREQUENCY = const(1000)
BUZZER_DUTY_CYCLE = const(1000)
DELAY = const(1)

# create PWM object
buzzer = PWM(Pin(BUZZER_GPIO_PIN))

# play sound
buzzer.freq(BUZZER_FREQUENCY)
buzzer.duty_u16(BUZZER_DUTY_CYCLE)
sleep(DELAY)

# stop sound
buzzer.duty_u16(0)
