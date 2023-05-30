from micropython import const
from lib.neopixelmatrix import NeoPixelMatrix
from urandom import randrange, randint
from utime import sleep_ms


GPIO_PIN = const(32)
NEOPIXEL_ROWS = const(10)
NEOPIXEL_COLS = const(16)


class Ball:

    def __init__(self, neopixel, pos_x: int, pos_y: int, rgb: tuple):
        """
        a NeoPixel ball object
        :param neopixel: neopixel object
        :param pos_x: x coordinates for start position
        :param pos_y: y coordinates for start position
        :param rgb: color as RGB tuple
        """
        self.nps = neopixel
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.color = tuple(rgb)

        self.direction_x = [-1, 1][randrange(2)]
        self.direction_y = [-1, 1][randrange(2)]

    def draw_ball(self, pos_x: int, pos_y: int, reset: bool) -> None:
        """
        draw ball on matrix
        :param pos_x: x coordinates
        :param pos_y: y coordinates
        :param reset: set pixel back to display color or not
        :return: None
        """
        if reset:
            self.nps.set_coordinate(int(pos_x), int(pos_y), (0, 0, 0))
        else:
            self.nps.set_coordinate(int(pos_x), int(pos_y), self.color)


if __name__ == '__main__':
    nps = NeoPixelMatrix(GPIO_PIN, NEOPIXEL_ROWS, NEOPIXEL_COLS)

    balls = []
    number_balls = randint(2, 6)

    for i in range(number_balls):
        balls.append(Ball(nps, randint(1, 9), randint(1, 5), (randint(0, 90), randint(0, 90), randint(0, 90))))

    nps.clear_matrix()
    nps.draw_rectangle(0, 0, NEOPIXEL_COLS, NEOPIXEL_ROWS, (25, 0, 0))

    while True:
        for i in range(number_balls):
            if balls[i].pos_x < 2:
                balls[i].direction_x = 1

            if balls[i].pos_x > NEOPIXEL_COLS - 3:
                balls[i].direction_x = -1

            if balls[i].pos_y < 2:
                balls[i].direction_y = 1

            if balls[i].pos_y > NEOPIXEL_ROWS - 3:
                balls[i].direction_y = -1

            balls[i].draw_ball(balls[i].pos_x, balls[i].pos_y, True)

            balls[i].pos_x += balls[i].direction_x
            balls[i].pos_y += balls[i].direction_y

            balls[i].draw_ball(balls[i].pos_x, balls[i].pos_y, False)

        nps.write_matrix()
        sleep_ms(25)
