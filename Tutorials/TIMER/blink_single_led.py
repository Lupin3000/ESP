from micropython import const
from machine import Pin, Timer


# define constants
LED_GPIO_PIN = const(23)
TIMER_PERIOD = const(500)

# set GPIO pin and virtual timer
led = Pin(LED_GPIO_PIN, Pin.OUT)
timer = Timer(-1)

# initialize timer
timer.init(period=TIMER_PERIOD, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))
