from micropython import const
from machine import Pin


LED_GPIO_PIN = const(23)
BUTTON_GPIO_PIN = const(22)


def interrupt_handler(pin) -> None:
    """
    count and toggle led high/low
    :param pin: class pin
    :return: None
    """
    global count
    global led

    count += 1
    print(f'[INFO] LED switch {count} by {pin}')
    led.value(not led.value())


if __name__ == '__main__':
    count = 0

    led = Pin(LED_GPIO_PIN, Pin.OUT, value=0)
    btn = Pin(BUTTON_GPIO_PIN, Pin.IN, Pin.PULL_UP)

    btn.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_handler)
