from lib.neopixelmatrix import NeoPixelMatrix
from utime import sleep


class NeoPixelMatrixIcon(NeoPixelMatrix):
    """
    Extension class for NeoPixelMatrix Module
    """

    def set_icon(self, icon: list, x: int, y: int, color: tuple) -> None:
        """
        draw a simple icon on NeoPixel Matrix
        :param icon: list of icon values
        :param x: start position for x coordinates
        :param y: start position for y coordinates
        :param color: RGB color tuple
        :return: None
        """
        start_x = int(x)
        start_y = int(y)

        for j, row in enumerate(list(icon)):
            for i, c in enumerate(row):
                if c == 0:
                    c = (0, 0, 0)
                else:
                    c = tuple(color)

                val_x = i + start_x
                val_y = j + start_y

                self.set_coordinate(val_x, val_y, tuple(c))


if __name__ == '__main__':
    nps = NeoPixelMatrixIcon(pin=23, rows=10, cols=16)

    my_heart = [
        [0, 1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]
    ]

    my_smiley = [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0]
    ]

    my_house = [
        [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
    ]

    while True:
        nps.clear_matrix()
        nps.set_icon(my_heart, 4, 1, (50, 0, 0))
        nps.write_matrix()
        sleep(.5)

        nps.clear_matrix()
        nps.set_icon(my_smiley, 4, 1, (0, 20, 0))
        nps.write_matrix()
        sleep(.5)

        nps.clear_matrix()
        nps.set_icon(my_house, 4, 1, (0, 0, 20))
        nps.write_matrix()
        sleep(.5)
