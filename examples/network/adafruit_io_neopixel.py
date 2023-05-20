from micropython import const
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import urequests as requests
import ujson as json


NEOPIXEL_PIN = const(23)
NEOPIXEL_NUMBER = const(160)
ADAFRUIT_IO_USER = 'YOUR USER NAME'
ADAFRUIT_IO_KEY = 'YOUR IO KEY'
ADAFRUIT_IO_FEED = 'YOUR FEED KEY'


class AdafruitIO:
    def __init__(self, usr: str, key: str, feed: str):
        """
        constructor
        :param usr: user name for adafruit io
        :param key: adafruit io key
        :param feed: adafruit feed key (not feed name!)
        """
        self.__user = str(usr)
        self.__key = str(key)
        self.__feed = str(feed)

    @staticmethod
    def hex_to_rgb(value: str) -> tuple:
        """
        convert hex code to integers
        :param value: color hex value
        :return: tuple
        """
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def get_feed(self) -> tuple:
        """
        do feed request and return color tuple
        :return: tuple
        """
        headers = {'X-AIO-Key': self.__key, 'Content-Type': 'application/json'}
        url = "https://io.adafruit.com/api/v2/" + self.__user + "/feeds/" + self.__feed + "/data/last"

        response = requests.get(url, headers=headers)
        parsed = json.loads(response.text)
        hex_val = parsed['value']
        rgb_val = AdafruitIO.hex_to_rgb(hex_val)

        return rgb_val


if __name__ == '__main__':
    io = AdafruitIO(usr=ADAFRUIT_IO_USER, key=ADAFRUIT_IO_KEY, feed=ADAFRUIT_IO_FEED)
    nps = NeoPixel(Pin(NEOPIXEL_PIN), NEOPIXEL_NUMBER)

    while True:
        nps.fill(io.get_feed())
        nps.write()
        sleep(0.5)
