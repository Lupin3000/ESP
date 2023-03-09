from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep_ms


class NeoPixelRing:

    def __init__(self, pin: int, count: int):
        """
        class initializer
        :param pin: integer for data GPIO Pin
        :param count: integer for total Neopixel count
        """
        self.neopixel_count = int(count)
        self.neopixel = NeoPixel(Pin(int(pin)), self.neopixel_count)

    def fill(self, rgb: tuple) -> None:
        """
        set all Neopixel to same color
        :param rgb: tuple of rgb color (eq. 10, 20, 30)
        :return: None
        """
        for value in rgb:
            if not 0 <= int(value) <= 255:
                raise Exception('Tuple parameter not in range 0 to 255')

        self.neopixel.fill(tuple(rgb))
        self.neopixel.write()

    def clear(self) -> None:
        """
        set all Neopixel off
        :return: None
        """
        self.fill((0, 0, 0))

    def random(self, single: bool = True) -> None:
        """
        set all or each Neopixel to random color
        :param single: bool for single random color, False mean all pixel
        :return: None
        """
        if single:
            for item in range(self.neopixel_count):
                self.neopixel[item] = (randint(0, 255), randint(0, 255), randint(0, 255))
                self.neopixel.write()
        else:
            rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
            for item in range(self.neopixel_count):
                self.neopixel[item] = rgb
                self.neopixel.write()

    def circle(self, front_rgb: tuple, back_rgb: tuple, milliseconds: int) -> None:
        """
        circle Neopixel with specific front- and background color
        :param front_rgb: tuple of rgb color (eq. 255, 0, 0)
        :param back_rgb: tuple of rgb color (eq. 0, 0, 255)
        :param milliseconds: integer in milliseconds
        :return: None
        """
        for value in front_rgb:
            if not 0 <= int(value) <= 255:
                raise Exception('Tuple parameter not in range 0 to 255')

        for value in back_rgb:
            if not 0 <= int(value) <= 255:
                raise Exception('Tuple parameter not in range 0 to 255')

        if not int(milliseconds):
            error = TypeError("Parameter must be integer")
            raise Exception(error)

        self.fill(front_rgb)

        for index in range(self.neopixel_count):
            self.neopixel[index] = tuple(back_rgb)
            self.neopixel[index - 1] = tuple(front_rgb)
            self.neopixel.write()
            sleep_ms(int(milliseconds))

    def fade(self, milliseconds: int, direction: bool = True) -> None:
        """
        fade all Neopixel in or out
        :param milliseconds: integer in milliseconds
        :param direction: bool for fade in/out, False means fade out
        :return: None
        """
        if not int(milliseconds):
            error = TypeError("Parameter must be integer")
            raise Exception(error)

        if direction:
            for value in range(0, 255, 1):
                self.fill((value, value, value))
                sleep_ms(int(milliseconds))
        else:
            for value in range(255, 0, -1):
                self.fill((value, value, value))
                sleep_ms(int(milliseconds))

            self.fill((0, 0, 0))
