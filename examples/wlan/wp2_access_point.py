from micropython import const
from network import WLAN, AP_IF


WLAN_ESSID = const('ESP-NETWORK')
WLAN_PASSWORD = const('12345678')
WLAN_CHANNEL = const(11)

if __name__ == '__main__':
    if len(WLAN_PASSWORD) >= 8:
        ap = WLAN(AP_IF)
        ap.config(essid=WLAN_ESSID, password=WLAN_PASSWORD)
        ap.config(channel=WLAN_CHANNEL)
        ap.config(authmode=3)
        ap.active(True)

        while not ap.active():
            print('[INFO] Create access point')

        config = ap.ifconfig()

        print('[INFO] WPA2 access point created')
        print(f"{'Channel' : <15}{WLAN_CHANNEL}")
        print(f"{'IP' : <15}{config[0]}")
        print(f"{'Subnet mask' :<15}{config[1]}")
        print(f"{'Gateway' :<15}{config[2]}")
