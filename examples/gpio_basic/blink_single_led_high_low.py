from micropython import const
from machine import Pin
from utime import sleep


LED_GPIO_PIN = const(23)
DELAY_SECONDS = const(0.5)


if __name__ == '__main__':
    led = Pin(LED_GPIO_PIN, Pin.OUT)

    while True:
        print('[INFO] LED ON')
        led.value(1)
        sleep(DELAY_SECONDS)

        print('[INFO] LED OFF')
        led.value(0)
        sleep(DELAY_SECONDS)
