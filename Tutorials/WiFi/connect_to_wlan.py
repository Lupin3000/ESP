from network import WLAN, STA_IF


# declare constant
NL = '\n'

# declare variables
ssid = ''
password = ''

# create station
sta = WLAN(STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    print(f'Connect to {ssid} ... please wait')

# get network configuration
config = sta.ifconfig()
print(f'IP: {config[0]}{NL}Subnet mask: {config[1]}{NL}Gateway: {config[2]}{NL}DNS: {config[3]}')
