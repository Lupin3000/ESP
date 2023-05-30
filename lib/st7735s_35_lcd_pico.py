from micropython import const
from machine import Pin, SPI, PWM
from framebuf import FrameBuffer, RGB565
from utime import sleep_ms, sleep_us


class LCD(FrameBuffer):
    """
    MicroPython Pico Eval Board - 3.5inch 480x320 LCD driver
    https://www.waveshare.com/esp32-s2.htm

    The driver is based on MicroPython FrameBuffer as well as a smaller further development
    (cleanup, improvements, etc.) of the original example provided by WaveShare

    Drawing primitive shapes
    To draw pixels, lines, rectangles, ellipses, polygons, text, etc. the standard FrameBuffer methods are available
    """
    LCD_DC = const(8)
    LCD_CS = const(9)
    LCD_SCK = const(10)
    LCD_MOSI = const(11)
    LCD_MISO = const(12)
    LCD_BL = const(13)
    LCD_RST = const(15)
    TP_CS = const(16)
    TP_IRQ = const(17)

    def __init__(self, width: int = 480, height: int = 160):
        """
        LCD constructor
        :param width: frame width in pixel
        :param height: frame height in pixel
        """
        self.width = int(width)
        self.height = int(height)

        self._cs = Pin(self.LCD_CS, Pin.OUT)
        self._rst = Pin(self.LCD_RST, Pin.OUT)
        self._dc = Pin(self.LCD_DC, Pin.OUT)

        self._tp_cs = Pin(self.TP_CS, Pin.OUT)
        self._irq = Pin(self.TP_IRQ, Pin.IN)

        self._buffer = bytearray(self.height * self.width * 2)
        self._pwm = PWM(Pin(self.LCD_BL))

        self._spi = SPI(1, 60_000_000, sck=Pin(self.LCD_SCK), mosi=Pin(self.LCD_MOSI), miso=Pin(self.LCD_MISO))

        self._cs(1)
        self._dc(1)
        self._rst(1)
        self._tp_cs(1)

        super().__init__(self._buffer, self.width, self.height, RGB565)
        self._init_display()

    def _write_cmd(self, cmd) -> None:
        """
        write commands to display
        :param cmd: hex number value
        :return: None
        """
        self._cs(1)
        self._dc(0)
        self._cs(0)
        self._spi.write(bytearray([cmd]))
        self._cs(1)

    def _write_data(self, buf) -> None:
        """
        write data to display
        :param buf: hex number value
        :return: None
        """
        self._cs(1)
        self._dc(1)
        self._cs(0)
        self._spi.write(bytearray([buf]))
        self._cs(1)

    def _init_display(self) -> None:
        """
        initialize display
        :return: None
        """
        self._rst(1)
        sleep_ms(5)

        self._rst(0)
        sleep_ms(10)

        self._rst(1)
        sleep_ms(5)

        self._write_cmd(0x21)
        self._write_cmd(0xC2)
        self._write_data(0x33)
        self._write_cmd(0XC5)
        self._write_data(0x00)
        self._write_data(0x1e)
        self._write_data(0x80)
        self._write_cmd(0xB1)
        self._write_data(0xB0)
        self._write_cmd(0x36)
        self._write_data(0x28)
        self._write_cmd(0XE0)
        self._write_data(0x00)
        self._write_data(0x13)
        self._write_data(0x18)
        self._write_data(0x04)
        self._write_data(0x0F)
        self._write_data(0x06)
        self._write_data(0x3a)
        self._write_data(0x56)
        self._write_data(0x4d)
        self._write_data(0x03)
        self._write_data(0x0a)
        self._write_data(0x06)
        self._write_data(0x30)
        self._write_data(0x3e)
        self._write_data(0x0f)
        self._write_cmd(0XE1)
        self._write_data(0x00)
        self._write_data(0x13)
        self._write_data(0x18)
        self._write_data(0x01)
        self._write_data(0x11)
        self._write_data(0x06)
        self._write_data(0x38)
        self._write_data(0x34)
        self._write_data(0x4d)
        self._write_data(0x06)
        self._write_data(0x0d)
        self._write_data(0x0b)
        self._write_data(0x31)
        self._write_data(0x37)
        self._write_data(0x0f)
        self._write_cmd(0X3A)
        self._write_data(0x55)
        self._write_cmd(0x11)
        sleep_ms(120)

        self._write_cmd(0x29)
        self._write_cmd(0xB6)
        self._write_data(0x00)
        self._write_data(0x62)
        self._write_cmd(0x36)
        self._write_data(0x28)

    def backlight(self, duty: int) -> None:
        """
        set backlight
        :param duty: set the backlight by value (0 - 100)
        :return: None
        """
        val = int(duty)
        self._pwm.freq(1000)

        if val >= 100:
            self._pwm.duty_u16(65535)
        else:
            self._pwm.duty_u16(655 * val)

    def show_up(self) -> None:
        """
        show content on upper frame
        :return: None
        """
        self._write_cmd(0x2A)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data(0x01)
        self._write_data(0xdf)
        self._write_cmd(0x2B)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data(0x9f)
        self._write_cmd(0x2C)

        self._cs(1)
        self._dc(1)
        self._cs(0)
        self._spi.write(self._buffer)
        self._cs(1)

    def show_down(self) -> None:
        """
        show content on lower frame
        :return: None
        """
        self._write_cmd(0x2A)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data(0x01)
        self._write_data(0xdf)
        self._write_cmd(0x2B)
        self._write_data(0x00)
        self._write_data(0xA0)
        self._write_data(0x01)
        self._write_data(0x3f)
        self._write_cmd(0x2C)

        self._cs(1)
        self._dc(1)
        self._cs(0)
        self._spi.write(self._buffer)
        self._cs(1)

    def touch_get(self) -> list:
        """
        get touch position
        :return: list
        """
        if self._irq() == 0:
            self._spi = SPI(1, 5_000_000, sck=Pin(self.LCD_SCK), mosi=Pin(self.LCD_MOSI), miso=Pin(self.LCD_MISO))
            self._tp_cs(0)

            point_x = 0
            point_y = 0

            for i in range(0, 3):
                self._spi.write(bytearray([0XD0]))
                read_data = self._spi.read(2)
                sleep_us(10)
                point_x = point_x + (((read_data[0] << 8) + read_data[1]) >> 3)
                self._spi.write(bytearray([0X90]))
                read_data = self._spi.read(2)
                point_y = point_y + (((read_data[0] << 8) + read_data[1]) >> 3)

            point_x = point_x / 3
            point_y = point_y / 3

            self._tp_cs(1)
            self._spi = SPI(1, 60_000_000, sck=Pin(LCD_SCK), mosi=Pin(LCD_MOSI), miso=Pin(LCD_MISO))
            return [point_x, point_y]
