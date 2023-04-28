from micropython import const
from machine import PWM, Pin
from utime import sleep_ms


LED_GPIO_PIN = const(23)
DELAY_MILLISECONDS = const(5)
LED_FREQUENCY = const(5000)


if __name__ == '__main__':
    led = PWM(Pin(LED_GPIO_PIN))
    led.freq(LED_FREQUENCY)

    while True:
        print('[INFO] Fade LED ON')
        for item in range(0, 1023):
            led.duty(item)
            sleep_ms(DELAY_MILLISECONDS)

        print('[INFO] Fade LED OFF')
        for item in range(1023, 0, -1):
            led.duty(item)
            sleep_ms(DELAY_MILLISECONDS)
