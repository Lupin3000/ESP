from micropython import const
from machine import Pin, I2C
from time import sleep
from bme680 import *


SDA_GPIO_PIN = const(21)
SCL_GPIO_PIN = const(22)
NL = const('\n')


if __name__ == '__main__':
    i2c = I2C(scl=Pin(SCL_GPIO_PIN), sda=Pin(SDA_GPIO_PIN))
    bme = BME680_I2C(i2c=i2c)

    while True:
        try:
            temp = str(round(bme.temperature, 2)) + ' C'
            hum = str(round(bme.humidity, 2)) + ' %'
            pres = str(round(bme.pressure, 2)) + ' hPa'
            gas = str(round(bme.gas / 1000, 2)) + ' KOhms'

            print('[INFO] BME 680')
            print(f'Temperature: {temp}')
            print(f'Humidity: {hum}')
            print(f'Pressure: {pres}')
            print(f'Gas: {gas} {NL}')
        except OSError as e:
            print('[ERROR] Failed to read sensor.')

        sleep(5)
