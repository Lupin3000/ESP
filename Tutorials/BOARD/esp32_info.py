from machine import RTC, unique_id, freq
from ubinascii import hexlify
from esp32 import hall_sensor, raw_temperature


# create real time clock object
rtc = RTC()

# get information
tuple_rtc = rtc.datetime()
str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'
byte_mac = hexlify(unique_id(), ':')
str_mac = str(byte_mac, 'utf-8')

# show information
print(f"{'Date/Time' : < 15}{str_date} {str_time}")
print(f"{'ID' : < 15}{str_mac}")
print(f"{'CPU' : < 15}{freq()} Hz")
print(f"{'Hall' : < 15}{hall_sensor()}")
print(f"{'MCU' : < 15}{raw_temperature()} Fahrenheit")