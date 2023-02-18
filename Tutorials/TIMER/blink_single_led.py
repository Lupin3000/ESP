from micropython import const
from machine import Pin, Timer


# define constants
LED_GPIO_PIN = const(23)
TIMER_PERIOD = const(500)

# create pin and virtual timer objects
led = Pin(LED_GPIO_PIN, Pin.OUT)
timer = Timer(-1)

if __name__ == '__main__':
    timer.init(period=TIMER_PERIOD, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))
