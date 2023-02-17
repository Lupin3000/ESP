from micropython import const
from machine import TouchPad, Pin
from utime import sleep


# define constants
LED_RED_GPIO_PIN = const(21)
LED_GREEN_GPIO_PIN = const(22)
LED_BLUE_GPIO_PIN = const(23)
TOUCH_GPIO_PIN = const(13)
TOUCH_MIN = const(100)
TOUCH_DELAY = const(0.5)


def toggle_leds() -> None:
    """
    Toggle LED's by count
    :return: None
    """
    global led_red
    global led_green
    global led_blue
    global led_counter_on

    if led_counter_on == 0:
        print('[INFO] Blue LED ON')
        led_blue.value(1)
        led_counter_on += 1
    elif led_counter_on == 1:
        print('[INFO] Green LED ON')
        led_green.value(1)
        led_counter_on += 1
    elif led_counter_on == 2:
        print('[INFO] Red LED ON')
        led_red.value(1)
        led_counter_on += 1
    else:
        print('[INFO] All LEDs OFF')
        led_blue.value(0)
        led_green.value(0)
        led_red.value(0)
        led_counter_on = 0


# set GPIO pins
led_red = Pin(LED_RED_GPIO_PIN, Pin.OUT)
led_green = Pin(LED_GREEN_GPIO_PIN, Pin.OUT)
led_blue = Pin(LED_BLUE_GPIO_PIN, Pin.OUT)
touch = TouchPad(Pin(TOUCH_GPIO_PIN))

# define variables
led_counter_on = 0

while True:
    touch_value = touch.read()

    if int(touch_value) < TOUCH_MIN:
        print(f'[INFO] Touch value {touch_value}')
        toggle_leds()
        sleep(TOUCH_DELAY)
