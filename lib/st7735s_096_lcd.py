from micropython import const
from machine import Pin, SPI, PWM
from framebuf import FrameBuffer, RGB565
from time import sleep


class LCD(FrameBuffer):
    """
    MicroPython ESP32-S2 MCU Wi-Fi Development Board - 0.96inch 160x80 LCD driver
    https://www.waveshare.com/esp32-s2.htm

    The driver is based on MicroPython FrameBuffer as well as
    a smaller further development (cleanup) of the original example provided
    by WaveShare https://github.com/waveshare/Pico_code/blob/main/Python/Pico-LCD-0.96/pico-lcd-0.96.py
    """

    LCD_CS = const(9)
    LCD_CLK = const(10)
    LCD_MOSI = const(11)
    LCD_DC = const(18)
    LCD_RST = const(21)
    LCD_BL = const(45)

    def __init__(self):
        self.width = 160
        self.height = 80

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
        self.init_display()
        self.set_window(0, 0, self.width - 1, self.height - 1)

    def write_cmd(self, cmd):
        self._dc(0)
        self._cs(0)
        self._spi.write(bytearray([cmd]))

    def write_data(self, buf):
        self._dc(1)
        self._cs(0)
        self._spi.write(bytearray([buf]))
        self._cs(1)

    def reset(self):
        self._rst(1)
        sleep(0.2)
        self._rst(0)
        sleep(0.2)
        self._rst(1)
        sleep(0.2)

    def backlight_off(self):
        self._pwm.freq(1)
        self._pwm.duty_u16(0)

    def backlight_on(self, value):
        self._pwm.freq(1000)

        if value <= 0:
            value = 1
        if value >= 1000:
            value = 1000

        data = int((value * 65536 / 1000) - 1)
        self._pwm.duty_u16(data)

    def init_display(self):
        self.reset()
        self.backlight_on(1000)

        self.write_cmd(0x11)
        sleep(0.12)

        self.write_cmd(0x21)
        self.write_cmd(0x21)
        self.write_cmd(0xB1)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB2)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB3)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB4)
        self.write_data(0x03)
        self.write_cmd(0xC0)
        self.write_data(0x62)
        self.write_data(0x02)
        self.write_data(0x04)
        self.write_cmd(0xC1)
        self.write_data(0xC0)
        self.write_cmd(0xC2)
        self.write_data(0x0D)
        self.write_data(0x00)
        self.write_cmd(0xC3)
        self.write_data(0x8D)
        self.write_data(0x6A)
        self.write_cmd(0xC4)
        self.write_data(0x8D)
        self.write_data(0xEE)
        self.write_cmd(0xC5)
        self.write_data(0x0E)
        self.write_cmd(0xE0)
        self.write_data(0x10)
        self.write_data(0x0E)
        self.write_data(0x02)
        self.write_data(0x03)
        self.write_data(0x0E)
        self.write_data(0x07)
        self.write_data(0x02)
        self.write_data(0x07)
        self.write_data(0x0A)
        self.write_data(0x12)
        self.write_data(0x27)
        self.write_data(0x37)
        self.write_data(0x00)
        self.write_data(0x0D)
        self.write_data(0x0E)
        self.write_data(0x10)
        self.write_cmd(0xE1)
        self.write_data(0x10)
        self.write_data(0x0E)
        self.write_data(0x03)
        self.write_data(0x03)
        self.write_data(0x0F)
        self.write_data(0x06)
        self.write_data(0x02)
        self.write_data(0x08)
        self.write_data(0x0A)
        self.write_data(0x13)
        self.write_data(0x26)
        self.write_data(0x36)
        self.write_data(0x00)
        self.write_data(0x0D)
        self.write_data(0x0E)
        self.write_data(0x10)
        self.write_cmd(0x3A)
        self.write_data(0x05)
        self.write_cmd(0x36)
        self.write_data(0xA8)
        self.write_cmd(0x29)

    def set_window(self, x_start, y_start, x_end, y_end):
        x_start = x_start + 1
        x_end = x_end + 1
        y_start = y_start + 26
        y_end = y_end + 26

        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(x_start)
        self.write_data(0x00)
        self.write_data(x_end)
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(y_start)
        self.write_data(0x00)
        self.write_data(y_end)
        self.write_cmd(0x2C)

    def show(self):
        self.set_window(0, 0, self.width - 1, self.height - 1)
        self._dc(1)
        self._cs(0)
        self._spi.write(self._buffer)
        self._cs(1)

    @staticmethod
    def rgb_color(r, g, b):
        return (((g & 0b00011100) << 3) + ((r & 0b11111000) >> 3) << 8) + (b & 0b11111000) + ((g & 0b11100000) >> 5)
