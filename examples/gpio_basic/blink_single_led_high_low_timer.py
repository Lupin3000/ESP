from micropython import const
from machine import Pin, Timer


LED_GPIO_PIN = const(23)
TIMER_PERIOD = const(500)


if __name__ == '__main__':
    led = Pin(LED_GPIO_PIN, Pin.OUT)
    timer = Timer(-1)

    timer.init(period=TIMER_PERIOD, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))
