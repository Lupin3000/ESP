from machine import PWM, Pin
from utime import sleep_us


# create PWM object with GPIO pin
led = PWM(Pin(23))
led.freq(5000)

# create variables
delay_main = 300
delay_low = 1000

while True:
    # main beat
    for dc in range(0, 1023):
        led.duty(dc)
        sleep_us(delay_main)

    for dc in range(1023, 0, -1):
        led.duty(dc)
        sleep_us(delay_main)

    # low beat
    for dc in range(0, 1023):
        led.duty(dc)
        sleep_us(delay_low)

    for dc in range(1023, 0, -1):
        led.duty(dc)
        sleep_us(delay_low)

    led.duty(0)
    sleep_us(500000)
