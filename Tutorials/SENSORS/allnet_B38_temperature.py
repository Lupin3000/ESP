from micropython import const
from machine import Pin, I2C


# define constants
I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)
I2C_ADDRESS = const(79)


def convert_data(value: bytes) -> float:
    """
    Convert bytes to float value (degrees Celsius)
    :param value: bytes
    :return: float
    """
    temp_c = (value[0] << 5) | (value[1] >> 3)
    if (temp_c >> 11) == 1:
        temp_c = temp_c - (1 << 13)
    temp_c = temp_c * 0.03125

    return temp_c


if __name__ == '__main__':
    i2c = None

    try:
        i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
    except Exception as err:
        print(f'[ERROR] I2C bus initialization failed: {err}')

    if i2c:
        data = bytearray(2)
        i2c.readfrom_mem_into(I2C_ADDRESS, 0x00, data)
        print(f'[INFO] {convert_data(data)} °C')
