import network


# create access point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP-Network', channel=6, hidden=False)

while not ap.active():
    print('Create Access Point ... please wait')

# show configuration
config = ap.ifconfig()
new_line = '\n'
print(f'IP: {config[0]}{new_line}Subnet mask: {config[1]}{new_line}Gateway: {config[2]}{new_line}DNS: {config[3]}')
