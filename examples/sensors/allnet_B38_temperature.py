from micropython import const
from machine import Pin, I2C
from ubluetooth import BLE, UUID
from ustruct import pack
from ble_advertising import advertising_payload
from utime import sleep_ms


I2C_SDA_PIN = const(21)
I2C_SCL_PIN = const(22)
I2C_ADDRESS = const(79)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_INDICATE_DONE = const(20)

_FLAG_READ = const(0x0002)
_FLAG_NOTIFY = const(0x0010)
_FLAG_INDICATE = const(0x0020)

_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)

_ENV_SENSE_UUID = UUID(0x181A)
_TEMP_CHAR = (
    UUID(0x2A6E),
    _FLAG_READ | _FLAG_NOTIFY | _FLAG_INDICATE,
)
_ENV_SENSE_SERVICE = (
    _ENV_SENSE_UUID,
    (_TEMP_CHAR,),
)


class TemperatureBLE:
    def __init__(self, ble, name="mpy-temp"):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)

        ((self._handle,),) = self._ble.gatts_register_services((_ENV_SENSE_SERVICE,))
        self._connections = set()

        self._payload = advertising_payload(name=name,
                                            services=[_ENV_SENSE_UUID],
                                            appearance=_ADV_APPEARANCE_GENERIC_THERMOMETER)
        self._advertise()

    def _irq(self, event, data):
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            self._advertise()
        elif event == _IRQ_GATTS_INDICATE_DONE:
            conn_handle, value_handle, status = data

    def set_temperature(self, temp_deg_c, notify=False, indicate=False):
        self._ble.gatts_write(self._handle, pack("<h", int(temp_deg_c * 100)))

        if notify or indicate:
            for conn_handle in self._connections:
                if notify:
                    self._ble.gatts_notify(conn_handle, self._handle)
                if indicate:
                    self._ble.gatts_indicate(conn_handle, self._handle)

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)


class TemperatureSensor:
    def __init__(self, sda: int, scl: int, address: int):
        """
        temperature sensor constructor
        :param sda: number for GPIO SDA pin
        :param scl: number for GPIO SCL pin
        :param address: number for sensor address
        """
        self.__sda = int(sda)
        self.__scl = int(scl)
        self.__address = int(address)

        self.__i2c = I2C(0, scl=Pin(self.__scl), sda=Pin(self.__sda))

    @staticmethod
    def convert_data(value: bytes) -> float:
        """
        convert bytes to float value (degrees Celsius)
        :param value: bytes
        :return: float
        """
        temp_c = (value[0] << 5) | (value[1] >> 3)
        if (temp_c >> 11) == 1:
            temp_c = temp_c - (1 << 13)
        temp_c = temp_c * 0.03125

        return round(temp_c, 2)

    def read_data(self) -> float:
        """
        trigger read from temperature sensor
        :return: float
        """
        data = bytearray(2)
        self.__i2c.readfrom_mem_into(self.__address, 0x00, data)

        return TemperatureSensor.convert_data(data)


if __name__ == '__main__':
    bluetooth = BLE()
    service = TemperatureBLE(ble=bluetooth, name='esp32')
    sensor = TemperatureSensor(sda=I2C_SDA_PIN, scl=I2C_SCL_PIN, address=I2C_ADDRESS)

    i = 0

    while True:
        i = (i + 1) % 10
        t = sensor.read_data()

        service.set_temperature(t, notify=i == 0, indicate=False)

        sleep_ms(1000)
