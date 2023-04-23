from machine import unique_id, freq, RTC
from usys import platform, version
from esp32 import hall_sensor, raw_temperature
from ubinascii import hexlify


def convert_unique_id() -> str:
    """
    get and converts the unique device id
    :return: mac address as string
    """
    byte_mac = hexlify(unique_id(), ':')
    string_mac = str(byte_mac, 'utf-8')

    return string_mac


def convert_rtc() -> tuple:
    """
    get current device time/date
    :return: date and time string values as tuple
    """
    rtc = RTC()
    tuple_rtc = rtc.datetime()
    string_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
    string_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'

    return string_date, string_time


if __name__ == '__main__':
    print('\n[INFO] Board information')
    print(f"{'Device ID' : < 15} : {convert_unique_id()}")
    print(f"{'Frequency' : < 15} : {freq()} Hz")
    str_date, str_time = convert_rtc()
    print(f"{'Date/Time' : < 15} : {str_date} {str_time}")
    print(f"{'Version' : <15} : {version}")
    print(f"{'Platform' : <15} : {platform}")
    print(f"{'Hall' : < 15} : {hall_sensor()}")
    print(f"{'MCU' : < 15} : {raw_temperature()} F\n")
