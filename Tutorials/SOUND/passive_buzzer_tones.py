from micropython import const
from machine import Pin, PWM
from utime import sleep


# define constant
BUZZER_GPIO_PIN = const(23)
BUZZER_DUTY_CYCLE = const(1000)
BUZZER_FREQUENCY_TONE_A = const(300)
BUZZER_FREQUENCY_TONE_B = const(800)
BUZZER_FREQUENCY_TONE_C = const(400)
DELAY = const(.15)
REPEATS = const(5)

# create PWM object
buzzer = PWM(Pin(BUZZER_GPIO_PIN))

# define variable
count = 1

while count <= REPEATS:
    count += 1

    # play tone a
    buzzer.freq(BUZZER_FREQUENCY_TONE_A)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(DELAY)
    buzzer.duty_u16(0)

    # play tone b
    buzzer.freq(BUZZER_FREQUENCY_TONE_B)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(DELAY)
    buzzer.duty_u16(0)

    # play tone c
    buzzer.freq(BUZZER_FREQUENCY_TONE_C)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(DELAY)
    buzzer.duty_u16(0)
