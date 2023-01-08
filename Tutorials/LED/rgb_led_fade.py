from machine import PWM, Pin
from utime import sleep


# declare constant
DELAY = 0.001
FREQUENCE = 100

# declare PWM and Pins
rgb_r = PWM(Pin(21))
rgb_g = PWM(Pin(22))
rgb_b = PWM(Pin(23))

rgb_r.freq(FREQUENCE)
rgb_g.freq(FREQUENCE)
rgb_b.freq(FREQUENCE)

while True:
    # LED Fade ON
    print('LED: Fade ON')
    for dc in range(0, 1023):
        rgb_r.duty(dc)
        sleep(DELAY)

    for dc in range(0, 1023):
        rgb_g.duty(dc)
        sleep(DELAY)

    for dc in range(0, 1023):
        rgb_b.duty(dc)
        sleep(DELAY)

    # LED Fade OFF
    print('LED: Fade OFF')
    for dc in range(1023, 0, -1):
        rgb_r.duty(dc)
        sleep(DELAY)

    for dc in range(1023, 0, -1):
        rgb_g.duty(dc)
        sleep(DELAY)

    for dc in range(1023, 0, -1):
        rgb_b.duty(dc)
        sleep(DELAY)
