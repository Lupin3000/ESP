from micropython import const
from machine import PWM, Pin
from utime import sleep


# define constants
LED_GPIO_PIN = const(23)
DELAY = const(0.005)
LED_FREQUENCY = const(5000)

# create pwm/pin objects
led = PWM(Pin(LED_GPIO_PIN))
led.freq(LED_FREQUENCY)

if __name__ == '__main__':
    while True:
        print('[INFO] Fade LED ON')
        for dc in range(0, 1023):
            led.duty(dc)
            sleep(DELAY)

        print('[INFO] Fade LED OFF')
        for dc in range(1023, 0, -1):
            led.duty(dc)
            sleep(DELAY)
