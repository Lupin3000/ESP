from network import WLAN, STA_IF
from ubinascii import hexlify


def conv_mode(number: int) -> str:
    """
    convert WLAN authentication mode
    :param number: int of authentication mode
    :return: str of authentication mode
    """
    if number == 0:
        return 'open'
    elif number == 1:
        return 'WEP'
    elif number == 2:
        return 'WPA-PSK'
    elif number == 3:
        return 'WPA2-PSK'
    elif number == 4:
        return 'WPA/WPA2-PSK'
    else:
        return 'unknown'


# declare constant
NL = '\n'

# declare variable
count = 0

# create station
sta = WLAN(STA_IF)
sta.active(True)

# scan access points
ap = sta.scan()
ap_count = len(ap)

# output access points
print(f"{NL}{'Name' : <25}{'BSSID' : ^20}{'Channel' : ^10}{'RSSI' : ^10}{'Authentication' : ^20}")
print('-' * 82)

for item in ap:
    count += 1
    byte_name = item[0]
    str_name = str(byte_name, 'utf-8')
    byte_mac = hexlify(item[1], ':')
    str_mac = str(byte_mac, 'utf-8')
    int_strength = f'{item[3]} dBm'

    if count < ap_count:
        print(f"{str_name : <25}{str_mac : ^20}{item[2] : ^10}{int_strength : ^10}{conv_mode(item[4]) : ^20}")
    else:
        print(f"{str_name : <25}{str_mac : ^20}{item[2] : ^10}{int_strength : ^10}{conv_mode(item[4]) : ^20}{NL}")
