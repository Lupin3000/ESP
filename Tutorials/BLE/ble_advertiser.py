from micropython import const
from ubluetooth import BLE


# define constants
_ADV_TYP_NAME = const(9)
_BROADCASTING_INTERVAL_US = const(100)


def ble_advertise(ble_obj, name: str = 'BLE-ESP32') -> None:
    """
    Start broadcasting in interval with device name
    :param ble_obj: bluetooth object
    :param name: device name as string
    :return: None
    """
    dev_name = bytes(name, 'UTF-8')

    # 0x02 - General discoverable mode
    # 0x01 - AD Type = 0x01
    # 0x02 - value = 0x02
    adv_data = bytearray('\x02\x01\x02') + bytearray((len(dev_name) + 1, _ADV_TYP_NAME)) + dev_name

    print(f'[INFO] Start BLE advertise as {name}...')
    ble_obj.gap_advertise(_BROADCASTING_INTERVAL_US, adv_data, connectable=False)


if __name__ == '__main__':
    ble = None

    try:
        ble = BLE()
    except Exception as err:
        print(f'[ERROR] bluetooth initialization failed: {err}')

    if ble:
        ble.active(True)
        ble_advertise(ble)
