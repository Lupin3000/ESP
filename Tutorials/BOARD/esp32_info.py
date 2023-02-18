from machine import RTC, unique_id, freq
from ubinascii import hexlify
from esp32 import hall_sensor, raw_temperature
from usys import version, platform


def show_date_time() -> None:
    """
    Print out current device date/time
    :return: None
    """
    rtc = None

    try:
        rtc = RTC()
    except Exception as err:
        print(f'[ERROR] RTC initialization failed: {err}')

    if rtc:
        tuple_rtc = rtc.datetime()
        str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
        str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'

        print(f"{'Date/Time' : < 15}{str_date} {str_time}")


def show_device_mac() -> None:
    """
    Print out device mac address
    :return: None
    """
    byte_mac = hexlify(unique_id(), ':')
    str_mac = str(byte_mac, 'utf-8')

    print(f"{'ID' : < 15}{str_mac}")


def show_hall() -> None:
    """
    Print out device hall sensor value
    :return: None
    """
    print(f"{'Hall' : < 15}{hall_sensor()}")


def show_cpu() -> None:
    """
    Print out device CPU frequency
    :return: None
    """
    print(f"{'CPU' : < 15}{freq()} Hz")


def show_mcu_temp() -> None:
    """
    Print out device MCU temperature
    :return: None
    """
    print(f"{'MCU' : < 15}{raw_temperature()} Fahrenheit")


def show_micropython_info() -> None:
    """
    Print out MicroPython information
    :return: None
    """
    print(f"{'Version' : <15}{version}")
    print(f"{'Platform' : <15}{platform}")


if __name__ == '__main__':
    show_date_time()
    show_device_mac()
    show_hall()
    show_cpu()
    show_mcu_temp()
    show_micropython_info()
