from micropython import const
from machine import Pin, ADC, SoftI2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms


ADC_PIN = const(32)
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
DISPLAY_SDA_PIN = const(21)
DISPLAY_SCL_PIN = const(22)
DURATION_MILLISECONDS = const(250)


def draw_on_screen(current_value: int) -> None:
    """
    draws graphic and text on display
    :param current_value: adc value as int
    :return: None
    """
    global oled

    oled.fill(0)

    rec_height = int(DISPLAY_HEIGHT / 2)
    rec_width = int(current_value * (DISPLAY_WIDTH / 65535))
    oled.fill_rect(0, 0, rec_width, rec_height, 1)

    volt = round(current_value * (3.3 / 65535), 2)
    txt = f'{volt} V - {current_value}'
    oled.text(txt, 0, 54)

    if float(volt) > 0.1:
        oled.show()


if __name__ == '__main__':
    adc = ADC(Pin(ADC_PIN, Pin.IN))
    adc.atten(ADC.ATTN_11DB)

    i2c = SoftI2C(sda=Pin(DISPLAY_SDA_PIN), scl=Pin(DISPLAY_SCL_PIN))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    while True:
        adc_val = adc.read_u16()
        draw_on_screen(adc_val)
        sleep_ms(DURATION_MILLISECONDS)
