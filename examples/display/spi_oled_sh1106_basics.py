from micropython import const
from machine import Pin, SPI
from lib.sh1106 import SH1106_SPI
from urandom import getrandbits
from framebuf import FrameBuffer, MONO_HLSB
from utime import sleep_ms


SDA_PIN = const(23)
SCL_PIN = const(18)
DC_PIN = const(2)
RES_PIN = const(4)
CS_PIN = const(5)

DP_WIDTH = const(128)
DP_HEIGHT = const(64)


def matrix() -> None:
    """
    create matrix effect
    :return: None
    """
    global display

    for i in range(DP_WIDTH):
        for j in range(DP_HEIGHT):
            display.pixel(i, j, getrandbits(1))

    display.show()


def scroll_text(text: str) -> None:
    """
    scroll string from left to right
    :param text: message to display
    :return: None
    """
    global display

    for i in range(len(text)*6):
        display.fill(0)
        display.text(text, -i, 30)
        display.show()
        sleep_ms(5)


def load_image(filename: str, w: int, h: int):
    """
    load pbm images
    :param filename: path/filename of pbm
    :param w: width of image
    :param h: height of image
    :return: FrameBuffer object
    """
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        f.readline()
        data = bytearray(f.read())

    return FrameBuffer(data, w, h, MONO_HLSB)


if __name__ == '__main__':
    spi = SPI(1, baudrate=1000000, sck=Pin(SCL_PIN), mosi=Pin(SDA_PIN))
    display = SH1106_SPI(width=DP_WIDTH, height=DP_HEIGHT,
                         spi=spi, dc=Pin(DC_PIN), res=Pin(RES_PIN), cs=Pin(CS_PIN), rotate=0, delay=0)

    img_armchair = load_image('armchair.pbm', 128, 64)
    img_morpheus = load_image('morpheus.pbm', 128, 64)
    img_pill = load_image('pill.pbm', 128, 64)

    display.fill(0)

    while True:
        display.invert(0)
        scroll_text("    Wake up, Neo...      ")

        for i in range(0, 5):
            matrix()
            sleep_ms(5)

        display.invert(1)
        display.blit(img_armchair, 0, 0)
        display.show()
        sleep_ms(500)

        for i in range(0, 2):
            matrix()
            sleep_ms(5)

        display.blit(img_morpheus, 0, 0)
        display.show()
        sleep_ms(1000)

        scroll_text("    Decide, blue or red...          ")

        display.blit(img_pill, 0, 0)
        display.show()
        sleep_ms(1500)
