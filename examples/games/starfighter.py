from micropython import const
from machine import Pin, ADC, SoftI2C
from lib.ssd1306 import SSD1306_I2C
from random import randint
from utime import sleep_ms


DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
DISPLAY_SDA_PIN = const(21)
DISPLAY_SCL_PIN = const(22)
ADC_PIN = const(32)


class Display:
    def __init__(self, sda: int, scl: int, width: int, height: int):
        """
        display constructor
        :param sda: GPIO for SDA
        :param scl: GPIO for SCL
        :param width: display width in pixel
        :param height: display height in pixel
        """
        i2c = SoftI2C(sda=Pin(int(sda)), scl=Pin(int(scl)))
        self.oled = SSD1306_I2C(int(width), int(height), i2c)


class Stars:
    def __init__(self, x: int, y: int):
        """
        star constructor
        :param x: x-position for star
        :param y: y-position for star
        """
        self.x = int(x)
        self.y = int(y)


class Enemy:
    def __init__(self):
        """
        enemy constructor
        """
        self.icon = [
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
        ]

        self.width = len(self.icon[0])
        self.height = len(self.icon)

        self.x = int(DISPLAY_WIDTH - self.width - 1)
        self.y = int((DISPLAY_HEIGHT / 2) - (self.height / 2))

        self.speed = 1
        self.shield = 25
        self.bullet_state = "ready"
        self.bullet_speed = 5


class Fighter:
    def __init__(self, pin: int):
        """
        fighter constructor
        :param pin: GPIO pin
        """
        self._adc = ADC(Pin(int(pin), Pin.IN))
        self._adc.atten(ADC.ATTN_11DB)

        self.icon = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.width = len(self.icon[0])
        self.height = len(self.icon)

        self.x = 1
        self.y = None

        self.shield = 25
        self.bullet_state = "ready"
        self.bullet_speed = 5

    def get_position(self) -> None:
        """
        get and set y coordinate for fighter
        :return: None
        """
        y_max = DISPLAY_HEIGHT - self.height - 4
        y_pos = int(self._adc.read_u16() * (DISPLAY_HEIGHT / 65535))

        if y_pos < 1:
            y_pos = 1

        if y_pos > y_max:
            y_pos = y_max

        self.y = y_pos


def add_stars(amount: int) -> None:
    """
    create stars
    :param amount: number of stars
    :return: None
    """
    global stars

    for i in range(int(amount)):
        star = Stars(x=randint(0, DISPLAY_WIDTH - 1), y=randint(0, DISPLAY_HEIGHT - 1))
        stars.append(star)


def is_point_in_rect(point: list, rect: list) -> bool:
    """
    verify if point is inside rectangle
    :param point: list of x, y coordinates for point
    :param rect: list of x, y, width and height for rectangle
    :return: bool
    """
    x1, y1, w, h = rect
    x2, y2 = x1 + w, y1 + h

    x, y = point

    if x1 < x < x2:
        if y1 < y < y2:
            return True
    return False


if __name__ == '__main__':
    display = Display(sda=DISPLAY_SDA_PIN, scl=DISPLAY_SCL_PIN, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

    enemy = Enemy()
    enemy_bullet_x_pos = enemy.x - int(enemy.height / 2)
    enemy_bullet_y_pos = enemy.y

    fighter = Fighter(pin=ADC_PIN)
    fighter_bullet_x_pos = enemy.x - int(fighter.height / 2)
    fighter_bullet_y_pos = enemy.y

    stars = []
    add_stars(amount=20)

    while True:
        if fighter.shield <= 0 or enemy.shield <= 0:
            break

        display.oled.fill(0)

        for item in stars:
            display.oled.pixel(item.x, item.y, 1)

        shield_val = 25 - fighter.shield
        display.oled.fill_rect(1, (DISPLAY_HEIGHT - 3), 27, 3, 1)
        display.oled.fill_rect(2, (DISPLAY_HEIGHT - 2), shield_val, 1, 0)

        fighter.get_position()
        for y, row in enumerate(fighter.icon):
            for x, c in enumerate(row):
                display.oled.pixel(x + fighter.x, y + fighter.y, c)

        if fighter.bullet_state == 'fire':
            fighter_bullet_x_pos += fighter.bullet_speed
            display.oled.fill_rect(fighter_bullet_x_pos, fighter_bullet_y_pos, 3, 2, 1)

        hit = is_point_in_rect(point=[fighter_bullet_x_pos, fighter_bullet_y_pos],
                               rect=[enemy.x, enemy.y, enemy.width, enemy.height])

        if hit:
            enemy.shield -= 5
            fighter.bullet_state = "ready"
            fighter_bullet_x_pos = fighter.x - int(fighter.height / 2)
            fighter_bullet_y_pos = fighter.y

        if fighter_bullet_x_pos > DISPLAY_WIDTH:
            fighter.bullet_state = "ready"
            fighter_bullet_x_pos = fighter.x - int(fighter.height / 2)
            fighter_bullet_y_pos = fighter.y

        if fighter.bullet_state == "ready":
            fighter.bullet_state = 'fire'

        shield_val = 25 - enemy.shield
        display.oled.fill_rect((DISPLAY_WIDTH - 28), (DISPLAY_HEIGHT - 3), 27, 3, 1)
        display.oled.fill_rect((DISPLAY_WIDTH - 27), (DISPLAY_HEIGHT - 2), shield_val, 1, 0)

        if 10 > enemy.shield > 5:
            enemy.speed = 3

        if enemy.shield < 5:
            enemy.speed = 5

        enemy.y -= enemy.speed

        if enemy.y < 1:
            enemy.speed *= -1

        if enemy.y > (DISPLAY_HEIGHT - enemy.height - 4):
            enemy.speed *= -1

        for y, row in enumerate(enemy.icon):
            for x, c in enumerate(row):
                display.oled.pixel(x + enemy.x, y + enemy.y, c)

        if enemy.bullet_state == 'fire':
            enemy_bullet_x_pos -= enemy.bullet_speed
            display.oled.fill_rect(enemy_bullet_x_pos, enemy_bullet_y_pos, 3, 2, 1)

        hit = is_point_in_rect(point=[enemy_bullet_x_pos, enemy_bullet_y_pos],
                               rect=[fighter.x, fighter.y, fighter.width, fighter.height])

        if hit:
            fighter.shield -= 5
            enemy.bullet_state = "ready"
            enemy_bullet_x_pos = enemy.x - int(enemy.height / 2)
            enemy_bullet_y_pos = enemy.y

        if enemy_bullet_x_pos < 0:
            enemy.bullet_state = "ready"
            enemy_bullet_x_pos = enemy.x - int(enemy.height / 2)
            enemy_bullet_y_pos = enemy.y

        if enemy.bullet_state == "ready":
            enemy.bullet_state = 'fire'

        display.oled.show()

        sleep_ms(100)

    display.oled.fill(0)

    if fighter.shield == 0:
        display.oled.text('Enemy win', 10, 20, 1)
    else:
        display.oled.text('You win', 10, 20, 1)

    display.oled.text('the epic match', 10, 30, 1)
    display.oled.show()
