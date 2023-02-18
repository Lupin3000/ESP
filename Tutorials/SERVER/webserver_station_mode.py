from micropython import const
from network import WLAN, STA_IF
from usocket import socket, AF_INET, SOCK_STREAM


# declare constant
SSID = const('YOUR WLAN SSID')
PASSWORD = const('YOUR WLAN PASSWORD')

# html template
html = """<html>
            <head>
                <title>ESP Webserver</title>
            </head>
            <body>
                <h1>Welcome to your ESP</h1>
                <p>Example of an very simple webserver on ESP.</p>
            </body>
          </html>"""

if __name__ == '__main__':
    # create station and start connection
    sta = WLAN(STA_IF)
    sta.active(True)
    sta.connect(SSID, PASSWORD)

    while not sta.isconnected():
        print(f'Connect to {SSID} ... please wait')

    # get network configuration
    config = sta.ifconfig()
    nl = '\n'
    print(f'IP: {config[0]}{nl}Subnet mask: {config[1]}{nl}Gateway: {config[2]}{nl}DNS: {config[3]}')

    # start socket listener on port 80
    s_lis = socket(AF_INET, SOCK_STREAM)
    s_lis.bind(('', 80))
    s_lis.listen(5)

    while True:
        conn, addr = s_lis.accept()
        print(f'Got a connection from {str(addr)}')

        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)

        response = html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
