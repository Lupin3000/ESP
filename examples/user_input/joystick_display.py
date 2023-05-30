from micropython import const
from machine import Pin, ADC, SPI
from lib.sh1106 import SH1106_SPI
from utime import sleep_ms


GPIO_ADC_X_PIN = const(32)
GPIO_ADC_Y_PIN = const(33)
GPIO_BUTTON_PIN = const(35)

GPIO_SDA_PIN = const(23)
GPIO_SCL_PIN = const(18)
GPIO_DC_PIN = const(2)
GPIO_RES_PIN = const(4)
GPIO_CS_PIN = const(5)

DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)


class Display:
    def __init__(self):
        """
        display constructor
        """
        spi = SPI(1, baudrate=1000000, sck=Pin(GPIO_SCL_PIN), mosi=Pin(GPIO_SDA_PIN))

        self.oled = SH1106_SPI(width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, spi=spi, rotate=0, delay=0,
                               dc=Pin(GPIO_DC_PIN), res=Pin(GPIO_RES_PIN), cs=Pin(GPIO_CS_PIN))

        self.width = DISPLAY_WIDTH
        self.height = DISPLAY_HEIGHT

    def draw_on_screen(self, x: int, y: int) -> None:
        """
        draw pixel on screen by x/y coordinates
        :param x: value for x-coordinate
        :param y: value for y-coordinate
        :return: None
        """
        self.oled.pixel(x, y, 1)

    def draw_circle(self, x_pos: int, y_pos: int, rad: int) -> None:
        """
        calculate circle by x/y coordinate (middle) and radius
        :param x_pos: value for x-coordinate
        :param y_pos: value for y-coordinate
        :param rad: value for radius
        :return: None
        """
        x = rad - 1
        y = 0
        dx = 1
        dy = 1
        err = dx - (rad << 1)

        while x >= y:
            if err <= 0:
                y += 1
                err += dy
                dy += 2

            if err > 0:
                x -= 1
                dx += 2
                err += dx - (rad << 1)

            self.draw_on_screen(x_pos + x, y_pos + y)
            self.draw_on_screen(x_pos + y, y_pos + x)
            self.draw_on_screen(x_pos - y, y_pos + x)
            self.draw_on_screen(x_pos - x, y_pos + y)
            self.draw_on_screen(x_pos - x, y_pos - y)
            self.draw_on_screen(x_pos - y, y_pos - x)
            self.draw_on_screen(x_pos + y, y_pos - x)
            self.draw_on_screen(x_pos + x, y_pos - y)


class Joystick:
    def __init__(self):
        """
        joystick constructor
        """
        self.adc_x = ADC(Pin(GPIO_ADC_X_PIN, Pin.IN))
        self.adc_x.atten(ADC.ATTN_11DB)

        self.adc_y = ADC(Pin(GPIO_ADC_Y_PIN, Pin.IN))
        self.adc_y.atten(ADC.ATTN_11DB)

    def get_raw_analog_values(self) -> tuple:
        """
        return tuple of current x/y raw analog values
        :return: tuple
        """
        adc_x_val = self.adc_x.read_u16()
        adc_y_val = self.adc_y.read_u16()

        return adc_x_val, adc_y_val

    def get_xy_coordinates(self) -> tuple:
        """
        return tuple of from raw value converted x/y values
        :return: tuple
        """
        x, y = self.get_raw_analog_values()

        x_pos = int(x * (DISPLAY_WIDTH / 65535))

        if x_pos <= 5:
            x_pos = 5

        if x_pos >= (DISPLAY_WIDTH - 6):
            x_pos = (DISPLAY_WIDTH - 6)

        y_pos = int(y * (DISPLAY_HEIGHT / 65535))

        if y_pos <= 5:
            y_pos = 5

        if y_pos >= (DISPLAY_HEIGHT - 6):
            y_pos = (DISPLAY_HEIGHT - 6)

        return x_pos, y_pos


if __name__ == '__main__':
    display = Display()
    joystick = Joystick()

    while True:
        ch_x_pos, cs_y_pos = joystick.get_xy_coordinates()

        display.oled.fill(0)
        display.oled.rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)
        display.oled.text(f'X:{ch_x_pos} Y:{cs_y_pos} B:{Pin(GPIO_BUTTON_PIN, Pin.IN).value()}', 3, 3, 1)

        display.draw_circle(ch_x_pos, cs_y_pos, 4)

        for i in range(-5, 5, 1):
            if i < 0:
                display.draw_on_screen(ch_x_pos - i, cs_y_pos)
                display.draw_on_screen(ch_x_pos, cs_y_pos - i)
            if i == 0:
                display.draw_on_screen(ch_x_pos, cs_y_pos)
            if i < 0:
                display.draw_on_screen(ch_x_pos + i, cs_y_pos)
                display.draw_on_screen(ch_x_pos, cs_y_pos + i)

        display.oled.show()

        sleep_ms(100)
