from ubluetooth import BLE, UUID, FLAG_WRITE, FLAG_NOTIFY


class SimpleBluetoothLight:

    def __init__(self, name: str):
        """
        class initializer
        :param name: name of ble device
        """
        print('[INFO] Start ble device')

        self.rx = None
        self.tx = None
        self.connected = False
        self.device_name = str(name)
        self.device_uuid = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'

        self._ble = BLE()
        self._ble.active(True)
        self._ble.irq(self._irq)

        self._register()
        self._advertiser()

    def _irq(self, event: int, data: tuple) -> None:
        """
        ble irq event handler
        :param event: number of the event handler codes
        :param data: event-specific tuple of values (not used)
        :return: None
        """
        _ = data

        if event == 1:
            print('[INFO] A central has is_central_connected to this peripheral')
            self.connected = True
        elif event == 2:
            print('[INFO] A central has disconnected from this peripheral')
            self.connected = False
        elif event == 3:
            buffer = self._ble.gatts_read(self.rx)
            print(f"[INFO] message received: {buffer.decode('UTF-8').strip()}")

    def _register(self) -> None:
        """
        ble device register
        :return: None
        """
        nus_uuid = self.device_uuid
        rx_uuid = self.device_uuid
        tx_uuid = self.device_uuid

        ble_nus = UUID(nus_uuid)
        ble_rx = (UUID(rx_uuid), FLAG_WRITE)
        ble_tx = (UUID(tx_uuid), FLAG_NOTIFY)
        ble_uart = (ble_nus, (ble_tx, ble_rx,))
        services = (ble_uart,)

        ((self.tx, self.rx,),) = self._ble.gatts_register_services(services)

        print(f'[INFO] UUID: {self.device_uuid} - TX: {self.tx} - RX: {self.rx}')

    def _advertiser(self) -> None:
        """
        ble device advertiser
        :return: None
        """
        dev_name = bytes(self.device_name, 'UTF-8')
        adv_data = bytearray('\x02\x01\x02') + bytearray((len(dev_name) + 1, 0x09)) + dev_name
        self._ble.gap_advertise(100, adv_data)

        print(f'[INFO] ble device {self.device_name} started')

    def send_msg(self, data: str) -> None:
        """
        ble send message
        :param data: message string
        :return: None
        """
        msg = data + '\n'
        self._ble.gatts_notify(0, self.tx, msg)
