from micropython import const
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from utime import sleep


DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
LINE_HEIGHT = const(9)
COLUMN_WIDTH = const(8)

MICROPYTHON_ICON = [
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
]


if __name__ == '__main__':
    i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    oled.fill(0)
    print('[INFO] Sequence 1')
    # rectangle (screen sequence 1)
    oled.rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)

    # icon (screen sequence 1)
    start_x = 12
    start_y = 12
    for y, row in enumerate(MICROPYTHON_ICON):
        for x, c in enumerate(row):
            oled.pixel(x + start_x, y + start_y, c)

    # text (screen sequence 1)
    oled.text('MicroPython', 30, 15)
    oled.show()
    sleep(1)

    print('[INFO] Sequence 2')
    # text (screen sequence 2)
    oled.text('on ESP32', 35, 35)
    oled.show()
    sleep(1)

    print('[INFO] Sequence 3')
    # flash (screen sequence 3)
    for i in range(10):
        oled.invert(1)
        sleep(0.1)
        oled.invert(0)
        sleep(0.1)

    print('[INFO] Sequence 4')
    # animation (screen sequence 4)
    for index in range(DISPLAY_WIDTH, -1, -1):
        oled.fill_rect(index, 0, 1, DISPLAY_HEIGHT, 0)
        oled.show()
        sleep(0.005)
