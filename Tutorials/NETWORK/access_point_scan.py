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


def list_access_points(access_points: tuple) -> None:
    """
    Print out all access point form list
    :param access_points: tuple of access points
    :return: None
    """
    nl = '\n'
    counter = 0
    ap_count = len(access_points)

    # output access points
    print(f"{nl}{'Name' : <25}{'BSSID' : ^20}{'Channel' : ^10}{'RSSI' : ^10}{'Authentication' : ^20}")
    print('-' * 82)

    for item in access_points:
        counter += 1
        byte_name = item[0]
        str_name = str(byte_name, 'utf-8')
        byte_mac = hexlify(item[1], ':')
        str_mac = str(byte_mac, 'utf-8')
        int_strength = f'{item[3]} dBm'

        if counter < ap_count:
            print(f"{str_name : <25}{str_mac : ^20}{item[2] : ^10}{int_strength : ^10}{conv_mode(item[4]) : ^20}")
        else:
            print(f"{str_name : <25}{str_mac : ^20}{item[2] : ^10}{int_strength : ^10}{conv_mode(item[4]) : ^20}{nl}")


if __name__ == '__main__':
    sta = None
    ap = 0

    try:
        sta = WLAN(STA_IF)
    except Exception as err:
        print(f'[ERROR] WLAN initialization failed: {err}')

    if sta:
        sta.active(True)
        print('[INFO] Scan for access points')
        ap = sta.scan()

        if len(ap) > 0:
            list_access_points(ap)
        else:
            print('[INFO] No access points found')
