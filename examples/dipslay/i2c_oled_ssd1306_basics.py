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


def scroll_vertical_in_out(content: list) -> None:
    """
    scrolls the content from top to down
    :param content: list of different strings per row to display
    :return: None
    """
    global oled

    for item in range(0, (DISPLAY_HEIGHT * 2 + 1), 1):
        for line in content:
            oled.text(line[2], line[0], -DISPLAY_HEIGHT + item + line[1])
        oled.show()
        if item != DISPLAY_HEIGHT:
            oled.fill(0)


if __name__ == '__main__':
    i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    oled.fill(0)
    print('[INFO] Sequence 1')
    oled.rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)

    start_x = 12
    start_y = 12
    for y, row in enumerate(MICROPYTHON_ICON):
        for x, c in enumerate(row):
            oled.pixel(x + start_x, y + start_y, c)

    oled.text('MicroPython', 30, 15)
    oled.show()
    sleep(1)

    print('[INFO] Sequence 2')
    oled.text('on ESP32', 35, 35)
    oled.show()
    sleep(1)

    print('[INFO] Sequence 3')
    for i in range(10):
        oled.invert(1)
        sleep(0.1)
        oled.invert(0)
        sleep(0.1)

    print('[INFO] Sequence 4')
    for index in range(DISPLAY_WIDTH, -1, -1):
        oled.fill_rect(index, 0, 1, DISPLAY_HEIGHT, 0)
        oled.show()
        sleep(0.005)

    oled.fill(0)

    print('[INFO] Sequence 5')
    text_1 = "Damien P. George"
    text_2 = "many thanks to"
    text_3 = "All honor and"
    screen = [[0, 0, text_1], [0, 16, text_2], [0, 32, text_3]]

    scroll_vertical_in_out(screen)
