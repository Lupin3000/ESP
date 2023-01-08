from network import WLAN, AP_IF


# declare constant
NL = '\n'

# create access point
ap = WLAN(AP_IF)
ap.active(True)
ap.config(essid='ESP-Network', channel=6, hidden=False)

while not ap.active():
    print('Create Access Point ... please wait')

# show configuration
config = ap.ifconfig()
print(f'IP: {config[0]}{NL}Subnet mask: {config[1]}{NL}Gateway: {config[2]}{NL}DNS: {config[3]}')
