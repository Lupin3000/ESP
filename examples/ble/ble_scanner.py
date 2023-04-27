from micropython import const
from ubluetooth import BLE
from ubinascii import hexlify
from utime import sleep


_SCAN_DURATION_MS = const(7000)
_SCAN_INTERVAL_US = const(1000000)
_SCAN_WINDOW_US = const(50000)

_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_COMPLETE = const(6)


def mac_to_str(mac_address: bytes) -> str:
    """
    convert byte value of mac address to string value
    :param mac_address: bytes value of mac address
    :return: str of mac address
    """
    return hexlify(mac_address, ':').decode().upper()


def irq_scan(event, data) -> None:
    """
    set global variables for specific ble _IRQ events
    :param event: constants of the event handler codes
    :param data: event-specific tuple of values
    :return: None
    """
    global process
    global ble_adv

    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        ble_adv[mac_to_str(addr)] = [rssi, bytes(adv_data)]
    elif event == _IRQ_SCAN_COMPLETE:
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
        ble.irq(irq_scan)

        process = True

        print('[INFO] Scanning for ble devices...')
        ble.gap_scan(_SCAN_DURATION_MS, _SCAN_INTERVAL_US, _SCAN_WINDOW_US, False)

        while process:
            sleep(1)

        count = len(ble_adv)
        if count > 0:
            print(f'[INFO] {count} ble devices found')
            for mac in ble_adv:
                print(f'[INFO] {mac} (rssi {ble_adv[mac][0]} dBm)')
        else:
            print('[INFO] No ble devices found')

        ble.active(False)
