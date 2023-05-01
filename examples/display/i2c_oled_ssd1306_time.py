from micropython import const
from machine import Pin, SoftI2C, RTC
from ssd1306 import SSD1306_I2C
import freesans20
import writer
from utime import sleep


DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
DISPLAY_SDA_PIN = const(21)
DISPLAY_SCL_PIN = const(22)
DISPLAY_DELAY = const(1)


def get_date_time() -> tuple:
    """
    convert and returns formatted date/time
    :return: tuple of strings for date and time
    """
    tuple_rtc = rtc.datetime()
    str_date = f'{tuple_rtc[2]:02d}.{tuple_rtc[1]:02d}.{tuple_rtc[0]}'
    str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'

    return str_date, str_time


if __name__ == '__main__':
    rtc = RTC()
    i2c = SoftI2C(sda=Pin(DISPLAY_SDA_PIN), scl=Pin(DISPLAY_SCL_PIN))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    font_writer = writer.Writer(oled, freesans20)

    while True:
        oled.fill(0)
        current_date, current_time = get_date_time()

        current_date_len = font_writer.stringlen(current_date)
        font_writer.set_textpos(30 + (64 - current_date_len) // 2, 10)
        font_writer.printstring(current_date)

        current_time_len = font_writer.stringlen(current_time)
        font_writer.set_textpos(40 + (64 - current_date_len) // 2, 35)
        font_writer.printstring(current_time)

        oled.show()
        sleep(DISPLAY_DELAY)
