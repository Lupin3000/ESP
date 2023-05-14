from micropython import const
from network import WLAN, STA_IF


AP_SSID = 'YOUR WLAN NAME'
AP_PASSWORD = 'YOUR WLAN PASSWORD'


if __name__ == '__main__':
    sta = WLAN(STA_IF)
    sta.active(True)
    sta.connect(AP_SSID, AP_PASSWORD)

    while not sta.isconnected():
        print(f'[INFO] Connection to {AP_SSID}')

    config = sta.ifconfig()

    print(f'[INFO] connected to WLAN {AP_SSID}')
    print(f"{'IP' : <15}{config[0]}")
    print(f"{'Subnet mask' :<15}{config[1]}")
    print(f"{'Gateway' :<15}{config[2]}")
    print(f"{'DNS' :<15}{config[3]}")
