from micropython import const
from machine import Pin, ADC, SoftI2C
from ssd1306 import SSD1306_I2C
from writer import Writer
import freesans20
from utime import sleep_ms


SDA_GPIO_PIN = const(21)
SCL_GPIO_PIN = const(22)
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
ADC_GPIO_PIN = const(34)
DELAY_MILLISECONDS = const(500)


class Display:
    def __init__(self):
        """
        constructor for display
        """
        i2c = SoftI2C(sda=Pin(SDA_GPIO_PIN), scl=Pin(SCL_GPIO_PIN))

        self.display = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
        self.width = DISPLAY_WIDTH
        self.height = DISPLAY_HEIGHT

        self.font_writer = Writer(self.display, freesans20)

    def draw_screen(self, value: str) -> None:
        """
        show value on oled screen
        :param value: string to print on screen
        :return: None
        """
        self.display.fill(0)

        current_len = self.font_writer.stringlen(str(value))
        self.font_writer.set_textpos(25 + (DISPLAY_HEIGHT - current_len) // 2, 20)
        self.font_writer.printstring(str(value))

        self.display.show()


class Microphone:
    def __init__(self):
        """
        constructor for microphone
        """
        self.mic = ADC(Pin(ADC_GPIO_PIN))
        self.mic.width(ADC.WIDTH_10BIT)
        self.mic.atten(ADC.ATTN_11DB)

    def get_decibels(self) -> int:
        """
        get current db value from microphone
        :return: db as integer
        """
        return int((self.mic.read() - 0) * (90 - 10) / (1023 - 0) + 10)


if __name__ == '__main__':
    oled = Display()
    mic = Microphone()

    while True:
        db_value = f'{mic.get_decibels()} db'
        oled.draw_screen(value=db_value)
        sleep_ms(DELAY_MILLISECONDS)
