from ubluetooth import BLE, UUID, FLAG_WRITE, FLAG_NOTIFY


def device_irq(event: int, data: tuple) -> None:
    """
    event handler for BLE IRQ
    :param event: number of the event handler codes
    :param data: event-specific tuple of values
    :return: None
    """
    if event == 1:
        print('[INFO] A central has connected to this peripheral')
    elif event == 2:
        print('[INFO] A central has disconnected from this peripheral')
    elif event == 3:
        print(f'[INFO] A central has send data: {data} to this peripheral')


def device_register() -> None:
    """
    BLE device register
    :return: None
    """
    global ble

    dev_id = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
    NUS_UUID = dev_id
    RX_UUID = dev_id
    TX_UUID = dev_id
    BLE_NUS = UUID(NUS_UUID)
    BLE_RX = (UUID(RX_UUID), FLAG_WRITE)
    BLE_TX = (UUID(TX_UUID), FLAG_NOTIFY)
    BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))
    SERVICES = (BLE_UART,)

    ((tx, rx,),) = ble.gatts_register_services(SERVICES)
    print(f'[INFO] TX: {tx} RX: {rx}')


def device_advertiser(name: str) -> None:
    """
    BLE device advertiser
    :param name: name of device
    :return: None
    """
    global ble

    dev_name = bytes(name, 'UTF-8')
    adv_data = bytearray('\x02\x01\x02') + bytearray((len(dev_name) + 1, 0x09)) + dev_name
    ble.gap_advertise(100, adv_data)
    print(f'[INFO] BLE device {name} started')


if __name__ == '__main__':
    ble = BLE()
    ble.active(True)
    ble.irq(device_irq)
    device_register()
    device_advertiser('ESP-DEMO')
