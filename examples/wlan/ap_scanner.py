from network import WLAN, STA_IF
from ubinascii import hexlify


def conv_wlan_mode(number: int) -> str:
    """
    convert a provided integer to string value
    :param number: integer value for encryption type
    :return: string value for encryption type
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


def list_access_points(access_points: tuple) -> None:
    """
    print scan report into output
    :param access_points: tuple of scan results
    :return: None
    """
    print(f"\n{'Name' : <25}{'BSSID' : ^20}{'Channel' : ^10}{'RSSI' : ^10}{'Authentication' : ^20}")
    print('-' * 82)

    for item in access_points:
        byte_name = item[0]
        str_name = str(byte_name, 'utf-8')
        byte_mac = hexlify(item[1], ':')
        str_mac = str(byte_mac, 'utf-8')
        str_strength = f'{item[3]} dBm'

        print(f"{str_name : <25}{str_mac : ^20}{item[2] : ^10}{str_strength : ^10}{conv_wlan_mode(item[4]) : ^20}")


if __name__ == '__main__':
    station = WLAN(STA_IF)
    station.active(True)

    tuple_access_points = station.scan()

    if len(tuple_access_points) > 0:
        list_access_points(tuple_access_points)
        print("\n")
    else:
        print('[INFO] No access points found')
