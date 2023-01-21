from micropython import const
from machine import TouchPad, Pin
from utime import sleep


# define constant
LED_GPIO = const(23)
TOUCH_GPIO = const(13)
TOUCH_MIN = const(100)

# define variables
led_status = False
led_pin = Pin(LED_GPIO, Pin.OUT)
touch_pin = TouchPad(Pin(TOUCH_GPIO))


def toggle_led() -> None:
    global led_status

    if not led_status:
        print('[INFO] LED ON')
        led_pin.value(1)
        led_status = True
    else:
        print('[INFO] LED OFF')
        led_pin.value(0)
        led_status = False


while True:
    touch_value = touch_pin.read()

    if int(touch_value) < TOUCH_MIN:
        print(f'[INFO] Touch value {touch_value}')
        toggle_led()
        sleep(0.5)
