from micropython import const
from machine import Pin
from neopixel import NeoPixel


# define constants
NEOPIXEL_ROWS = const(10)
NEOPIXEL_COLS = const(16)
NUMBER_PIXELS = const(NEOPIXEL_ROWS * NEOPIXEL_COLS)
LED_GPIO_PIN = const(23)

# create neopixel matrix object
matrix = NeoPixel(Pin(LED_GPIO_PIN), NUMBER_PIXELS)

# digit matrix
nums = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0,  # 0
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
        1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 7
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]  # 9


def clear_matrix() -> None:
    """
    Turn off all LED's on matrix
    :return: None
    """
    for pixel in range(NUMBER_PIXELS):
        matrix[pixel] = (0, 0, 0)
        matrix.write()


def fill_matrix(color: tuple) -> None:
    """
    Set all LED's on matrix to same rgb color
    :param color: tuple for RGB
    :return: None
    """
    for value in color:
        if not 0 <= int(value) <= 255:
            raise Exception('Tuple parameter not in range 0 to 255')

    for pixel in range(NUMBER_PIXELS):
        matrix[pixel] = color
        matrix.write()


def set_matrix_index(number: int, color: tuple) -> None:
    """
    Set specific LED on matrix via index to rgb color
    :param number: int for pixel index
    :param color: tuple for rgb color
    :return: None
    """
    if int(number) < 0:
        error = TypeError("Parameter 'number' must be positive")
        raise Exception(error)

    if int(number) > (NUMBER_PIXELS - 1):
        raise Exception(f"Parameter 'number' maximum is {NUMBER_PIXELS - 1}")

    for value in color:
        if not 0 <= int(value) <= 255:
            raise Exception('Tuple parameter not in range 0 to 255')

    matrix[int(number)] = color
    matrix.write()


def set_matrix_coordinate(x: int, y: int, color: tuple) -> None:
    """
    Set specific LED on matrix via x,y coordinates to rgb color
    :param x: int for x coordinate on matrix
    :param y: int for y coordinate on matrix
    :param color: tuple for rgb color
    :return: None
    """
    if int(x) < 0 or int(y) < 0:
        error = TypeError("Parameter must be positive")
        raise Exception(error)

    if int(x) > (NEOPIXEL_COLS - 1):
        raise Exception(f"Parameter 'x' cannot higher {NEOPIXEL_COLS - 1}")

    if int(y) > (NEOPIXEL_ROWS - 1):
        raise Exception(f"Parameter 'y' cannot higher {NEOPIXEL_ROWS - 1}")

    index = int(y) * int(NEOPIXEL_COLS) + int(x)
    set_matrix_index(index, color)


def draw_horizontal_line(x: int, y: int, length: int, color: tuple) -> None:
    """
    Draw horizontal line with specific start from x,y coordinates, length in pixel and rgb color
    :param x: int for start coordinate x on matrix
    :param y:int for start coordinate y on matrix
    :param length: length in pixel of horizontal line
    :param color: tuple for rgb color
    :return: None
    """
    for item in range(length):
        x_cal = x + item
        if x_cal <= (NEOPIXEL_COLS - 1):
            set_matrix_coordinate(x_cal, y, color)


def draw_vertical_line(x: int, y: int, length: int, color: tuple) -> None:
    """
    Draw vertical line with specific start from x,y coordinates, length in pixel and rgb color
    :param x: int for start coordinate x on matrix
    :param y: int for start coordinate y on matrix
    :param length: int for length in pixel of vertical line
    :param color: tuple for rgb color
    :return: None
    """
    for item in range(length):
        y_cal = y + item
        if y_cal <= (NEOPIXEL_ROWS - 1):
            set_matrix_coordinate(x, y_cal, color)


def draw_rectangle(x: int, y: int, length: int, height: int, color: tuple) -> None:
    """
    Draw a rectangle with specific start from x,y coordinates, length, height in pixel and rgb color
    :param x: int for start coordinate x on matrix
    :param y: int for start coordinate y on matrix
    :param length: int for length in pixel of rectangle
    :param height: int for height in pixel of rectangle
    :param color: tuple for RGB
    :return: None
    """
    draw_horizontal_line(x, y, length, color)
    draw_horizontal_line(x, (y + height - 1), length, color)
    draw_vertical_line(x, y, height, color)
    draw_vertical_line((x + length - 1), y, height, color)


def show_digit(val: int, x: int, y: int, color: tuple) -> None:
    """
    Show digit from 0 to 9, placed by coordinates x,y in rgb color
    :param val: int from 0 to 9
    :param x: int for start coordinate x on matrix
    :param y: int for start coordinate x on matrix
    :param color: tuple for RGB
    :return: None
    """
    if NEOPIXEL_COLS < 3 or NEOPIXEL_ROWS < 3:
        raise Exception("Matrix does not provide enough LED's (min is 3x3)")

    if int(val) < 0:
        error = TypeError("Parameter 'val' must be positive")
        raise Exception(error)

    offset = val * 15

    for item in range(offset, offset + 15):
        if nums[item] == 1:
            xt = item % 3
            yt = (item - offset) // 3
            set_matrix_coordinate(xt + x, yt + y, color)


def show_time(hh: int, mm: int, color: tuple) -> None:
    """
    Display time on matrix
    :param hh: int of hour (one or two digits)
    :param mm: int of minute (one or two digits)
    :param color: tuple for RGB
    :return: None
    """
    if NEOPIXEL_COLS < 16 or NEOPIXEL_ROWS < 3:
        raise Exception("Matrix does not provide enough LED's (min is 16x3)")

    clear_matrix()

    hour_list = [int(item) for item in str(hh)]
    minute_list = [int(item) for item in str(mm)]
    hour_str = ''.join(map(str, hour_list))
    minute_str = ''.join(map(str, minute_list))
    time = f'{int(hour_str):02d}{int(minute_str):02d}'
    x = [int(item) for item in str(time)]

    show_digit(x[0], 0, 2, color)
    show_digit(x[1], 4, 2, color)
    show_digit(x[2], 9, 2, color)
    show_digit(x[3], 13, 2, color)


if __name__ == '__main__':
    # clear matrix
    clear_matrix()

    # set all neopixel to same color
    fill_matrix((125, 0, 0))

    # clear matrix
    clear_matrix()

    # set neopixel to specific color (by index)
    for index in range(0, NUMBER_PIXELS, 2):
        set_matrix_index(index, (10, 10, 10))

    # clear matrix
    clear_matrix()

    # set neopixel to specific color (by coordinates)
    for pos_x in range(5):
        for pos_y in range(5):
            set_matrix_coordinate(pos_x, pos_y, (0, 10, 0))

    for pos_x in range(5):
        for pos_y in range(5):
            set_matrix_coordinate(5 + pos_x, 5 + pos_y, (0, 0, 10))

    for pos_x in range(5):
        for pos_y in range(5):
            set_matrix_coordinate(10 + pos_x, pos_y, (10, 0, 0))

    # clear matrix
    clear_matrix()

    # draw horizontal lines
    for item in range(NEOPIXEL_ROWS):
        draw_horizontal_line(0, item, 5 + item, (25, 25, 1 * item))

    # clear matrix
    clear_matrix()

    # draw vertical lines
    for item in range(15, -1, -1):
        draw_vertical_line(item, 0, 10, (10, 10, 10))

    # clear matrix
    clear_matrix()

    # draw rectangles
    draw_rectangle(0, 0, 16, 10, (0, 0, 10))
    draw_rectangle(1, 1, 14, 8, (0, 10, 0))
    draw_rectangle(2, 2, 12, 6, (10, 0, 0))
    draw_rectangle(3, 3, 10, 4, (0, 0, 10))
    draw_rectangle(4, 4, 8, 2, (0, 10, 0))

    # clear matrix
    clear_matrix()

    # show some numbers
    show_digit(1, 5, 1, (100, 100, 0))
    show_digit(2, 0, 3, (100, 0, 100))
    show_digit(3, 10, 4, (0, 100, 100))

    # clear matrix
    clear_matrix()

    # show fake times
    show_time(21, 30, (10, 25, 50))
    show_time(7, 55, (10, 25, 50))
    show_time(10, 5, (10, 25, 50))

    # clear matrix
    clear_matrix()
