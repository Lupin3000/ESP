from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep_ms


class NeoPixelRing:

    _INT_VALUE_ERROR = 'Parameter must be an positive integer'
    _RGB_VALUE_ERROR = 'All tuple parameter values must in range 0 to 255'
    _STR_VALUE_ERROR = 'String parameter is not defined'

    def __init__(self, pin: int, count: int):
        """
        class initializer
        :param pin: integer for data GPIO Pin
        :param count: integer for total Neopixel count
        """
        if not int(pin):
            error = TypeError(self._INT_VALUE_ERROR)
            raise Exception(error)

        if not int(count):
            error = TypeError(self._INT_VALUE_ERROR)
            raise Exception(error)

        self.neopixel = NeoPixel(Pin(int(pin)), int(count))

    def fill(self, rgb: tuple) -> None:
        """
        set all Neopixel to same color
        :param rgb: tuple of rgb color (eq. 10, 20, 30)
        :return: None
        """
        for value in rgb:
            if not 0 <= int(value) <= 255:
                error = ValueError(self._RGB_VALUE_ERROR)
                raise Exception(error)

        self.neopixel.fill(tuple(rgb))
        self.neopixel.write()

    def clear(self) -> None:
        """
        set all Neopixel off
        :return: None
        """
        self.fill((0, 0, 0))

    def pixel(self, number: int, rgb: tuple) -> None:
        """
        set specific pixel to rgb color
        :param number: integer of pixel
        :param rgb: tuple of rgb color (eq. 100, 200, 0)
        :return: None
        """
        for value in rgb:
            if not 0 <= int(value) <= 255:
                error = ValueError(self._RGB_VALUE_ERROR)
                raise Exception(error)

        if not 0 <= int(number) <= (len(self.neopixel) - 1):
            error = ValueError(f'{self._INT_VALUE_ERROR} between 0 and {len(self.neopixel) - 1}')
            raise Exception(error)

        self.neopixel[int(number)] = tuple(rgb)
        self.neopixel.write()

    def random(self, single_rgb: bool = True) -> None:
        """
        set all or each Neopixel to random color
        :param single_rgb: bool for single random color, False mean all pixel
        :return: None
        """
        if bool(single_rgb):
            for item in range(len(self.neopixel)):
                self.neopixel[item] = (randint(0, 255), randint(0, 255), randint(0, 255))
                self.neopixel.write()
        else:
            rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
            for item in range(len(self.neopixel)):
                self.neopixel[item] = rgb
                self.neopixel.write()

    def circle(self, front_rgb: tuple, back_rgb: tuple, ms: int = 100, way: str = 'forward', on: bool = False) -> None:
        """
        circle Neopixel with specific front- and background color
        :param front_rgb: tuple of rgb front color to circle (eq. 255, 0, 0)
        :param back_rgb: tuple of rgb background color (eq. 0, 0, 255)
        :param ms: integer in milliseconds, Default = 100ms
        :param way: string for direction, Default = forward
        :param on: bool value if pixel turn back to back_rgb color, Default = False
        :return: None
        """
        for value in front_rgb:
            if not 0 <= int(value) <= 255:
                error = ValueError(self._RGB_VALUE_ERROR)
                raise Exception(error)

        for value in back_rgb:
            if not 0 <= int(value) <= 255:
                error = ValueError(self._RGB_VALUE_ERROR)
                raise Exception(error)

        if not int(ms):
            error = TypeError(self._INT_VALUE_ERROR)
            raise Exception(error)

        valid = {'forward', 'backward'}
        if way not in valid:
            error = ValueError(self._STR_VALUE_ERROR)
            raise Exception(error)

        self.fill(back_rgb)

        if str(way) == 'forward':
            for index in range(0, len(self.neopixel), 1):
                self.neopixel[index] = tuple(front_rgb)
                if not bool(on):
                    self.neopixel[index - 1] = tuple(back_rgb)
                self.neopixel.write()
                sleep_ms(int(ms))
        else:
            for index in range(len(self.neopixel) - 1, -1, -1):
                self.neopixel[index] = tuple(front_rgb)
                if index < 11 and not bool(on):
                    self.neopixel[index + 1] = tuple(back_rgb)
                self.neopixel.write()
                sleep_ms(int(ms))

    def fade(self, ms: int = 100, direction: bool = True) -> None:
        """
        fade all Neopixel in or out
        :param ms: integer in milliseconds, Default = 100ms
        :param direction: bool for fade in/out, False means fade out, Default = True
        :return: None
        """
        if not int(ms):
            error = TypeError(self._INT_VALUE_ERROR)
            raise Exception(error)

        if bool(direction):
            for value in range(0, 255, 1):
                self.fill((value, value, value))
                sleep_ms(int(ms))
        else:
            for value in range(255, 0, -1):
                self.fill((value, value, value))
                sleep_ms(int(ms))

            self.fill((0, 0, 0))
