from micropython import const
from machine import Pin
from utime import sleep_ms


# define constants
LED_GPIO_PIN = const(23)
BUTTON_GPIO_PIN = const(22)
DELAY = const(10)

# create pin objects
led = Pin(LED_GPIO_PIN, Pin.OUT)
btn = Pin(BUTTON_GPIO_PIN, Pin.IN, Pin.PULL_UP)

if __name__ == '__main__':
    while True:
        if not btn.value():
            print('[INFO] Button pressed')
            led.value(1)
        else:
            print('[INFO] Button released')
            led.value(0)

        sleep_ms(DELAY)
