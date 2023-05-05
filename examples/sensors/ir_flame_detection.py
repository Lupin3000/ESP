from micropython import const
from machine import Pin, RTC
from utime import sleep


FLAME_GPIO_PIN = const(23)
LED_GPIO_PIN = const(21)
DETECTION_DELAY = const(0.25)


if __name__ == '__main__':
    rtc = RTC()
    flame = Pin(FLAME_GPIO_PIN, Pin.IN)
    led = Pin(LED_GPIO_PIN, Pin.OUT)

    while True:
        sleep(DETECTION_DELAY)

        if flame.value() == 0:
            tuple_rtc = rtc.datetime()
            str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
            str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'
            led.value(1)
            print(f'[INFO] Alert flame detected {str_date} {str_time}')
        else:
            led.value(0)
