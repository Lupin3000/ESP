from micropython import const
from ubluetooth import BLE
from ubinascii import hexlify
from utime import sleep


# define constants
DURATION_MS = const(7000)
INTERVAL_US = const(1000000)
WINDOW_US = const(50000)
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)


def mac_to_str(mac_address: bytes) -> str:
    """
    Convert mac address
    :param mac_address: bytes of mac address
    :return: str
    """
    return hexlify(mac_address, ':').decode().upper()


def ble_irq(event, data) -> None:
    """
    event handler for BLE IRQ
    :param event: constants of the event handler codes
    :param data: event-specific tuple of values
    :return: None
    """
    global process

    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        ble_adv[mac_to_str(addr)] = [rssi, bytes(adv_data)]
    elif event == _IRQ_SCAN_DONE:
        process = False


if __name__ == '__main__':
    process = False
    ble_adv = {}
    ble = None

    try:
        ble = BLE()
    except Exception as err:
        print(f'[ERROR] bluetooth initialization failed: {err}')

    if ble:
        ble.active(True)
        ble.irq(ble_irq)
        process = True

        ble.gap_scan(DURATION_MS, INTERVAL_US, WINDOW_US, False)
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

        ble.active(False)
