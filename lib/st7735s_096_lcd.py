from micropython import const
from machine import Pin, SPI, PWM
from framebuf import FrameBuffer, RGB565
from time import sleep_ms


class LCD(FrameBuffer):
    """
    MicroPython ESP32-S2 MCU Wi-Fi Development Board - 0.96inch 160x80 LCD driver
    https://www.waveshare.com/esp32-s2.htm

    The driver is based on MicroPython FrameBuffer as well as a smaller further development
    (cleanup, improvements, etc.) of the original example provided
    by WaveShare https://github.com/waveshare/Pico_code/blob/main/Python/Pico-LCD-0.96/pico-lcd-0.96.py

    Drawing primitive shapes
    To draw pixels, lines, rectangles, ellipses, polygons, text, etc. the standard FrameBuffer methods are available
    """

    LCD_CS = const(9)
    LCD_CLK = const(10)
    LCD_MOSI = const(11)
    LCD_DC = const(18)
    LCD_RST = const(21)
    LCD_BL = const(45)

    def __init__(self, width: int = 160, height: int = 80):
        """
        lcd constructor incl. SPI initialisation
        :param width: display width (default: 160px)
        :param height: display height (default: 80px)
        """
        self.width = int(width)
        self.height = int(height)

        self._cs = Pin(self.LCD_CS, Pin.OUT)
        self._dc = Pin(self.LCD_DC, Pin.OUT)
        self._rst = Pin(self.LCD_RST, Pin.OUT)
        self._bl = Pin(self.LCD_BL, Pin.OUT)
        self._buffer = bytearray(self.height * self.width * 2)
        self._pwm = PWM(Pin(self.LCD_BL))

        self._spi = SPI(1, 10000_000, polarity=0, phase=0, sck=Pin(self.LCD_CLK), mosi=Pin(self.LCD_MOSI), miso=None)

        self._cs(0)
        self._dc(1)

        super().__init__(self._buffer, self.width, self.height, RGB565)

        self._init_display()
        self._set_window(0, 0, self.width - 1, self.height - 1)

    def _write_cmd(self, cmd) -> None:
        """
        write commands to display
        :param cmd: hex number value
        :return: None
        """
        self._dc(0)
        self._cs(0)
        self._spi.write(bytearray([cmd]))

    def _write_data(self, buf) -> None:
        """
        write data to display
        :param buf: hex number value
        :return: None
        """
        self._dc(1)
        self._cs(0)
        self._spi.write(bytearray([buf]))
        self._cs(1)

    def _reset(self) -> None:
        """
        reset display
        :return: None
        """
        self._rst(1)
        sleep_ms(200)

        self._rst(0)
        sleep_ms(200)

        self._rst(1)
        sleep_ms(200)

    def _init_display(self) -> None:
        """
        initialize display
        :return: None
        """
        self._reset()
        self.backlight_on(1000)

        self._write_cmd(0x11)
        sleep_ms(120)

        self._write_cmd(0x21)
        self._write_cmd(0x21)
        self._write_cmd(0xB1)
        self._write_data(0x05)
        self._write_data(0x3A)
        self._write_data(0x3A)
        self._write_cmd(0xB2)
        self._write_data(0x05)
        self._write_data(0x3A)
        self._write_data(0x3A)
        self._write_cmd(0xB3)
        self._write_data(0x05)
        self._write_data(0x3A)
        self._write_data(0x3A)
        self._write_data(0x05)
        self._write_data(0x3A)
        self._write_data(0x3A)
        self._write_cmd(0xB4)
        self._write_data(0x03)
        self._write_cmd(0xC0)
        self._write_data(0x62)
        self._write_data(0x02)
        self._write_data(0x04)
        self._write_cmd(0xC1)
        self._write_data(0xC0)
        self._write_cmd(0xC2)
        self._write_data(0x0D)
        self._write_data(0x00)
        self._write_cmd(0xC3)
        self._write_data(0x8D)
        self._write_data(0x6A)
        self._write_cmd(0xC4)
        self._write_data(0x8D)
        self._write_data(0xEE)
        self._write_cmd(0xC5)
        self._write_data(0x0E)
        self._write_cmd(0xE0)
        self._write_data(0x10)
        self._write_data(0x0E)
        self._write_data(0x02)
        self._write_data(0x03)
        self._write_data(0x0E)
        self._write_data(0x07)
        self._write_data(0x02)
        self._write_data(0x07)
        self._write_data(0x0A)
        self._write_data(0x12)
        self._write_data(0x27)
        self._write_data(0x37)
        self._write_data(0x00)
        self._write_data(0x0D)
        self._write_data(0x0E)
        self._write_data(0x10)
        self._write_cmd(0xE1)
        self._write_data(0x10)
        self._write_data(0x0E)
        self._write_data(0x03)
        self._write_data(0x03)
        self._write_data(0x0F)
        self._write_data(0x06)
        self._write_data(0x02)
        self._write_data(0x08)
        self._write_data(0x0A)
        self._write_data(0x13)
        self._write_data(0x26)
        self._write_data(0x36)
        self._write_data(0x00)
        self._write_data(0x0D)
        self._write_data(0x0E)
        self._write_data(0x10)
        self._write_cmd(0x3A)
        self._write_data(0x05)
        self._write_cmd(0x36)
        self._write_data(0xA8)
        self._write_cmd(0x29)

    def _set_window(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        """
        set display window
        :param x_start: start x-position for window
        :param y_start: start y-position for window
        :param x_end: end x-position for window
        :param y_end: end y-position for window
        :return: None
        """
        pos_x_start = int(x_start) + 1
        pos_x_end = int(x_end) + 1
        pos_y_start = int(y_start) + 26
        pos_y_end = int(y_end) + 26

        self._write_cmd(0x2A)
        self._write_data(0x00)
        self._write_data(pos_x_start)
        self._write_data(0x00)
        self._write_data(pos_x_end)
        self._write_cmd(0x2B)
        self._write_data(0x00)
        self._write_data(pos_y_start)
        self._write_data(0x00)
        self._write_data(pos_y_end)
        self._write_cmd(0x2C)

    def backlight_off(self) -> None:
        """
        turn display backlight off
        :return: None
        """
        self._pwm.freq(1)
        self._pwm.duty_u16(0)

    def backlight_on(self, value: int) -> None:
        """
        turn display backlight on by value
        :param value: integer between 1 and 1000
        :return: None
        """
        val = int(value)

        self._pwm.freq(1000)

        if val <= 0:
            val = 1

        if val >= 1000:
            val = 1000

        data = int((val * 65536 / 1000) - 1)
        self._pwm.duty_u16(data)

    def show(self) -> None:
        """
        show content on display
        :return: None
        """
        self._set_window(0, 0, self.width - 1, self.height - 1)
        self._dc(1)
        self._cs(0)
        self._spi.write(self._buffer)
        self._cs(1)

    @staticmethod
    def rgb_color(red: int, green: int, blue: int):
        """
        convert RGB888 to RGB565
        :param red: value for red (0 - 255)
        :param green: value for green (0 - 255)
        :param blue: value for blue (0 - 255)
        :return: RGB565 value
        """
        r = int(red)
        g = int(green)
        b = int(blue)

        return (((g & 0b00011100) << 3) + ((r & 0b11111000) >> 3) << 8) + (b & 0b11111000) + ((g & 0b11100000) >> 5)
