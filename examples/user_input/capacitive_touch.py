from micropython import const
from machine import TouchPad, Pin
from utime import sleep


LED_PIN = const(23)
TOUCH_PIN = const(13)
TOUCH_MIN = const(100)


if __name__ == '__main__':
    led = Pin(LED_PIN, Pin.OUT)

    touch = TouchPad(Pin(TOUCH_PIN, Pin.IN))
    touch.config(250)

    while True:
        if touch.read() < TOUCH_MIN:
            led.value(1)
        else:
            led.value(0)

        sleep(0.5)
