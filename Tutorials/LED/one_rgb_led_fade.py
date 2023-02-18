from micropython import const
from machine import PWM, Pin
from utime import sleep


# define constants
LED_RED_GPIO_PIN = const(21)
LED_GREEN_GPIO_PIN = const(22)
LED_BLUE_GPIO_PIN = const(23)
LED_FREQUENCY = const(100)
DELAY = const(0.001)

# create pwm/pin objects & set frequencies
rgb_r = PWM(Pin(LED_RED_GPIO_PIN))
rgb_g = PWM(Pin(LED_GREEN_GPIO_PIN))
rgb_b = PWM(Pin(LED_BLUE_GPIO_PIN))
rgb_r.freq(LED_FREQUENCY)
rgb_g.freq(LED_FREQUENCY)
rgb_b.freq(LED_FREQUENCY)

if __name__ == '__main__':
    while True:
        print('[INFO] Fade LED ON')
        for dc in range(0, 1023):
            rgb_r.duty(dc)
            sleep(DELAY)

        for dc in range(0, 1023):
            rgb_g.duty(dc)
            sleep(DELAY)

        for dc in range(0, 1023):
            rgb_b.duty(dc)
            sleep(DELAY)

        print('[INFO] Fade LED OFF')
        for dc in range(1023, 0, -1):
            rgb_r.duty(dc)
            sleep(DELAY)

        for dc in range(1023, 0, -1):
            rgb_g.duty(dc)
            sleep(DELAY)

        for dc in range(1023, 0, -1):
            rgb_b.duty(dc)
            sleep(DELAY)
