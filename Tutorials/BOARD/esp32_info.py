from machine import RTC, unique_id, freq
from ubinascii import hexlify
from esp32 import hall_sensor, raw_temperature


# create real time clock
rtc = RTC()

# show information
tuple_rtc = rtc.datetime()
str_date_time = f'{tuple_rtc[0]}-{tuple_rtc[1]}-{tuple_rtc[2]} {tuple_rtc[3]}:{tuple_rtc[4]}:{tuple_rtc[5]}'
byte_mac = hexlify(unique_id(), ':')
str_mac = str(byte_mac, 'utf-8')

print(f"{'Date/Time' : < 15}{str_date_time}")
print(f"{'ID' : < 15}{str_mac}")
print(f"{'CPU' : < 15}{freq()} Hz")
print(f"{'Hall' : < 15}{hall_sensor()}")
print(f"{'MCU' : < 15}{raw_temperature()} Fahrenheit")