from micropython import const
from machine import TouchPad, Pin
from utime import sleep


# define constant
LED_GPIO_BLUE = const(23)
LED_GPIO_GREEN = const(22)
LED_GPIO_RED = const(21)
TOUCH_GPIO = const(13)
TOUCH_MIN = const(100)

# define variables
led_on_count = 0
led_pin_blue = Pin(LED_GPIO_BLUE, Pin.OUT)
led_pin_green = Pin(LED_GPIO_GREEN, Pin.OUT)
led_pin_red = Pin(LED_GPIO_RED, Pin.OUT)
touch_pin = TouchPad(Pin(TOUCH_GPIO))


def toggle_leds() -> None:
    global led_on_count
    global led_pin_blue
    global led_pin_green
    global led_pin_red

    if led_on_count == 0:
        print('[INFO] Blue LED ON')
        led_pin_blue.value(1)
        led_on_count += 1
    elif led_on_count == 1:
        print('[INFO] Green LED ON')
        led_pin_green.value(1)
        led_on_count += 1
    elif led_on_count == 2:
        print('[INFO] Red LED ON')
        led_pin_red.value(1)
        led_on_count += 1
    else:
        print('[INFO] All LEDs OFF')
        led_pin_blue.value(0)
        led_pin_green.value(0)
        led_pin_red.value(0)
        led_on_count = 0


while True:
    touch_value = touch_pin.read()

    if int(touch_value) < TOUCH_MIN:
        print(f'[INFO] Touch value {touch_value}')
        toggle_leds()
        sleep(0.5)
