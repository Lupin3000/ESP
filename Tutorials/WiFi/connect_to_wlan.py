import network


# define variables
ssid = ''
password = ''

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    print(f'Connect to {ssid} ... please wait')

config = sta.ifconfig()
new_line = '\n'
print(f'IP: {config[0]}{new_line}Subnet mask: {config[1]}{new_line}Gateway: {config[2]}{new_line}DNS: {config[3]}')
