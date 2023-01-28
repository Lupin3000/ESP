from micropython import const
from network import WLAN, AP_IF


# define constants
WLAN_ESSID = const('ESP-NETWORK')
WLAN_PASSWORD = const('12345678')
WLAN_CHANNEL = const(11)

# create WLAN object (access point mode)
ap = WLAN(AP_IF)
ap.config(essid=WLAN_ESSID,  password=WLAN_PASSWORD)
ap.config(channel=WLAN_CHANNEL)
ap.config(authmode=3)
ap.active(True)

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
