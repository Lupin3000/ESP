from micropython import const
from network import WLAN, STA_IF
from utime import sleep_ms
import urequests


# define constants
WLAN_SSID = const('YOUR WLAN SSID')
WLAN_PASSWORD = const('YOUR WLAN PASSWORD')
WLAN_CONNECT_DELAY = const(500)
WLAN_MAX_RETRIES = const(10)
TARGET_URL = const('https://pentest-tools.com')


def connect_to_wlan() -> bool:
    """
    Connect to WLAN access point
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
    res = urequests.get(TARGET_URL)
    print(f'[INFO] HTTP Status Code is {res.status_code}')
