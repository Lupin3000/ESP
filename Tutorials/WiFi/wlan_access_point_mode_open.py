from micropython import const
from network import WLAN, AP_IF


# define constants
WLAN_ESSID = const('OPEN-NET')
WLAN_CHANNEL = const(6)

if __name__ == '__main__':
    # create WLAN object (access point mode)
    ap = WLAN(AP_IF)
    ap.active(True)
    ap.config(essid=WLAN_ESSID, channel=WLAN_CHANNEL, hidden=False)

    while not ap.active():
        print('[INFO] Create Access Point ... please wait')

    # get WLAN information
    config = ap.ifconfig()

    # show WLAN information
    print('[INFO] WLAN created')
    print(f"{'ESSID' : <15}{WLAN_ESSID}")
    print(f"{'Channel' : <15}{WLAN_CHANNEL}")
    print(f"{'IP' : <15}{config[0]}")
    print(f"{'Subnet mask' :<15}{config[1]}")
    print(f"{'Gateway' :<15}{config[2]}")
    print(f"{'DNS' :<15}{config[3]}")
