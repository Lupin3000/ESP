from micropython import const
from machine import Pin
from utime import sleep


PIN_R1 = const(2)
PIN_R2 = const(4)
PIN_R3 = const(5)
PIN_R4 = const(18)

PIN_C1 = const(19)
PIN_C2 = const(21)
PIN_C3 = const(22)
PIN_C4 = const(23)


def scan_keypad(row: int, col: int) -> int:
    """
    enable keypad rows and verify cols
    :param row: integer for row number
    :param col: integer for col number
    :return: integer
    """
    global row_pins
    global col_pins

    row_pins[row].value(1)

    if col_pins[col].value():
        status = 1
    else:
        status = 0

    row_pins[row].value(0)

    return status


if __name__ == '__main__':
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    row_pins = [
        Pin(PIN_R1, mode=Pin.OUT, value=0),
        Pin(PIN_R2, mode=Pin.OUT, value=0),
        Pin(PIN_R3, mode=Pin.OUT, value=0),
        Pin(PIN_R4, mode=Pin.OUT, value=0)
    ]
    col_pins = [
        Pin(PIN_C1, mode=Pin.IN, pull=Pin.PULL_DOWN),
        Pin(PIN_C2, mode=Pin.IN, pull=Pin.PULL_DOWN),
        Pin(PIN_C3, mode=Pin.IN, pull=Pin.PULL_DOWN),
        Pin(PIN_C4, mode=Pin.IN, pull=Pin.PULL_DOWN)
    ]

    print('Please press any key on Keypad:')
    while True:
        for row_item in range(4):
            for col_item in range(4):
                value = scan_keypad(row_item, col_item)
                if value == 1:
                    print(f"[INFO] Key {keys[row_item][col_item]} pressed")
                    sleep(0.25)
