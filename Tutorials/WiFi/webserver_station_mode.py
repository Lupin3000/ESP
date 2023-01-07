import network
import usocket as socket


# define variables
ssid = ''
password = ''

# start connection
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    print(f'Connect to {ssid} ... please wait')

config = sta.ifconfig()
new_line = '\n'
print(f'IP: {config[0]}{new_line}Subnet mask: {config[1]}{new_line}Gateway: {config[2]}{new_line}DNS: {config[3]}')

# define webpage
html = """<html>
            <head>
                <title>ESP</title>
            </head>
            <body>
                <h1>Welcome to ESP</h1>
                <p>simple webserver on ESP</p>
            </body>
          </html>"""

# start listener on port 80
s_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_con.bind(('', 80))
s_con.listen(5)

while True:
  conn, addr = s_con.accept()
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
