from micropython import const
from network import WLAN, STA_IF
from utime import sleep_ms
from time import time, localtime
from ntptime import settime


# define constant
WLAN_SSID = const('YOUR WLAN SSID')
WLAN_PASSWORD = const('YOUR WLAN PASSWORD')
WLAN_CONNECT_DELAY = const(500)
WLAN_MAX_RETRIES = const(10)
UTC_OFFSET = const(3600)


def connect_to_wlan() -> bool:
    """
    Connect to WLAN access point as station
    :return: bool
    """
    attempt = 0

    sta = WLAN(STA_IF)
    sta.active(True)
    sta.connect(WLAN_SSID, WLAN_PASSWORD)

    while not sta.isconnected():
        sleep_ms(WLAN_CONNECT_DELAY)
        attempt += 1
        print(f'[INFO] {attempt}. connect to {WLAN_SSID} ... please wait')

        if attempt >= WLAN_MAX_RETRIES:
            print(f'[ERROR] Connection to {WLAN_SSID} failed')
            return False

    return True


if connect_to_wlan():
    estimated_time = localtime()
    conv_estimated_date = f'{estimated_time[2]:02d}.{estimated_time[1]:02d}.{estimated_time[0]}'
    conv_estimated_time = f'{estimated_time[3]:02d}:{estimated_time[4]:02d}'

    settime()

    actual_time = localtime(time() + UTC_OFFSET)
    conv_actual_date = f'{actual_time[2]:02d}.{actual_time[1]:02d}.{actual_time[0]}'
    conv_actual_time = f'{actual_time[3]:02d}:{actual_time[4]:02d}'

    print(f'[INFO] Non-synced time: {conv_estimated_time} {conv_estimated_date}')
    print(f'[INFO] Synced time: {conv_actual_time} {conv_actual_date}')
