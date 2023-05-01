from usocket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


if __name__ == '__main__':
    html = """<html>
                <head>
                    <title>ESP Webserver</title>
                </head>
                <body>
                    <h1>Welcome to your ESP</h1>
                    <p>Example of an very simple webserver on ESP.</p>
                </body>
              </html>"""

    listener = socket(AF_INET, SOCK_STREAM)
    listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listener.bind(('', 80))
    listener.listen(5)

    while True:
        try:
            conn, addr = listener.accept()

            print(f'[INFO] connection from {str(addr)}')
            request = conn.recv(1024)

            response = html
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as err:
            print(f'[ERROR] following problem occurred: {err}')
            listener.close()
