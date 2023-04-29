from micropython import const
from machine import I2C, Pin
from usys import exit


I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)
I2C_FREQUENCY = const(400000)


def list_devices(i2c_devices: list) -> None:
    """
    print out the list of I2C devices
    :param i2c_devices: list of I2C devices
    :return: None
    """
    count = len(i2c_devices)

    if count == 0:
        print('[INFO] No I2C device found')
    else:
        print(f'[INFO] {count} device(s) found')
        for device in i2c_devices:
            print(f'[INFO] Decimal address: {device} Hex address: {hex(device)}')


if __name__ == '__main__':
    if 0 < I2C_FREQUENCY >= 500000:
        print(f'[ERROR] Wrong value for I2C frequency')
        exit()

    i2c = None
    try:
        i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=I2C_FREQUENCY)
    except Exception as err:
        print(f'[ERROR] I2C bus initialization failed: {err}')

    if i2c:
        print('[INFO] Scanning the I2C bus')
        devices = i2c.scan()
        list_devices(devices)
