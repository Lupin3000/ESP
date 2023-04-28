from micropython import const
from machine import Pin, PWM


LED_GPIO_PIN = const(23)
FREQUENCY = const(1)
DUTY_CYCLE = const(512)


if __name__ == '__main__':
    pwm_led = PWM(Pin(LED_GPIO_PIN), freq=FREQUENCY, duty=DUTY_CYCLE)
