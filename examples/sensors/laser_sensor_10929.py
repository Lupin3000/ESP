from micropython import const
from machine import Pin, SoftI2C
from lib.ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer, MONO_HLSB


LASER_GPIO_PIN = const(23)
SDA_GPIO_PIN = const(21)
SCL_GPIO_PIN = const(22)
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)

IMAGE_STOP = 'stop.pbm'
IMAGE_GO = 'go.pbm'


class Display:
    def __init__(self, sda_pin: int, scl_pin: int, width: int, height: int):
        """
        display constructor
        :param sda_pin: SDA GPIO Pin for display as integer
        :param scl_pin: SCL GPIO Pin for display as integer
        :param width: display width as integer
        :param height: display height as integer
        """
        i2c = SoftI2C(sda=Pin(int(sda_pin)), scl=Pin(int(scl_pin)))

        self.__width = int(width)
        self.__height = int(height)
        self.display = SSD1306_I2C(self.__width, self.__height, i2c)


class Laser:
    def __init__(self, display, pin: int):
        """
        laser constructor
        :param display: display object
        :param pin: DOUT GPIO pin as integer
        """
        self.__display = display

        self.__img_go = Laser.load_image(IMAGE_GO, 50, 50)
        self.__img_stop = Laser.load_image(IMAGE_STOP, 50, 50)

        self._detection = Pin(int(pin), Pin.IN)
        self._detection.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._handler)

    def _handler(self, pin) -> None:
        """
        irg multiplexer handler for display status
        :param pin: pin object
        :return: None
        """
        self.__display.fill(0)

        if pin.value() == 1:
            self.__display.blit(self.__img_go, 39, 5)
        else:
            self.__display.blit(self.__img_stop, 39, 5)

        self.__display.show()

    @staticmethod
    def load_image(filename: str, w: int, h: int):
        """
        load pbm image into FrameBuffer object
        :param filename: image path/filename as string
        :param w: width as integer of image to load
        :param h: height as integer of image to load
        :return: image as FrameBuffer object
        """
        with open(filename, 'rb') as f:
            f.readline()
            f.readline()
            f.readline()
            data = bytearray(f.read())

        return FrameBuffer(data, w, h, MONO_HLSB)


if __name__ == '__main__':
    oled = Display(sda_pin=SDA_GPIO_PIN, scl_pin=SCL_GPIO_PIN, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)
    laser = Laser(display=oled.display, pin=LASER_GPIO_PIN)
