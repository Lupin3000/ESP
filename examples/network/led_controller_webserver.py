from micropython import const
from machine import Pin
from usocket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


LED_ONE_PIN = const(23)
LED_TWO_PIN = const(22)


class LED:
    def __init__(self, pin: int):
        """
        led constructor
        :param pin: integer value for GPIO pin
        """
        self._led = Pin(pin, Pin.OUT, value=0)

    def led_on(self) -> None:
        """
        turn led on
        :return: None
        """
        self._led.value(1)

    def led_off(self) -> None:
        """
        turn led off
        :return: None
        """
        self._led.value(0)


class Server:
    def __init__(self, led: tuple):
        """
        server constructor
        :param led: tuple of leds
        """
        self._led = tuple(led)

        self._listener = socket(AF_INET, SOCK_STREAM)
        self._listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._listener.bind(('', 80))
        self._listener.listen()

    def listen(self) -> None:
        """
        server listener
        :return: None
        """
        conn, addr = self._listener.accept()

        request = conn.recv(1024).decode('utf-8')
        request_split = request.split(' ')

        if '?' in request_split[1]:
            parameter = request_split[1].split('?')
            parameter = parameter[1].split('=')

            if parameter[1] == 'on':
                self._led[int(parameter[0])].led_on()
            else:
                self._led[int(parameter[0])].led_off()

        try:
            header = 'HTTP/1.1 200 OK\n'
            file = open('index.html', 'rb')
            response = file.read()
            file.close()
        except Exception as err:
            header = 'HTTP/1.1 404 Not Found\n'
            response = 'Error 404'

        conn.send(header.encode('utf-8'))
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()


if __name__ == '__main__':
    led_one = LED(pin=LED_ONE_PIN)
    led_two = LED(pin=LED_TWO_PIN)

    leds = (led_one, led_two)

    server = Server(led=leds)

    while True:
        server.listen()
