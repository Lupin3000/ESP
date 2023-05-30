from micropython import const
from machine import Pin, SoftI2C, ADC
from lib.ssd1306 import SSD1306_I2C
from pictures import alien_screen, human_icon, space_ship
from urandom import randrange
from utime import sleep_ms, ticks_ms


DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
DISPLAY_SDA_PIN = const(21)
DISPLAY_SCL_PIN = const(22)

ADC_X_PIN = const(26)
ADC_Y_PIN = const(25)
BUTTON_PIN = const(33)


class Display:
    def __init__(self, sda: int, scl: int, width: int, height: int):
        """
        Display constructor
        :param sda: SDA pin
        :param scl: SCL pin
        :param width: display width in pixel
        :param height: display height in pixel
        """
        self.width = int(width)
        self.height = int(height)

        i2c = SoftI2C(sda=Pin(int(sda)), scl=Pin(int(scl)))
        self.oled = SSD1306_I2C(self.width, self.height, i2c)

    def draw_on_screen(self, x: int, y: int) -> None:
        """
        draw pixel on display
        :param x: x-coordinate for pixel
        :param y: y-coordinate for pixel
        :return: None
        """
        self.oled.pixel(x, y, 1)

    def draw_circle(self, x_pos: int, y_pos: int, rad: int) -> None:
        """
        draw circle on display
        :param x_pos: x-coordinate for center
        :param y_pos: y-coordinate for center
        :param rad: radius for circle
        :return: None
        """
        x = rad - 1
        y = 0
        dx = 1
        dy = 1
        err = dx - (rad << 1)

        while x >= y:
            if err <= 0:
                y += 1
                err += dy
                dy += 2

            if err > 0:
                x -= 1
                dx += 2
                err += dx - (rad << 1)

            self.draw_on_screen(x_pos + x, y_pos + y)
            self.draw_on_screen(x_pos + y, y_pos + x)
            self.draw_on_screen(x_pos - y, y_pos + x)
            self.draw_on_screen(x_pos - x, y_pos + y)
            self.draw_on_screen(x_pos - x, y_pos - y)
            self.draw_on_screen(x_pos - y, y_pos - x)
            self.draw_on_screen(x_pos + y, y_pos - x)
            self.draw_on_screen(x_pos + x, y_pos - y)


class Introduction:
    def __init__(self, display):
        """
        introduction constructor
        :param display: display object
        """
        self.screen = display

    def _typewriter_effect(self, data: str, x: int, y: int, speed: int = 200) -> None:
        """
        create typewriter effect for specific string on display
        :param data: text for effect on display
        :param x: x-coordinate for text
        :param y: y-coordinate for text
        :param speed: speed for effect
        :return: None
        """
        text = str(data)
        text_length = len(text)

        for letter in range(text_length + 1):
            self.screen.text(text[:letter], int(x), int(y))
            self.screen.show()

            sleep_ms(int(speed))

    def play_intro(self) -> None:
        """
        play complete intro on display
        :return: None
        """
        self.screen.fill(0)
        self.screen.invert(1)
        self.screen.blit(alien_screen, 0, 0)
        self.screen.show()
        sleep_ms(1750)

        self.screen.invert(0)
        self.screen.fill(0)
        self.screen.show()
        self._typewriter_effect("Message: A31K88", 0, 10, 100)
        self._typewriter_effect("Human attack us", 0, 25, 100)
        self._typewriter_effect(" Help required ", 0, 35, 100)
        sleep_ms(500)


class Joystick:
    def __init__(self, x: int, y: int, btn: int, width: int, height: int):
        """
        analog joystick constructor
        :param x: GPIO pin for x
        :param y: GPIO pin for y
        :param btn: GPIO pin for button
        :param width: display width in pixel
        :param height: display height in pixel
        """
        self._width = int(width)
        self._height = int(height)

        self.last_time = 0
        self.btn_pressed = False

        self._adc_x = ADC(Pin(int(x), Pin.IN))
        self._adc_x.atten(ADC.ATTN_11DB)

        self._adc_y = ADC(Pin(int(y), Pin.IN))
        self._adc_y.atten(ADC.ATTN_11DB)

        self._btn = Pin(int(btn), Pin.IN, Pin.PULL_UP)
        self._btn.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self._btn_handler)

    def _btn_handler(self, pin) -> None:
        """
        IRQ handler
        :param pin: pin object
        :return: None
        """
        new_time = ticks_ms()

        if (new_time - self.last_time) > 200 and pin.value() == 0:
            self.btn_pressed = True
        else:
            self.btn_pressed = False

    def _get_raw_analog_values(self) -> tuple:
        """
        get raw x,y values from ADC GPIOs
        :return: tuple
        """
        adc_x_val = self._adc_x.read_u16()
        adc_y_val = self._adc_y.read_u16()

        return adc_x_val, adc_y_val

    def get_xy_coordinates(self) -> tuple:
        """
        convert raw values (and restrict) x,y coordinate to display
        :return: tuple
        """
        x, y = self._get_raw_analog_values()

        x_pos = int(x * (self._width / 65535))
        if x_pos <= 5:
            x_pos = 5

        if x_pos >= (self._width - 6):
            x_pos = (self._width - 6)

        y_pos = int(y * (self._height / 65535))
        if y_pos <= 5:
            y_pos = 5

        if y_pos >= (self._height - 20):
            y_pos = (self._height - 20)

        return x_pos, y_pos

    def get_overlap(self, x: int, y: int, w: int, h: int) -> bool:
        """
        verify if crosshair overlaps object
        :param x: rectangle x coordinate
        :param y: rectangle y coordinate
        :param w: rectangle width in pixel
        :param h: rectangle height in pixel
        :return: bool
        """
        ch_x, ch_y = self.get_xy_coordinates()

        if int(x) < ch_x < (int(x) + int(w)) and int(y) < ch_y < (int(y) + int(h)):
            return True
        else:
            return False


if __name__ == '__main__':
    screen = Display(sda=DISPLAY_SDA_PIN, scl=DISPLAY_SCL_PIN, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

    intro = Introduction(display=screen.oled)
    intro.play_intro()
    del intro

    control = Joystick(x=ADC_X_PIN, y=ADC_Y_PIN, btn=BUTTON_PIN, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

    while True:
        screen.oled.fill(0)

        if control.btn_pressed:
            break
        else:
            screen.oled.fill_rect(18, 23, 100, 21, 1)
            screen.oled.text('Press button', 20, 25, 0)
            screen.oled.text('  to Start  ', 20, 35, 0)
            screen.oled.show()

        sleep_ms(100)

    shield = 15000
    pos_rx = randrange(-38, -16)
    speed_r = randrange(2, 4)
    pos_lx = randrange(128, 148)
    speed_l = randrange(2, 4)

    while True:
        if shield <= 0:
            break

        screen.oled.fill(0)
        ch_x_pos, cs_y_pos = control.get_xy_coordinates()

        screen.oled.pixel(50, 10, 1)
        screen.oled.pixel(120, 20, 1)
        screen.oled.pixel(5, 5, 1)
        screen.oled.pixel(75, 15, 1)
        screen.oled.pixel(10, 20, 1)

        pos_rx += speed_r
        pos_lx -= speed_l
        screen.oled.blit(human_icon, pos_rx, 28)
        screen.oled.blit(human_icon, pos_lx, 28)

        if control.btn_pressed:
            if control.get_overlap(pos_rx, 28, 16, 20):
                speed_r = randrange(2, 4)
                pos_rx = randrange(-38, -16)

            if control.get_overlap(pos_lx, 28, 16, 20):
                speed_l = randrange(2, 4)
                pos_lx = randrange(128, 148)

        if pos_rx >= 50:
            shield -= 1000
            speed_r = randrange(2, 4)
            pos_rx = randrange(-38, -16)

        if pos_lx <= 60:
            shield -= 1000
            speed_l = randrange(2, 4)
            pos_lx = randrange(128, 148)

        screen.oled.rect(0, 0, screen.oled.width, screen.oled.height, 1)
        screen.oled.hline(0, 50, screen.oled.width, 1)
        screen.oled.text(f'Shield:{str(shield)}', 10, 53, 1)

        screen.oled.blit(space_ship, 50, 25)

        screen.draw_circle(ch_x_pos, cs_y_pos, 4)

        for i in range(-5, 5, 1):
            if i < 0:
                screen.draw_on_screen(ch_x_pos - i, cs_y_pos)
                screen.draw_on_screen(ch_x_pos, cs_y_pos - i)
            if i == 0:
                screen.draw_on_screen(ch_x_pos, cs_y_pos)
            if i < 0:
                screen.draw_on_screen(ch_x_pos + i, cs_y_pos)
                screen.draw_on_screen(ch_x_pos, cs_y_pos + i)

        screen.oled.show()
        sleep_ms(75)

    screen.oled.fill(0)
    screen.oled.text('Shield lost', 20, 20)
    screen.oled.text('Humans win', 20, 30)
    screen.oled.show()
