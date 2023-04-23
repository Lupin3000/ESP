from micropython import const
from network import WLAN, AP_IF


AP_ESSID = const('OPEN-NET')
AP_CHANNEL = const(6)

if __name__ == '__main__':
    ap = WLAN(AP_IF)
    ap.active(True)
    ap.config(essid=AP_ESSID, channel=AP_CHANNEL, hidden=False)

    while not ap.active():
        print('[INFO] Create access point')

    ap_config = ap.ifconfig()

    print('[INFO] Open access point created')
    print(f"{'Channel' : <15}{AP_CHANNEL}")
    print(f"{'IP' : <15}{ap_config[0]}")
    print(f"{'Subnet mask' :<15}{ap_config[1]}")
    print(f"{'Gateway' :<15}{ap_config[2]}")
