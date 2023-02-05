from micropython import const
from network import WLAN, STA_IF
from utime import sleep_ms
from usocket import getaddrinfo


# define constants
WLAN_SSID = const('ORBI82')
WLAN_PASSWORD = const('boldbug903')
WLAN_CONNECT_DELAY = const(500)
TARGET = const('root-me.org')


def connect_to_wlan() -> bool:
    max_retries = 10
    attempt = 0

    sta = WLAN(STA_IF)
    sta.active(True)
    sta.connect(WLAN_SSID, WLAN_PASSWORD)

    while not sta.isconnected():
        sleep_ms(WLAN_CONNECT_DELAY)
        attempt += 1
        print(f'[INFO] {attempt}. connect to {WLAN_SSID} ... please wait')

        if attempt >= max_retries:
            print(f'[ERROR] Connection to {SSID} failed')
            return False

    return True


if connect_to_wlan():
    try:
        target = getaddrinfo(TARGET, 23)
        print(f'[INFO] IP of {TARGET} is {target[0][-1][0]}')
    except IOError as err:
        print(f'[ERROR] {err}')
