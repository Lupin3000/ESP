from network import WLAN, STA_IF
from usocket import socket, AF_INET, SOCK_STREAM


# declare constant
NL = '\n'

# declare variables
ssid = 'ORBI82'
password = 'boldbug903'
html = """<html>
            <head>
                <title>ESP</title>
            </head>
            <body>
                <h1>Welcome to ESP</h1>
                <p>simple webserver on ESP</p>
            </body>
          </html>"""

# create station and start connection
sta = WLAN(STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    print(f'Connect to {ssid} ... please wait')

# get network configuration
config = sta.ifconfig()
print(f'IP: {config[0]}{NL}Subnet mask: {config[1]}{NL}Gateway: {config[2]}{NL}DNS: {config[3]}')

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
