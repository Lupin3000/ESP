from micropython import const
from machine import Pin, RTC
from utime import sleep_ms


DATA_GPIO_PIN = const(23)
DELAY = const(500)


if __name__ == '__main__':
    detection = Pin(DATA_GPIO_PIN, Pin.IN)
    rtc = RTC()

    while True:
        if not detection.value():
            tuple_rtc = rtc.datetime()
            str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
            str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'
            print(f'[INFO] Obstacle detection {str_date} - {str_time}')
        sleep_ms(DELAY)
