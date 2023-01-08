from machine import PWM, Pin
from utime import sleep_us


# create constants
DELAY_MAIN = 300
DELAY_LOW = 1000
DELAY_END = 500000

# create PWM object with GPIO pin
led = PWM(Pin(23))
led.freq(5000)

while True:
    # LED Fade ON (main beat)
    print('LED: Fade ON (main beat)')
    for dc in range(0, 1023):
        led.duty(dc)
        sleep_us(DELAY_MAIN)

    # LED Fade OFF (main beat)
    print('LED: Fade OFF (main beat)')
    for dc in range(1023, 0, -1):
        led.duty(dc)
        sleep_us(DELAY_MAIN)

    # LED Fade ON (low beat)
    print('LED: Fade ON (low beat)')
    for dc in range(0, 1023):
        led.duty(dc)
        sleep_us(DELAY_LOW)

    # LED Fade OFF (low beat)
    print('LED: Fade OFF (low beat)')
    for dc in range(1023, 0, -1):
        led.duty(dc)
        sleep_us(DELAY_LOW)

    led.duty(0)
    sleep_us(DELAY_END)
