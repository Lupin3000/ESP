from micropython import const
from machine import Pin
from utime import sleep_ms


LED_GPIO_PIN = const(23)
BUTTON_GPIO_PIN = const(22)
DELAY_MILLISECONDS = const(10)


def toggle_led() -> None:
    """
    toggle led high/low
    :return: None
    """
    global led

    led.value(not led.value())


if __name__ == '__main__':
    count = 0
    led = Pin(LED_GPIO_PIN, Pin.OUT, value=0)
    btn = Pin(BUTTON_GPIO_PIN, Pin.IN, Pin.PULL_UP)

    while True:
        if not btn.value():
            count += 1
            print(f'[INFO] Button pressed {count}')
            toggle_led()

        sleep_ms(DELAY_MILLISECONDS)
