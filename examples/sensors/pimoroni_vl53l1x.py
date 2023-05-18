from micropython import const
from machine import Pin, I2C
from vl53l1x import VL53L1X
from ssd1306 import SSD1306_I2C
from utime import sleep_ms


I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)

DISPLAY_HEX = const(0x3C)
SENSOR_HEX = const(0x29)

DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)


class DistanceSensor:
    def __init__(self):
        """
        sensor constructor
        """
        self._i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))

    def get_distance(self) -> int:
        """
        measure and return distance
        :return: int
        """
        sensor_distance = VL53L1X(i2c=self._i2c, address=SENSOR_HEX)

        return int(sensor_distance.read())

    def __del__(self) -> None:
        """
        finalizer to delete i2c object
        :return: None
        """
        self._i2c.deinit()


class Display:
    def __init__(self):
        """
        display constructor
        """
        self._i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
        self._oled = SSD1306_I2C(width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, i2c=self._i2c, addr=DISPLAY_HEX)

    def write_to_display(self, value: int) -> None:
        """
        show value on display
        :param value: integer of distance
        :return: None
        """
        self._oled.fill(0)
        self._oled.text('Distance', 10, 10, 1)
        self._oled.text(f'{int(value)}mm', 10, 20, 1)
        self._oled.show()

    def __del__(self) -> None:
        """
        finalizer to delete i2c object
        :return: None
        """
        self._i2c.deinit()


if __name__ == '__main__':
    sensor = DistanceSensor()
    display = Display()

    while True:
        try:
            distance = sensor.get_distance()
        except KeyboardInterrupt as interrupt:
            print(f'[INFO] interrupt by user')
            del sensor
            del display
        else:
            display.write_to_display(value=distance)

        sleep_ms(500)
