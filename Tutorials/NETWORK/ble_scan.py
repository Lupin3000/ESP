from micropython import const
from ubluetooth import BLE
from ubinascii import hexlify
from utime import sleep


# define constants
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)


def mac2str(mac_address: bytes) -> str:
    """
    Convert mac address
    :param mac_address: bytes of mac address
    :return: str
    """
    return hexlify(mac_address, ':').decode().upper()


def ble_irq(event, data) -> None:
    """
    event handler for BLE IRQ
    :param event: constant of event handler codes
    :param data: event-specific tuple of values
    :return: None
    """
    global process

    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        ble_adv[mac2str(addr)] = [rssi, bytes(adv_data)]
    elif event == _IRQ_SCAN_DONE:
        process = False


# define variables
process = False
ble_adv = {}

try:
    ble = BLE()

    ble.active(True)
    ble.irq(ble_irq)

    process = True
    ble.gap_scan(7000, 1000000, 50000, False)
    print('[INFO] Scanning BLE...')

    while process:
        sleep(1)

    count = len(ble_adv)

    if count > 0:
        print(f'[INFO] {count} BLE devices found')

        for mac in ble_adv:
            print(f'[INFO] {mac} (rssi {ble_adv[mac][0]} dBm)')

    else:
        print('[INFO] No BLE devices found')

except Exception as err:
    print(f'[ERROR] bluetooth initialization failed: {err}')
