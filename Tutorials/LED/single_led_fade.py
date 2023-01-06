from machine import PWM, Pin
from time import sleep


# create PWM object with GPIO pin
led = PWM(Pin(23))
led.freq(5000)
delay = 0.005

while True:
    # LED Fade ON
    print('LED Fade ON')
    for dc in range(0, 1023):
        led.duty(dc)
        sleep(delay)

    # LED Fade OFF
    print('LED Fade OFF')
    for dc in range(1023, 0, -1):
        led.duty(dc)
        sleep(delay)
