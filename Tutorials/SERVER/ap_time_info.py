from micropython import const
from network import WLAN, AP_IF, AUTH_OPEN
from usocket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from machine import RTC


# define constants
ESSID = const('ESP-Network')
CHANNEL = const(11)


def create_ap() -> bool:
    """
    Create Access Point
    :return: bool
    """
    ap = WLAN(AP_IF)
    ap.active(True)

    try:
        ap.config(essid=ESSID, channel=CHANNEL, authmode=AUTH_OPEN, hidden=False)
    except Exception as err:
        print(f'[ERROR] Create access point {ESSID} failed')

    if ap.active():
        config = ap.ifconfig()
        print(f'[INFO] Create access point {ESSID} successful')
        print(f'[INFO] IP: {config[0]}')
        print(f'[INFO] Subnet mask: {config[1]}')
        print(f'[INFO] Gateway: {config[2]}')
        print(f'[INFO] DNS: {config[3]}')
        return True
    else:
        return False


def get_time() -> str:
    """
    Return current date/time
    :return: string
    """
    rtc = RTC()
    tuple_rtc = rtc.datetime()
    str_date = f'{tuple_rtc[0]}-{tuple_rtc[1]:02d}-{tuple_rtc[2]:02d}'
    str_time = f'{tuple_rtc[4]:02d}:{tuple_rtc[5]:02d}:{tuple_rtc[6]:02d}'
    org_time = f'Local device date/time: {str_date} {str_time}'

    return org_time


def create_webserver() -> None:
    """
    Start webserver via socket
    :return: None
    """
    print('[INFO] Start webserver on port 80')
    lis = socket(AF_INET, SOCK_STREAM)
    lis.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    lis.bind(('', 80))
    lis.listen(5)

    while True:
        try:
            conn, addr = lis.accept()
            print(f'[INFO] Got a connection from {str(addr)}')

            # request
            request = conn.recv(1024).decode('utf-8')
            print(request)

            # response
            response = get_time()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as err:
            lis.close()


if create_ap():
    create_webserver()
