from micropython import const
from ubluetooth import BLE, UUID, FLAG_WRITE, FLAG_READ, FLAG_NOTIFY
from utime import sleep


# define constants
_DELAY_SEC = const(50)

_ADV_TYP_NAME = const(9)
_BROADCASTING_INTERVAL_US = const(100)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)
_IRQ_GATTS_READ_REQUEST = const(4)

_FLAG_READ = const(0x0002)
_FLAG_WRITE_NO_RESPONSE = const(0x0004)
_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_UART_UUID = UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_TX = (
    UUID('6E400003-B5A3-F393-E0A9-E50E24DCCA9E'),
    _FLAG_READ | _FLAG_NOTIFY,
)
_UART_RX = (
    UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"),
    _FLAG_WRITE | _FLAG_WRITE_NO_RESPONSE,
)
_UART_SERVICE = (
    _UART_UUID,
    (_UART_TX, _UART_RX),
)


def ble_irq(event: int, data: tuple) -> None:
    """
    BLE irq event handler
    :param event: number of the event handler codes
    :param data: event-specific tuple of values (not used)
    :return: None
    """
    global my_ble
    global rx
    global is_central_connected

    _ = data

    if event == _IRQ_CENTRAL_CONNECT:
        print('[INFO] A central has is_central_connected to this peripheral')
        is_central_connected = True
    elif event == _IRQ_CENTRAL_DISCONNECT:
        print('[INFO] A central has disconnected from this peripheral')
        is_central_connected = False
    elif event == _IRQ_GATTS_WRITE:
        buffer = my_ble.gatts_read(rx)
        print(f"[INFO] A central has written this: {buffer.decode('UTF-8').strip()}")


def ble_notify(data: str) -> None:
    """
    Notify the connected central that value has changed, and issue a reading of current value of this peripheral
    :param data: short string of value(s)
    :return: None
    """
    global my_ble
    global tx

    print(f'[INFO] Peripheral send notification: {data} to central')
    message = data.strip()
    my_ble.gatts_notify(0, tx, message + '\n')


def ble_advertise(name: str = 'ESP32') -> None:
    """
    Start broadcasting in interval with device name
    :param name: device name as string
    :return: None
    """
    global my_ble

    dev_name = bytes(name, 'UTF-8')

    # 0x02 - General discoverable mode
    # 0x01 - AD Type = 0x01
    # 0x02 - value = 0x02
    adv_data = bytearray('\x02\x01\x02') + bytearray((len(dev_name) + 1, _ADV_TYP_NAME)) + dev_name

    print(f'[INFO] Start BLE advertise as {name}...')
    my_ble.gap_advertise(_BROADCASTING_INTERVAL_US, adv_data, connectable=True)


def ble_services() -> None:
    """
    Configure specific services
    :param bluetooth: bluetooth object
    :return: None
    """
    global my_ble
    global tx
    global rx

    services = (_UART_SERVICE,)
    ((tx, rx,), ) = my_ble.gatts_register_services(services)


if __name__ == '__main__':
    device_name = 'SimpleBLE'
    my_ble = None
    tx = None
    rx = None
    is_central_connected = False

    try:
        my_ble = BLE()
    except Exception as err:
        print(f'[ERROR] Bluetooth initialization failed: {err}')

    if my_ble:
        print(f'[INFO] Start BLE services and irq for {device_name}')
        my_ble.active(True)
        ble_services()
        my_ble.irq(ble_irq)

        while True:
            ble_advertise(device_name)

            sleep(_DELAY_SEC / 2)
            if is_central_connected:
                ble_notify('Hi from ESP32...')

            sleep(_DELAY_SEC)
