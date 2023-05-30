from micropython import const
from machine import Pin, ADC
from lib.neopixelmatrix import NeoPixelMatrix
from urandom import randint, randrange
from utime import sleep_ms


GPIO_ADC_PIN = const(32)
GPIO_MATRIX_PIN = const(23)
MATRIX_ROWS = const(10)
MATRIX_COLS = const(16)


class Paddle:
    def __init__(self, neopixel, color: tuple):
        """
        paddle constructor
        :param neopixel: NeoPixel object
        :param color: RGB color tuple
        """
        self.nps = neopixel
        self.color = tuple(color)

        self.height = 3
        self.pos_x = 0
        self.pos_y = None

    def draw_paddle(self) -> None:
        """
        draw paddle on NeoPixel matrix
        :return: None
        """
        self.nps.set_coordinate(self.pos_x, self.pos_y, self.color)
        self.nps.vline(self.pos_x, self.pos_y - 1, 3, self.color)


class Ball:
    def __init__(self, neopixel, color: tuple):
        """
        ball constructor
        :param neopixel: NeoPixel object
        :param color: RGB color tuple
        """
        self.nps = neopixel
        self.color = tuple(color)

        self.pos_x = randint(3, MATRIX_COLS - 2)
        self.pos_y = randint(3, MATRIX_ROWS - 2)

        self.direction_x = [-1, 1][randrange(0, 2)]
        self.direction_y = [-1, 1][randrange(0, 2)]

    def draw_ball(self) -> None:
        """
        draw ball on NeoPixel matrix
        :return: None
        """
        self.nps.set_coordinate(self.pos_x, self.pos_y, self.color)


class Score:
    def __init__(self, neopixel):
        """
        score constructor
        :param neopixel: RGB color tuple
        """
        self.nps = neopixel
        self.score = 0

    def draw_score(self):
        """
        draw score on NeoPixel matrix
        :return: None
        """
        if self.score == 1:
            self.nps.set_coordinate(MATRIX_COLS - 1, 0, (20, 0, 0))
        if self.score == 2:
            self.nps.set_coordinate(MATRIX_COLS - 1, 0, (20, 0, 0))
            self.nps.set_coordinate(MATRIX_COLS - 2, 0, (20, 0, 0))
        if self.score == 3:
            self.nps.set_coordinate(MATRIX_COLS - 1, 0, (20, 0, 0))
            self.nps.set_coordinate(MATRIX_COLS - 2, 0, (20, 0, 0))
            self.nps.set_coordinate(MATRIX_COLS - 3, 0, (20, 0, 0))


if __name__ == '__main__':
    adc = ADC(Pin(GPIO_ADC_PIN, Pin.IN))
    adc.atten(ADC.ATTN_11DB)

    nps = NeoPixelMatrix(pin=GPIO_MATRIX_PIN, rows=MATRIX_ROWS, cols=MATRIX_COLS)

    paddle = Paddle(nps, color=(0, 10, 0))
    ball = Ball(nps, color=(0, 0, 20))
    score = Score(nps)

    nps.clear_matrix()
    nps.set_digit(3, 7, 2, (0, 20, 0))
    nps.write_matrix()
    sleep_ms(500)
    nps.clear_matrix()
    nps.set_digit(2, 7, 2, (0, 20, 0))
    nps.write_matrix()
    sleep_ms(500)
    nps.clear_matrix()
    nps.set_digit(1, 7, 2, (0, 20, 0))
    nps.write_matrix()
    sleep_ms(500)

    while True:
        adc_val = adc.read_u16()
        paddle.pos_y = int(adc_val * (MATRIX_ROWS / 65535))

        ball.pos_x += ball.direction_x
        ball.pos_y += ball.direction_y

        if paddle.pos_y >= 8:
            paddle.pos_y = 8

        if paddle.pos_y <= 1:
            paddle.pos_y = 1

        if ball.pos_x == 0:
            if ball.pos_x or ball.pos_y in {(paddle.pos_y - 1), paddle.pos_y, (paddle.pos_y + 1)}:
                ball.direction_x = 1

        if ball.pos_x == -1:
            score.score += 1
            ball.pos_x = randint(3, MATRIX_COLS - 2)
            ball.pos_y = randint(3, MATRIX_ROWS - 2)

        if score.score > 3:
            break

        if ball.pos_x == (MATRIX_COLS - 1):
            ball.direction_x = -1

        if ball.pos_y < 1:
            ball.direction_y = 1

        if ball.pos_y > (MATRIX_ROWS - 2):
            ball.direction_y = -1

        nps.clear_matrix()

        score.draw_score()
        paddle.draw_paddle()
        ball.draw_ball()

        nps.write_matrix()

        sleep_ms(150)

    for i in range(0, 2):
        nps.fill_matrix((20, 0, 0))
        nps.write_matrix()
        sleep_ms(500)
        nps.fill_matrix((0, 0, 0))
        nps.write_matrix()
        sleep_ms(500)
