from micropython import const
from network import WLAN, STA_IF
from utime import sleep_ms


WLAN_SSID = 'YOUR WLAN SSID'
WLAN_PASSWORD = 'YOUR WLAN PASSWORD'
WLAN_CONNECT_DELAY = const(500)
WLAN_MAX_RETRIES = const(15)


def connect_to_ap() -> bool:
    """
    connect as station to access point
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
            return False

    return True


if connect_to_ap():
    print(f'[INFO] connection to {WLAN_SSID} established')
else:
    print(f'[ERROR] connection to {WLAN_SSID} failed')
