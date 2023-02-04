from micropython import const
from machine import I2C, Pin


# define constants
I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)
I2C_FREQUENCY = const(400000)

# create I2C object
i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=I2C_FREQUENCY)

print('[Info] Scanning the I2C bus')
devices = i2c.scan()
device_count = len(devices)

if device_count == 0:
    print('[INFO] No I2C device found')
else:
    print(f'[INFO] {device_count} device(s) found')

    for device in devices:
        print(f'[INFO] Decimal address: {device} Hex address: {hex(device)}')
