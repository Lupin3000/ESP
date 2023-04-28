from micropython import const
from machine import Pin, PWM
from utime import sleep


BUZZER_GPIO_PIN = const(23)
BUZZER_FREQUENCY = const(1000)
BUZZER_DUTY_CYCLE = const(1000)
DELAY_SECONDS = const(2)


if __name__ == '__main__':
    buzzer = PWM(Pin(BUZZER_GPIO_PIN))

    print('[INFO] play noisy tone')
    buzzer.freq(BUZZER_FREQUENCY)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(DELAY_SECONDS)

    buzzer.duty_u16(0)
