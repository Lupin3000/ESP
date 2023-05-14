from micropython import const
from machine import Pin, SoftI2C
from network import WLAN, AP_IF
from utime import localtime
from bme680 import BME680_I2C
from usocket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


WLAN_ESSID = 'ESP-NETWORK'
WLAN_PASSWORD = '12345678'
SDA_GPIO_PIN = const(21)
SCL_GPIO_PIN = const(22)


class AccessPoint:
    def __init__(self):
        """
        access point constructor
        """
        if len(WLAN_PASSWORD) >= 8:
            self.ap = WLAN(AP_IF)
            self.ap.config(essid=WLAN_ESSID, password=WLAN_PASSWORD)
            self.ap.config(security=4)
            self.ap.active(True)

            while not self.ap.active():
                print('[INFO] Create access point')

    def get_status(self) -> None:
        """
        print access point WLAN information
        :return: None
        """
        config = self.ap.ifconfig()

        print(f"{'SSID' : <15} {self.ap.config('ssid')}")
        print(f"{'IP' : <15} {config[0]}")
        print(f"{'Subnet' : <15} {config[1]}")


class BME680:
    def __init__(self):
        """
        BME680 sensor constructor
        """
        i2c = SoftI2C(scl=Pin(SCL_GPIO_PIN), sda=Pin(SDA_GPIO_PIN))
        self.bme = BME680_I2C(i2c=i2c)

    def get_values(self) -> dict:
        """
        get values from BME680 sensor
        :return: dict
        """
        dictionary = {}

        try:
            dictionary['temperature'] = str(round(self.bme.temperature, 2))
            dictionary['humidity'] = str(round(self.bme.humidity, 2))
            dictionary['pressure'] = str(round(self.bme.pressure, 2))
            dictionary['gas'] = str(round(self.bme.gas / 1000, 2))
        except OSError as err:
            print(f'[ERROR] Failed to read sensor: {err}')

        return dictionary


if __name__ == '__main__':
    wifi = AccessPoint()
    wifi.get_status()

    if wifi.ap.active():
        sensor = BME680()

        listener = socket(AF_INET, SOCK_STREAM)
        listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        listener.bind(('', 80))
        listener.listen(5)

        while True:
            sensor_values = sensor.get_values()
            year, month, day, hour, minutes, _, _, _ = localtime()

            connection, address = listener.accept()
            request = connection.recv(1024)

            try:
                header = 'HTTP/1.1 200 OK\n'
                file = open('template.htm', 'rb')
                response = file.read().decode('utf-8')
                response = response.replace('<!-- date -->', f'{year}/{month}/{day}')
                response = response.replace('<!-- time -->', f'{hour}:{minutes}')
                response = response.replace('<!-- temperature -->', sensor_values['temperature'])
                response = response.replace('<!-- humidity -->', sensor_values['humidity'])
                response = response.replace('<!-- pressure -->', sensor_values['pressure'])
                response = response.replace('<!-- gas -->', sensor_values['gas'])
                file.close()
            except Exception as err:
                header = 'HTTP/1.1 404 Not Found\n'
                response = 'Error 404'

            connection.send(header.encode('utf-8'))
            connection.send('Content-Type: text/html\n')
            connection.send('Connection: close\n\n')
            connection.sendall(response)
            connection.close()
