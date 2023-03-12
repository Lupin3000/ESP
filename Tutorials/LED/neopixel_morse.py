from micropython import const
from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms


# define constants
GPIO_DATA_PIN = const(23)
LED_NUMBER = const(12)

_DIT = const(200)
_DAH = const(3 * _DIT)
_WORD = const(7 * _DIT)
_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': ' ',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '.':'.-.-.-', ',': '--..--', '?': '..--..', '/': '--..-.', '@': '.--.-.'}


def flash_led(duration: int) -> None:
    """
    flash LED by given duration
    :param duration: time in milliseconds
    :return: None
    """
    global np

    np.fill((100, 100, 100))
    np.write()
    sleep_ms(duration)
    np.fill((0, 0, 0))
    np.write()


def morse(message: str) -> None:
    """
    create morse code
    :param message: message as string
    :return: None
    """
    for letter in str(message):
        morse_code = _CODE.get(letter.upper())
        for code in morse_code:
            if code == '.':
                flash_led(_DIT)
            elif code == '-':
                flash_led(_DAH)
            else:
                sleep_ms(_WORD)
            sleep_ms(_DIT)
        sleep_ms(_DAH)


if __name__ == '__main__':
    np = NeoPixel(Pin(GPIO_DATA_PIN), LED_NUMBER)
    morse('SOS SOS SOS')
