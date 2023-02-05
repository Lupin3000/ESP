from micropython import const
from machine import Pin
from utime import sleep_us, ticks_us, sleep

# define constants
TRIGGER_GPIO_PIN = const(23)
ECHO_GPIO_PIN = const(21)

# create pin objects
trigger = Pin(TRIGGER_GPIO_PIN, Pin.OUT)
echo = Pin(ECHO_GPIO_PIN, Pin.IN)

while True:
    trigger.value(0)
    sleep_us(2)
    trigger.value(1)
    sleep_us(10)
    trigger.value(0)

    while echo.value() == 0:
        pass

    ticks1 = ticks_us()

    while echo.value() == 1:
        pass

    ticks2 = ticks_us()
    value = (ticks2 - ticks1) / 58.0
    print(f'[INFO] distance measure is: {value:.2f} cm')
    sleep(2)
