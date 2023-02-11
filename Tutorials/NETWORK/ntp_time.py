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
    estimated = localtime()
    estimated_date = f'{estimated[2]:02d}.{estimated[1]:02d}.{estimated[0]}'
    estimated_time = f'{estimated[3]:02d}:{estimated[4]:02d}'

    settime()

    actual = localtime(time() + UTC_OFFSET)
    actual_date = f'{actual[2]:02d}.{actual[1]:02d}.{actual[0]}'
    actual_time = f'{actual[3]:02d}:{actual[4]:02d}'

    print(f'[INFO] Non-synced time: {estimated_time} {estimated_date}')
    print(f'[INFO] Synced time: {actual_time} {actual_date}')
