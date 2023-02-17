from micropython import const
from machine import PWM, Pin
from network import WLAN, STA_IF
from utime import sleep, sleep_ms
from usocket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


# declare constants
SSID = const('YOUR SSID')
PWD = const('YOUR PASSWORD')
LED_GPIO = const(23)
DELAY = const(0.005)
LED_FREQ = const(5000)
NL = const('\n')


def fade_led_on() -> None:
    """
    Fade LED on
    :return: None
    """
    global led_status

    if led_status == 0:
        led_status = 1
        # LED Fade ON
        print('[INFO] LED Fade ON')
        for dc in range(0, 1023):
            led.duty(dc)
            sleep(DELAY)


def fade_led_off() -> None:
    """
    Fade LED off
    :return: None
    """
    global led_status

    if led_status == 1:
        led_status = 0
        # LED Fade OFF
        print('[INFO] LED Fade OFF')
        for dc in range(1023, 0, -1):
            led.duty(dc)
            sleep(DELAY)


def connect_to_ap(max_retries: int = 10) -> bool:
    """
    Create WlAN station and connect to Access Point
    :param max_retries: int
    :return: bool
    """
    sta = WLAN(STA_IF)
    sta.active(True)
    sta.connect(SSID, PWD)

    attempt = 0
    while not sta.isconnected():
        sleep_ms(500)
        attempt += 1
        print(f'[INFO] {attempt} Connect to {SSID} ... please wait')

        if attempt >= max_retries:
            print(f'[ERROR] Connection to {SSID} failed')
            return False

    # get network configuration
    config = sta.ifconfig()
    print(f'[INFO] Connection to {SSID} established')
    print(f'[INFO] IP: {config[0]}')
    print(f'[INFO] Subnet mask: {config[1]}')
    print(f'[INFO] Gateway: {config[2]}')
    print(f'[INFO] DNS: {config[3]}')

    return True


def create_webserver() -> None:
    """
    Create webserver on port 80
    :return: None
    """
    print('[INFO] Start webserver on port 80')
    s_lis = socket(AF_INET, SOCK_STREAM)
    s_lis.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s_lis.bind(('', 80))
    s_lis.listen(5)

    while True:
        conn, addr = s_lis.accept()
        print(f'[INFO] Got a connection from {str(addr)}')

        # request
        request = conn.recv(1024).decode('utf-8')
        request_split = request.split(' ')
        print(f'[INFO] HTTP Method {request_split[0]}')
        print(f'[INFO] HTTP Request {request_split[1]}')

        if '?' in request_split[1]:
            parameter = request_split[1].split('?')
            parameter = parameter[1].split('=')[1]
            print(f'[INFO] HTTP Parameter {parameter}')

            # turn led on/off
            if parameter == 'on':
                fade_led_on()
            else:
                fade_led_off()

        # prepare response
        try:
            header = 'HTTP/1.1 200 OK\n'
            file = open('index.html', 'rb')
            response = file.read()
            file.close()
        except Exception as err:
            header = 'HTTP/1.1 404 Not Found\n'
            response = 'Error 404'

        # send response
        conn.send(header.encode('utf-8'))
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()


# create PWM object with GPIO pin
led = PWM(Pin(LED_GPIO))
led.freq(LED_FREQ)

# define variable
led_status = 1

if connect_to_ap():
    create_webserver()
