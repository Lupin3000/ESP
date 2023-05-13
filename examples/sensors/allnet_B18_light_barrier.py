from micropython import const
from machine import Pin
from utime import ticks_ms, time, localtime
from ntptime import settime
import urequests


UTC_OFFSET = const(7200)
BARRIER_GPIO_PIN = const(23)
PUSHOVER_TOKEN = 'YOUR PUSHOVER TOKEN'
PUSHOVER_USER_KEY = 'YOUR PUSHOVER USER KEY'


def irq_handler(pin) -> None:
    """
    irq handler
    :param pin: pin object
    :return: None
    """
    global last_time

    new_time = ticks_ms()

    if (new_time - last_time) > 500:
        last_time = new_time

        msg = f"token={PUSHOVER_TOKEN}&user={PUSHOVER_USER_KEY}"
        msg += f"&title=Alert&message=Light Barrier Interrupted"
        msg += f"&sound=siren&timestamp={time()}"

        r = urequests.post(url="https://api.pushover.net/1/messages.json", data=msg)
        print(f'[INFO] Response: {r.text}')
        r.close()


if __name__ == '__main__':
    last_time = 0

    try:
        settime()
    except Exception as t_err:
        print(f'[ERROR] Connection to NTP server failed: {t_err}')

    actual = localtime(time() + UTC_OFFSET)

    barrier = Pin(BARRIER_GPIO_PIN, Pin.IN, Pin.PULL_DOWN)
    barrier.irq(handler=irq_handler, trigger=Pin.IRQ_RISING)
