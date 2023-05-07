from machine import Pin
from neopixel import NeoPixel


class NeoPixelMatrix:

    NUMS = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0,  # 0
            0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
            1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
            1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
            1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
            1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
            1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
            1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 7
            1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
            1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]  # 9

    def __init__(self, pin: int, rows: int, cols: int):
        """
        construct a NeoPixel matrix object
        :param pin: gpio pin value
        :param rows: number of neopixel in rows
        :param cols: number of neopixel in cols
        """
        self.rows = int(rows)
        self.cols = int(cols)
        self.number = self.rows * self.cols
        self.np = NeoPixel(Pin(pin), self.number)

    def write_matrix(self) -> None:
        """
        writes the current NeoPixel data to matrix
        :return: None
        """
        self.np.write()

    def fill_matrix(self, color: tuple) -> None:
        """
        set all NeoPixel to same color
        :param color: tuple of RGB values
        :return: None
        """
        self.np.fill(tuple(color))

    def clear_matrix(self) -> None:
        """
        set all NeoPixel off by RGB value (0, 0, 0)
        :return: None
        """
        self.fill_matrix((0, 0, 0))
        self.write_matrix()

    def set_index(self, number: int, color: tuple) -> None:
        """
        set a specific NeoPixel to RGB color by index number
        :param number: specific NeoPixel
        :param color: tuple of RGB values
        :return: None
        """
        self.np[int(number)] = tuple(color)

    def set_coordinate(self, x: int, y: int, color: tuple) -> None:
        """
        set a specific NeoPixel to RGB color by x,y coordinate on matrix
        :param x: value for x position
        :param y: value for y position
        :param color: tuple of RGB values
        :return: None
        """
        index = int(y) * int(self.cols) + int(x)
        self.set_index(index, tuple(color))

    def hline(self, x: int, y: int, length: int, color: tuple) -> None:
        """
        set NeoPixel to RGB value as horizontal line by x,y start coordinates and length
        :param x: value for x start position
        :param y: value for y start position
        :param length: value for length
        :param color: tuple of RGB values
        :return: None
        """
        for item in range(int(length)):
            x_cal = int(x) + item
            if x_cal <= (self.cols - 1):
                self.set_coordinate(x_cal, int(y), tuple(color))

    def vline(self, x: int, y: int, length: int, color: tuple) -> None:
        """
        set NeoPixel to RGB value as vertical line by x,y start coordinates and length
        :param x: value for x start position
        :param y: value for y start position
        :param length: value for length
        :param color: tuple of RGB values
        :return: None
        """
        for item in range(int(length)):
            y_cal = int(y) + item
            if y_cal <= (self.rows - 1):
                self.set_coordinate(int(x), y_cal, tuple(color))

    def draw_rectangle(self, x: int, y: int, length: int, height: int, color: tuple) -> None:
        """
        set NeoPixel to RGB value as rectangle by x,y start coordinates, length and height
        :param x: value for x start position
        :param y: value for y start position
        :param length: value for length
        :param height: value for height
        :param color: tuple of RGB values
        :return: None
        """
        self.hline(int(x), int(y), int(length), tuple(color))
        self.hline(int(x), (int(y) + int(height) - 1), int(length), tuple(color))
        self.vline(int(x), int(y), int(height), tuple(color))
        self.vline((int(x) + int(length) - 1), int(y), int(height), tuple(color))

    def set_digit(self, val: int, x: int, y: int, color: tuple) -> None:
        """
        create a digit 0-9 on NeoPixels by value incl. x,y coordinates and color
        :param val: number from 0 till 9
        :param x: value for x coordinate on matrix
        :param y: value for y coordinate on matrix
        :param color: tuple of RGB values
        :return: None
        """
        offset = int(val) * 15

        for item in range(offset, offset + 15):
            if self.NUMS[item] == 1:
                xt = item % 3
                yt = (item - offset) // 3
                self.set_coordinate(xt + int(x), yt + int(y), tuple(color))
