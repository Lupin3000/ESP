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
        NeoPixelRing.__verify_int(pin, 1)
        NeoPixelRing.__verify_int(count, 1)

        self.neopixel = NeoPixel(Pin(int(pin)), int(count))

    @staticmethod
    def __verify_int(value: int, minimum: int, maximum: int = None) -> None:
        """
        verify integer parameter
        :param value: mandatory integer value
        :param minimum: mandatory minimum integer value
        :param maximum: optional maximum value
        :return: None
        """
        if not isinstance(value, int):
            error = TypeError('Parameter must be integer')
            raise Exception(error)

        if int(value) < int(minimum):
            error = ValueError(f'Integer must be positive starting from {int(minimum)}')
            raise Exception(error)

        if maximum:
            if int(value) > int(maximum):
                error = ValueError(f'Maximum for integer is {int(maximum)}')
                raise Exception(error)

    @staticmethod
    def __verify_rgb(value: tuple) -> None:
        """
        verify rgb color parameter
        :param value: mandatory tuple of rgb color (eq. 0, 0, 0)
        :return: None
        """
        if not len(tuple(value)) == 3:
            error = ValueError('Parameter must be an tuple with length 3')
            raise Exception(error)

        for item in tuple(value):
            if not 0 <= int(item) <= 255:
                error = ValueError('Every tuple parameter value must in range 0 to 255')
                raise Exception(error)

    @staticmethod
    def __verify_bool(value: bool) -> None:
        """
        verify bool parameter
        :param value: mandatory bool value
        :return: None
        """
        if not isinstance(value, bool):
            error = TypeError('Parameter must be a bool')
            raise Exception(error)

    @staticmethod
    def wheel(pos: int) -> tuple:
        """
        generates the rainbow color spectrum
        :param pos: integer value
        :return: tuple
        """
        if pos < 0 or pos > 255:
            return 0, 0, 0
        if pos < 85:
            return 255 - pos * 3, pos * 3, 0
        if pos < 170:
            pos -= 85
            return 0, 255 - pos * 3, pos * 3
        pos -= 170
        return pos * 3, 0, 255 - pos * 3

    def pixel(self, index: int, rgb: tuple) -> None:
        """
        set specific Neopixel to rgb color
        :param index: integer of pixel
        :param rgb: tuple of rgb color (eq. 100, 200, 0)
        :return: None
        """
        NeoPixelRing.__verify_int(index, 0, (len(self.neopixel) - 1))
        NeoPixelRing.__verify_rgb(rgb)

        self.neopixel[int(index)] = tuple(rgb)
        self.neopixel.write()

    def fill(self, rgb: tuple) -> None:
        """
        set all Neopixel to same color
        :param rgb: tuple of rgb color (eq. 10, 20, 30)
        :return: None
        """
        NeoPixelRing.__verify_rgb(rgb)

        self.neopixel.fill(tuple(rgb))
        self.neopixel.write()

    def clear(self) -> None:
        """
        set all Neopixel off
        :return: None
        """
        self.fill((0, 0, 0))

    def rainbow(self) -> None:
        """
        create animated Neopixel rainbow effect
        :return: None
        """
        for value in range(255):
            for item in range(len(self.neopixel)):
                rc_index = (item * 256 // len(self.neopixel)) + value
                self.neopixel[item] = NeoPixelRing.wheel(rc_index & 255)
            self.neopixel.write()

    def random(self, single: bool = True) -> None:
        """
        set all or each Neopixel to random color
        :param single: bool for single random color, False mean all pixel
        :return: None
        """
        NeoPixelRing.__verify_bool(single)

        if bool(single):
            for item in range(len(self.neopixel)):
                self.neopixel[item] = (randint(0, 255), randint(0, 255), randint(0, 255))
                self.neopixel.write()
        else:
            rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
            for item in range(len(self.neopixel)):
                self.neopixel[item] = rgb
                self.neopixel.write()

    def circle(self, front_rgb: tuple, back_rgb: tuple, ms: int = 100, way: bool = True, on: bool = False) -> None:
        """
        circle Neopixel with specific front- and background color
        :param front_rgb: tuple of rgb front color to circle (eq. 255, 0, 0)
        :param back_rgb: tuple of rgb background color (eq. 0, 0, 255)
        :param ms: integer in milliseconds, Default = 100ms
        :param way: bool for snake_direction (forward or backward), Default = True
        :param on: bool value if pixel turn back to back_rgb color, Default = False
        :return: None
        """
        NeoPixelRing.__verify_rgb(front_rgb)
        NeoPixelRing.__verify_rgb(back_rgb)
        NeoPixelRing.__verify_int(ms, 1)
        NeoPixelRing.__verify_bool(way)
        NeoPixelRing.__verify_bool(on)

        self.fill(back_rgb)

        if bool(way):
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

    def fade(self, ms: int = 10, direction: bool = True) -> None:
        """
        fade all Neopixel in or out
        :param ms: integer in milliseconds, Default = 10ms
        :param direction: bool for fade in/out, False means fade out, Default = True
        :return: None
        """
        NeoPixelRing.__verify_int(ms, 1)
        NeoPixelRing.__verify_bool(direction)

        if bool(direction):
            for value in range(0, 255, 1):
                self.fill((value, value, value))
                sleep_ms(int(ms))
        else:
            for value in range(255, 0, -1):
                self.fill((value, value, value))
                sleep_ms(int(ms))

            self.fill((0, 0, 0))
