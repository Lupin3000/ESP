from micropython import const
from machine import Pin, SoftI2C
from lib.ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer, MONO_HLSB
from urandom import randint
from utime import sleep_ms


PIN_SDA = const(21)
PIN_SCL = const(22)
BUTTON_PIN = const(23)
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)


class SlotItem:
    def __init__(self, image: str):
        """
        slot item constructor
        :param image: image of slot item
        """
        self.image = SlotItem._load_image(str(image), 40, 40)

    @staticmethod
    def _load_image(filename: str, w: int, h: int):
        """
        load image into FrameBuffer
        :param filename: image path/name
        :param w: width of image in pixel
        :param h: height of image in pixel
        :return: FrameBuffer object
        """
        with open(filename, 'rb') as f:
            f.readline()
            f.readline()
            f.readline()
            data = bytearray(f.read())

        return FrameBuffer(data, w, h, MONO_HLSB)


def spin_slots() -> None:
    """
    start slot spinning
    :return: None
    """
    global oled
    global slot_items

    num_a = None
    num_b = None
    num_c = None

    oled.vline(42, 10, 40, 1)
    oled.vline(84, 10, 40, 1)

    for i in range(0, 15):
        num_a = randint(0, len(slot_items) - 1)
        num_b = randint(0, len(slot_items) - 1)
        num_c = randint(0, len(slot_items) - 1)

        oled.blit(slot_items[num_a].image, 1, 10)
        oled.blit(slot_items[num_b].image, 43, 10)
        oled.blit(slot_items[num_c].image, 85, 10)
        oled.show()

        sleep_ms(75)

    if num_a == num_b == num_c:

        for i in range(0, 5):
            oled.invert(1)
            sleep_ms(50)
            oled.invert(0)
            sleep_ms(50)


def interrupt_handler(pin) -> None:
    """
    button irq handler
    :param pin: GPIO pin
    :return: None
    """
    spin_slots()


if __name__ == '__main__':
    i2c = SoftI2C(sda=Pin(PIN_SDA), scl=Pin(PIN_SCL))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    btn = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
    btn.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_handler)

    slot_items = [
        SlotItem('cherry.pbm'),
        SlotItem('clover.pbm'),
        SlotItem('seven.pbm'),
        SlotItem('diamond.pbm')
    ]

    oled.fill(0)
    oled.rect(0, 9, 127, 42, 1)
    oled.text('Press Button', 5, 20, 1)
    oled.text('Good luck...', 5, 35, 1)
    oled.show()
