from micropython import const
from machine import PWM, Pin
from utime import sleep_us


# define constants
LED_GPIO_PIN = const(23)
LED_FREQUENCY = const(5000)
DELAY_MAIN = const(300)
DELAY_LOW = const(1000)
DELAY_END = const(500000)

# create pwm/pin objects
led = PWM(Pin(LED_GPIO_PIN))
led.freq(LED_FREQUENCY)

if __name__ == '__main__':
    while True:
        print('[INFO] Fade LED ON (main beat)')
        for dc in range(0, 1023):
            led.duty(dc)
            sleep_us(DELAY_MAIN)

        print('[INFO] Fade LED OFF (main beat)')
        for dc in range(1023, 0, -1):
            led.duty(dc)
            sleep_us(DELAY_MAIN)

        print('[INFO] Fade LED ON (low beat)')
        for dc in range(0, 1023):
            led.duty(dc)
            sleep_us(DELAY_LOW)

        print('[INFO] Fade LED OFF (low beat)')
        for dc in range(1023, 0, -1):
            led.duty(dc)
            sleep_us(DELAY_LOW)

        led.duty(0)
        sleep_us(DELAY_END)
