from micropython import const
from neopixelmatrix import NeoPixelMatrix
from utime import sleep


NEOPIXEL_PIN = const(23)
NEOPIXEL_ROWS = const(10)
NEOPIXEL_COLS = const(16)


if __name__ == '__main__':
    nps = NeoPixelMatrix(NEOPIXEL_PIN, NEOPIXEL_ROWS, NEOPIXEL_COLS)

    while True:
        nps.clear_matrix()
        nps.set_digit(3, 5, 1, (100, 100, 0))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.set_digit(2, 5, 1, (100, 100, 0))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.set_digit(1, 5, 1, (100, 100, 0))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.vline(1, 1, 2, (0, 30, 10))
        nps.vline(3, 1, 4, (0, 20, 0))
        nps.vline(5, 1, 6, (0, 10, 10))
        nps.vline(7, 1, 8, (10, 20, 0))
        nps.vline(8, 1, 8, (10, 20, 0))
        nps.vline(10, 1, 6, (0, 10, 10))
        nps.vline(12, 1, 4, (0, 20, 0))
        nps.vline(14, 1, 2, (0, 30, 10))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.hline(0, 9, 16, (20, 0, 0))
        nps.hline(1, 7, 14, (0, 0, 20))
        nps.hline(2, 5, 12, (20, 20, 0))
        nps.hline(3, 3, 10, (20, 0, 20))
        nps.hline(4, 1, 8, (0, 20, 20))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.fill_matrix((5, 5, 5))
        nps.write_matrix()
        sleep(1)

        nps.clear_matrix()
        nps.draw_rectangle(1, 1, 8, 4, (1, 2, 3))
        nps.draw_rectangle(7, 6, 3, 3, (3, 2, 1))
        nps.draw_rectangle(10, 2, 4, 5, (2, 3, 0))
        nps.write_matrix()
