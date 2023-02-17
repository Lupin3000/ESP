from micropython import const
from machine import TouchPad, Pin
from utime import sleep


# define constants
LED_GPIO_PIN = const(23)
TOUCH_GPIO_PIN = const(13)
TOUCH_MIN = const(100)
TOUCH_DELAY = const(0.5)


def toggle_led() -> None:
    """
    Toggle LED by current status
    :return: None
    """
    global led_status
    global led

    if not led_status:
        print('[INFO] LED ON')
        led.value(1)
        led_status = True
    else:
        print('[INFO] LED OFF')
        led.value(0)
        led_status = False


# set GPIO pins
led = Pin(LED_GPIO_PIN, Pin.OUT)
touch = TouchPad(Pin(TOUCH_GPIO_PIN))

# define variable
led_status = False

while True:
    touch_value = touch.read()

    if int(touch_value) < TOUCH_MIN:
        print(f'[INFO] Touch value is {touch_value}')
        toggle_led()
        sleep(TOUCH_DELAY)
