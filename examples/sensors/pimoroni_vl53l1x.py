from micropython import const
from machine import Pin, I2C
from vl53l1x import VL53L1X
from utime import sleep_ms


I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)


if __name__ == '__main__':
    i2c = None

    try:
        i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
    except Exception as err:
        print(f'[ERROR] I2C bus initialization failed: {err}')

    if i2c:
        distance = VL53L1X(i2c)
        while True:
            print(f"[INFO] distance: {distance.read()}mm")
            sleep_ms(50)
