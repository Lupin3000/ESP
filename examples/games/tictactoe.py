from micropython import const
from machine import Pin, ADC, SoftSPI
from lib.sh1106 import SH1106_SPI
from urandom import randint
from utime import sleep_ms, ticks_ms


SDA_PIN = const(23)
SCL_PIN = const(18)
DC_PIN = const(2)
RES_PIN = const(4)
CS_PIN = const(5)
DP_WIDTH = const(128)
DP_HEIGHT = const(64)

ADC_X_PIN = const(32)
ADC_Y_PIN = const(33)
BUTTON_PIN = const(35)


class Display:
    def __init__(self, sda: int, scl: int, dc: int, cs: int, res: int, width: int, height: int):
        """
        display constructor
        :param sda: GPIO pin for SDA
        :param scl: GPIO pin for SCL
        :param dc: GPIO pin for DC
        :param cs: GPIO pin for CS
        :param res: GPIO pin for RES
        :param width: display width in pixel
        :param height: display height in pixel
        """
        spi = SoftSPI(baudrate=1000000, sck=Pin(int(scl)), mosi=Pin(int(sda)), miso=Pin(int(dc)))

        self.oled = SH1106_SPI(spi=spi,
                               width=int(width),
                               height=int(height),
                               dc=Pin(int(dc)),
                               res=Pin(int(res)),
                               cs=Pin(int(cs)),
                               rotate=0,
                               delay=0)


class GameBoard:
    def __init__(self, screen):
        """
        game board constructor
        :param screen: screen object
        """
        self.display = screen

        self.players = {'cross': 0, 'circle': 0}
        self.current_player = list(self.players)[randint(0, 1)]
        self.move = False
        self.board = None
        self._joystick_pos_x = None
        self._joystick_pos_y = None

        self._cross_icon = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ]

        self._circle_icon = [
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]

        self._matrix = {
            '00': ['6', '6'],
            '01': ['26', '6'],
            '02': ['45', '6'],
            '10': ['6', '26'],
            '11': ['26', '26'],
            '12': ['45', '26'],
            '20': ['6', '45'],
            '21': ['26', '45'],
            '22': ['45', '45']
        }

        self.empty_board()

    def set_cursor(self, pos_x: int, pos_y: int) -> None:
        """
        set x,y coordinates for cursor on display
        :param pos_x: x-coordinate
        :param pos_y: y-coordinate
        :return: None
        """
        position_x = int(pos_x)
        position_y = int(pos_y)

        if 0 <= position_x <= 20:
            position_x = 2

        if 20 <= position_x <= 40:
            position_x = 22

        if 40 <= position_x <= 60:
            position_x = 42

        if 0 <= position_y <= 20:
            position_y = 2

        if 20 <= position_y <= 40:
            position_y = 22

        if 40 <= position_y <= 60:
            position_y = 42

        self._joystick_pos_x = position_x
        self._joystick_pos_y = position_y

    def add_item_to_board(self) -> None:
        """
        add icon for current player into board
        :return: None
        """
        row = None
        col = None

        if self._joystick_pos_x == 2 and self._joystick_pos_y == 2:
            row = 0
            col = 0
        if self._joystick_pos_x == 22 and self._joystick_pos_y == 2:
            row = 0
            col = 1
        if self._joystick_pos_x == 42 and self._joystick_pos_y == 2:
            row = 0
            col = 2
        if self._joystick_pos_x == 2 and self._joystick_pos_y == 22:
            row = 1
            col = 0
        if self._joystick_pos_x == 22 and self._joystick_pos_y == 22:
            row = 1
            col = 1
        if self._joystick_pos_x == 42 and self._joystick_pos_y == 22:
            row = 1
            col = 2
        if self._joystick_pos_x == 2 and self._joystick_pos_y == 42:
            row = 2
            col = 0
        if self._joystick_pos_x == 22 and self._joystick_pos_y == 42:
            row = 2
            col = 1
        if self._joystick_pos_x == 42 and self._joystick_pos_y == 42:
            row = 2
            col = 2

        if row is not None and col is not None and self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.move = True

    def draw_board(self) -> None:
        """
        draw full game board on screen
        :return: None
        """
        self.display.rect(0, 0, 61, 61, 1)
        self.display.hline(0, 20, 60, 1)
        self.display.hline(0, 40, 60, 1)
        self.display.vline(20, 0, 60, 1)
        self.display.vline(40, 0, 60, 1)

        for index_x, row in enumerate(self.board):
            for col, item in enumerate(row):
                self._draw_icon(name=item, row=index_x, col=col)

        self.display.rect(self._joystick_pos_x, self._joystick_pos_y, 17, 17, 1)

        if self.current_player == 'cross':
            self.display.fill_rect(65, 32, 55, 20, 1)
            color_one = 1
            color_two = 0
        elif self.current_player == 'circle':
            self.display.fill_rect(65, 0, 55, 20, 1)
            color_one = 0
            color_two = 1
        else:
            color_one = 0
            color_two = 0

        self.display.text(str(list(self.players)[0]), 65, 1, int(color_one))
        self.display.text(str(list(self.players.values())[0]), 65, 11, int(color_one))

        self.display.text(str(list(self.players)[1]), 65, 33, int(color_two))
        self.display.text(str(list(self.players.values())[1]), 65, 43, int(color_two))

    def _draw_icon(self, name: str, row: int, col: int) -> None:
        """
        draw icons (cross or circle) on specific x,y coordinate
        :param name: icon name
        :param row: number of row
        :param col: number of col
        :return: None
        """
        if name == 'cross':
            icon = self._cross_icon
        elif name == 'circle':
            icon = self._circle_icon
        else:
            icon = None

        if icon:
            item = f'{row}{col}'
            for y, row in enumerate(icon):
                for x, c in enumerate(row):
                    self.display.pixel(int(self._matrix[item][0]) + x, int(self._matrix[item][1]) + y, c)

    def empty_board(self) -> None:
        """
        clean board to start new round
        :return: None
        """
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def check_board(self) -> bool:
        """
        verify if specific player win
        :return: bool
        """
        player = self.current_player

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False


class Joystick:
    def __init__(self, x_axis: int, y_axis: int, btn: int):
        """
        joystick constructor
        :param x_axis: GPIO pin for x-axis
        :param y_axis: GPIO pin for y-axis
        :param btn: GPIO pin for button
        """
        self._adc_x = ADC(Pin(int(x_axis), Pin.IN))
        self._adc_x.atten(ADC.ATTN_11DB)

        self._adc_y = ADC(Pin(int(y_axis), Pin.IN))
        self._adc_y.atten(ADC.ATTN_11DB)

        self.button_pressed = False
        self._last_time = 0
        self._btn = Pin(int(btn), Pin.IN, Pin.PULL_UP)
        self._btn.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._btn_handler)

    def _btn_handler(self, pin) -> None:
        """
        IRQ handler/debounce for button
        :param pin: pin object
        :return: None
        """
        new_time = ticks_ms()

        if (new_time - self._last_time) > 500 and pin.value() == 0:
            self.button_pressed = True
        else:
            self.button_pressed = False

    def _get_raw_values(self) -> tuple:
        """
        read raw analog values from ADC pins
        :return: tuple
        """
        raw_x = self._adc_x.read_u16()
        raw_y = self._adc_y.read_u16()

        return raw_x, raw_y

    def get_coordinates(self) -> tuple:
        """
        get calculated x,y coordinate for joystick
        :return: tuple
        """
        max_x = 60
        max_y = 60

        x, y = self._get_raw_values()

        x_pos = int(x * (max_x / 65535))
        y_pos = int(y * (max_y / 65535))

        return x_pos, y_pos


def flash(screen) -> None:
    """
    flash screen
    :param screen: display object
    :return: None
    """
    value = 1

    for i in range(6):
        if value == 1:
            screen.oled.invert(value)
            value = 0
        else:
            screen.oled.invert(value)
            value = 1
        sleep_ms(100)


if __name__ == '__main__':
    display = Display(sda=SDA_PIN, scl=SCL_PIN, dc=DC_PIN, cs=CS_PIN, res=RES_PIN, width=DP_WIDTH, height=DP_HEIGHT)
    game = GameBoard(screen=display.oled)
    control = Joystick(x_axis=ADC_X_PIN, y_axis=ADC_Y_PIN, btn=BUTTON_PIN)

    while True:
        win_round = False
        display.oled.fill(0)

        if list(game.players.values())[0] >= 10 or list(game.players.values())[1] >= 10:
            break

        joystick_x_pos, joystick_y_pos = control.get_coordinates()
        game.set_cursor(pos_x=joystick_x_pos, pos_y=joystick_y_pos)
        if control.button_pressed:
            game.add_item_to_board()

        if game.check_board():
            game.players[game.current_player] += 1
            win_round = True

        game.draw_board()
        display.oled.show()

        if win_round:
            flash(screen=display)
            game.empty_board()

        if game.move:
            game.move = False
            for key in game.players.keys():
                if key not in game.current_player:
                    game.current_player = key
                    break

        search = ''
        if not any(search in sublist for sublist in game.board):
            flash(screen=display)
            game.empty_board()

        sleep_ms(100)

    txt_0 = f'{str(list(game.players)[0]):6}: {str(list(game.players.values())[0])}'
    txt_1 = f'{str(list(game.players)[1]):6}: {str(list(game.players.values())[1])}'

    display.oled.text('Result', 10, 10, 1)
    display.oled.hline(10, 20, 80, 1)
    display.oled.text(txt_0, 10, 25, 1)
    display.oled.text(txt_1, 10, 35, 1)

    display.oled.show()
