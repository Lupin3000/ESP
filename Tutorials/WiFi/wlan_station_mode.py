from micropython import const
from network import WLAN, STA_IF


# define constant
WLAN_SSID = const('YOUR WLAN SSID')
WLAN_PASSWORD = const('YOUR WLAN PASSWORD')

# create WLAN object (station mode)
sta = WLAN(STA_IF)
sta.active(True)
sta.connect(WLAN_SSID, WLAN_PASSWORD)

while not sta.isconnected():
    print(f'[INFO] Connect to {WLAN_SSID} ... please wait')

# get WLAN information
config = sta.ifconfig()

# show WLAN information
print('[INFO] connected to WLAN')
print(f"{'SSID' : <15}{WLAN_SSID}")
print(f"{'IP' : <15}{config[0]}")
print(f"{'Subnet mask' :<15}{config[1]}")
print(f"{'Gateway' :<15}{config[2]}")
print(f"{'DNS' :<15}{config[3]}")
