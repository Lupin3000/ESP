from micropython import const
from machine import Pin, ADC, SoftI2C, PWM
from lib.ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer, MONO_HLSB
from urandom import randint
from utime import sleep, sleep_ms


ADC_PIN = const(32)
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)
DISPLAY_SDA_PIN = const(21)
DISPLAY_SCL_PIN = const(22)
BUZZER_PIN = const(18)
BUZZER_DUTY_CYCLE = const(1000)
DURATION_MILLISECONDS = const(1)

IMG_INTRO = 'racer_intro.pbm'
IMG_DEAD = 'racer_dead.pbm'
ICON_CAR = 'racer_car.pbm'
ICON_CAR_WIDTH = const(10)
ICON_CAR_HEIGHT = const(15)

OBSTACLE_WIDTH = const(10)
OBSTACLE_HEIGHT = const(10)

ROAD_LEFT = const(30)
ROAD_RIGHT = const(90)


def draw_road() -> None:
    """
    draw road on screen
    :return: None
    """
    global oled

    oled.vline(ROAD_LEFT, 0, DISPLAY_HEIGHT, 1)
    oled.vline(ROAD_RIGHT, 0, DISPLAY_HEIGHT, 1)


def load_image(filename: str, w: int, h: int):
    """
    load, convert and return class for image
    :param filename: string of path/filename
    :param w: width of image
    :param h: height of image
    :return: class
    """
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        f.readline()
        data = bytearray(f.read())

    return FrameBuffer(data, w, h, MONO_HLSB)


def draw_car(x: int, y: int) -> None:
    """
    draw the car on screen
    :param x: value for x position
    :param y: value for y position
    :return: None
    """
    global oled

    img_car = load_image(ICON_CAR, ICON_CAR_WIDTH, ICON_CAR_HEIGHT)
    oled.blit(img_car, x, y)


def draw_obstacle(x: int, y: int) -> None:
    """
    draw obstacle on screen
    :param x: value for x position
    :param y: value for y position
    :return: None
    """
    global oled

    oled.fill_rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, 1)


def verify_overlap(car_coordinates: list, obstacle_coordinates: list) -> bool:
    car = car_coordinates
    obstacle = obstacle_coordinates

    if (car[0] >= obstacle[2]) or (car[2] <= obstacle[0]) or (car[3] <= obstacle[1]) or (car[1] >= obstacle[3]):
        return False
    else:
        return True


def play_startup_sound():
    """
    play intro sound
    :return: None
    """
    global buzzer

    buzzer.duty_u16(1000)
    buzzer.freq(600)
    sleep(.25)
    buzzer.freq(800)
    sleep(.25)
    buzzer.freq(1200)
    sleep(.25)
    buzzer.duty_u16(0)


def dead_sound() -> None:
    """
    play end sound
    :return: None
    """
    global buzzer

    buzzer.freq(900)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(2)
    buzzer.duty_u16(0)


if __name__ == '__main__':
    adc = ADC(Pin(ADC_PIN, Pin.IN))
    adc.atten(ADC.ATTN_11DB)

    i2c = SoftI2C(sda=Pin(DISPLAY_SDA_PIN), scl=Pin(DISPLAY_SCL_PIN))
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

    buzzer = PWM(Pin(BUZZER_PIN))
    buzzer.duty_u16(0)

    oled.fill(0)
    img_intro = load_image(IMG_INTRO, 128, 64)
    oled.blit(img_intro, 0, 0)
    oled.invert(1)
    oled.show()
    play_startup_sound()

    car_y = 40
    obstacle_x = randint(ROAD_LEFT, ROAD_RIGHT)
    if obstacle_x > ROAD_RIGHT - OBSTACLE_WIDTH:
        obstacle_x = obstacle_x - OBSTACLE_WIDTH
    obstacle_y = 0
    count = 0
    oled.invert(0)

    while True:
        buzzer.duty_u16(1000)
        buzzer.freq(50)

        adc_val = adc.read_u16()
        car_x = int(adc_val * (DISPLAY_WIDTH / 65535))
        if car_x > 100:
            car_x = 110

        if car_x < 10:
            car_x = 10

        crash = verify_overlap(
            car_coordinates=[car_x, car_y, (car_x + ICON_CAR_WIDTH), (car_y + ICON_CAR_WIDTH)],
            obstacle_coordinates=[obstacle_x, obstacle_y, (obstacle_x + OBSTACLE_WIDTH), (obstacle_y + OBSTACLE_HEIGHT)]
        )
        if crash:
            break

        oled.fill(0)
        oled.text(str(count), 0, 0)
        draw_road()
        draw_obstacle(x=obstacle_x, y=obstacle_y)
        draw_car(x=car_x, y=car_y)
        oled.show()

        if obstacle_y > 64:
            count += 1
            buzzer.duty_u16(1000)
            buzzer.freq(1000)
            obstacle_x = randint(ROAD_LEFT, ROAD_RIGHT)
            if obstacle_x > ROAD_RIGHT - OBSTACLE_WIDTH:
                obstacle_x = obstacle_x - OBSTACLE_WIDTH
            obstacle_y = 0
        else:
            obstacle_y += 2

        sleep_ms(DURATION_MILLISECONDS)

        buzzer.duty_u16(0)

    oled.fill(0)
    img_dead = load_image(IMG_DEAD, 128, 64)
    oled.blit(img_dead, 0, 0)
    oled.invert(1)
    oled.show()
    dead_sound()
