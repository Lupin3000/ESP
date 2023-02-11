from micropython import const
from machine import Pin
from neopixel import NeoPixel
from random import randint
from utime import sleep, sleep_ms


# define constants
NEOPIXEL_NUMBER = const(90)
LED_GPIO_PIN = const(23)
DELAY = const(5)

# create neopixel object
nps = NeoPixel(Pin(LED_GPIO_PIN), NEOPIXEL_NUMBER)


def value_verification(value: int, minimum: int = 0, maximum: int = 255) -> bool:
    """
    Verify if specific value is between specific minimum and maximum values
    :param value: int of value
    :param minimum: int of minimum value (default = 0)
    :param maximum: int of maximum value (default = 255)
    :return: bool
    """
    if int(minimum) <= int(value) <= int(maximum):
        return True
    else:
        return False


def random_rgb() -> tuple:
    """
    Return random rgb tuple with 3 items (between 0 and 255)
    :return: tuple
    """
    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rgb


def clear_all() -> None:
    """
    Turn off all LED's by rgb value (0, 0, 0)
    :return: None
    """
    for item in range(NEOPIXEL_NUMBER):
        nps[item] = (0, 0, 0)
        nps.write()


def set_color(red: int, green: int, blue: int) -> None:
    """
    Set all LED's (on) in specific rgb color
    :param red: int between 0 and 255
    :param green: int between 0 and 255
    :param blue: int between 0 and 255
    :return: None
    """
    arg_verify = True

    if not value_verification(value=red):
        print(f'[ERROR] wrong argument {red} for parameter red')
        arg_verify = False

    if not value_verification(value=green):
        print(f'[ERROR] wrong argument {green} for parameter green')
        arg_verify = False

    if not value_verification(value=blue):
        print(f'[ERROR] wrong argument {blue} for parameter blue')
        arg_verify = False

    if arg_verify:
        for item in range(NEOPIXEL_NUMBER):
            nps[item] = (red, green, blue)
            nps.write()


def cycle_color(foreground: tuple, background: tuple, rounds: int = 1, wait: int = 10) -> None:
    """
    Cycle a single LED in specific rgb color
    :param foreground: tuple of foreground rgb colors eq. (255, 0, 0)
    :param background: tuple of background rgb colors eq. (0, 0, 0)
    :param rounds: int (minimum is 1, default = 1)
    :param wait: int (minimum is 1, default = 10) in milliseconds
    :return: None
    """
    arg_verify = True
    count = 1

    if not value_verification(value=foreground[0], minimum=0, maximum=255):
        print(f'[ERROR] wrong argument {foreground[0]} for parameter foreground red')
        arg_verify = False

    if not value_verification(value=foreground[1], minimum=0, maximum=255):
        print(f'[ERROR] wrong argument {foreground[1]} for parameter foreground green')
        arg_verify = False

    if not value_verification(value=foreground[2], minimum=0, maximum=255):
        print(f'[ERROR] wrong argument {foreground[2]} for parameter foreground blue')
        arg_verify = False

    if not value_verification(minimum=0, maximum=255, value=background[0]):
        print(f'[ERROR] wrong argument {background[0]} for parameter background red')
        arg_verify = False

    if not value_verification(minimum=0, maximum=255, value=background[1]):
        print(f'[ERROR] wrong argument {background[1]} for parameter background green')
        arg_verify = False

    if not value_verification(minimum=0, maximum=255, value=background[2]):
        print(f'[ERROR] wrong argument {background[2]} for parameter background blue')
        arg_verify = False

    if not int(rounds) >= 1:
        print(f'[ERROR] wrong argument {rounds} for parameter rounds')
        arg_verify = False

    if not int(wait) >= 1:
        print(f'[ERROR] wrong argument {wait} for parameter wait')
        arg_verify = False

    if arg_verify:
        set_color(background[0], background[1], background[2])

        while count <= rounds:
            count += 1
            for item in range(NEOPIXEL_NUMBER):
                nps[item] = (foreground[0], foreground[1], foreground[2])
                nps[item - 1] = background
                nps.write()
                sleep_ms(wait)


def random_colors(value: str = 'single') -> None:
    """
    Set LED's to random rgb color value specified by parameter argument
    :param value: string of either 'all' or 'single' (default = 'single')
    :return: None
    """
    valid = {'all', 'single'}

    if value in valid and value == 'single':
        for item in range(NEOPIXEL_NUMBER):
            nps[item] = random_rgb()
            nps.write()

    if value in valid and value == 'all':
        color = random_rgb()
        for item in range(NEOPIXEL_NUMBER):
            nps[item] = color
            nps.write()


while True:
    print('[INFO] Set each LED to random color')
    random_colors()
    sleep(DELAY)

    print("[INFO] Set all LED's to random color")
    random_colors('all')
    sleep(DELAY)

    print("[INFO] Turn off all LED's")
    clear_all()
    sleep(DELAY)

    print("[INFO] Set all LED's to same color")
    set_color(150, 150, 150)
    sleep(DELAY)

    print("[INFO] Cycle LED's with specific colors")
    cycle_color(foreground=(255, 0, 0), background=(0, 0, 0), rounds=3, wait=50)

    print("[INFO] Cycle LED's with specific colors")
    cycle_color(foreground=(0, 0, 0), background=(0, 255, 0), rounds=3, wait=25)
