from micropython import const
from machine import Pin, ADC, SPI
from sh1106 import SH1106_SPI
from urandom import randint
from utime import sleep_ms


GPIO_SDA_PIN = const(23)
GPIO_SCL_PIN = const(18)
GPIO_DC_PIN = const(2)
GPIO_RES_PIN = const(4)
GPIO_CS_PIN = const(5)

DP_WIDTH = const(128)
DP_HEIGHT = const(64)

ADC_X_PIN = const(32)
ADC_Y_PIN = const(33)
BUTTON_PIN = const(35)


class Controller:
    def __init__(self):
        """
        controller constructor
        """
        self.adc_x = ADC(Pin(ADC_X_PIN, Pin.IN))
        self.adc_x.atten(ADC.ATTN_11DB)

        self.adc_y = ADC(Pin(ADC_Y_PIN, Pin.IN))
        self.adc_y.atten(ADC.ATTN_11DB)

    def get_direction(self) -> str:
        """
        get controller snake_direction
        :return: str
        """
        adc_x_val = self.adc_x.read_u16()
        adc_y_val = self.adc_y.read_u16()

        x_pos = int(adc_x_val * (DP_WIDTH / 65535))
        y_pos = int(adc_y_val * (DP_HEIGHT / 65535))

        if x_pos < (DP_WIDTH / 2) - 3:
            return 'left'
        elif x_pos > (DP_WIDTH / 2) + 3:
            return 'right'
        elif y_pos < (DP_HEIGHT / 2) - 3:
            return 'up'
        elif y_pos > (DP_HEIGHT / 2) + 3:
            return 'down'
        else:
            return 'middle'


class GameInterface:
    def __init__(self):
        """
        game interface constructor
        """
        spi = SPI(1, baudrate=1000000, sck=Pin(GPIO_SCL_PIN), mosi=Pin(GPIO_SDA_PIN))

        self.oled = SH1106_SPI(width=DP_WIDTH, height=DP_HEIGHT, spi=spi, rotate=0, delay=0,
                               dc=Pin(GPIO_DC_PIN), res=Pin(GPIO_RES_PIN), cs=Pin(GPIO_CS_PIN))

        self.score = 0
        self._field_x = 3
        self._field_y = 13
        self._field_w = DP_WIDTH - 6
        self._field_h = DP_HEIGHT - 16

    def show_interface(self) -> None:
        """
        create the game interface
        :return: None
        """
        self.oled.rect(0, 0, self.oled.width, self.oled.height, 1)
        self.oled.text(f'Score: {self.score}', 2, 2, 1)
        self.oled.hline(0, 10, self.oled.width, 1)

    def generate_fruit(self) -> tuple:
        """
        generate random x/y coordinates for fruit inside game field
        :return: tuple
        """
        return randint(self._field_x, self._field_w), randint(self._field_y, self._field_h)


if __name__ == '__main__':
    control = Controller()
    interface = GameInterface()
    fruit_pos = interface.generate_fruit()

    snake = [(DP_WIDTH // 2, DP_HEIGHT // 2)]
    snake_size = 10
    snake_dir_x = 1
    snake_dir_y = 0

    while True:
        interface.oled.fill(0)
        interface.show_interface()
        interface.oled.pixel(fruit_pos[0], fruit_pos[1], 1)

        snake_direction = control.get_direction()
        if snake_direction == 'up':
            snake_dir_x = 0
            snake_dir_y = -1
        if snake_direction == 'right':
            snake_dir_x = 1
            snake_dir_y = 0
        if snake_direction == 'down':
            snake_dir_x = 0
            snake_dir_y = 1
        if snake_direction == 'left':
            snake_dir_x = -1
            snake_dir_y = 0

        head = (snake[-1][0] + snake_dir_x, snake[-1][1] + snake_dir_y)
        snake.append(head)

        if len(snake) > snake_size:
            snake.pop(0)

        if head[0] < 1 or head[0] > (DP_WIDTH - 2) or head[1] < 10 or head[1] > (DP_HEIGHT - 1) or head in snake[:-1]:
            break

        for segment in snake:
            interface.oled.pixel(segment[0], segment[1], 1)

        interface.oled.show()

        if head == fruit_pos:
            fruit_pos = interface.generate_fruit()
            snake_size += 5
            interface.score += 1

        sleep_ms(100)

    interface.oled.fill(0)
    interface.oled.text("Game Over", 10, 20)
    interface.oled.text(f'Score: {interface.score}', 10, 30)
    interface.oled.show()
