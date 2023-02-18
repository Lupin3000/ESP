from micropython import const
from machine import Pin, RTC
from dht import DHT11
from utime import sleep


# define constant
DHT_GPIO_PIN = const(5)
DELAY = const(5)
NL = const('\n')

# create DHT11 and RTC objects
sensor = DHT11(Pin(DHT_GPIO_PIN))
rtc = RTC()

if __name__ == '__main__':
    while True:
        try:
            sleep(DELAY)

            tuple_rtc = rtc.datetime()
            str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
            str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'
            sensor.measure()

            # show information
            print(f'Date: {str_date}')
            print(f'Time: {str_time}')
            print(f'Temperature: {sensor.temperature()} °C')
            print(f'Humidity: {sensor.humidity()} %{NL}')
        except OSError as e:
            print('Cannot read sensor.')
