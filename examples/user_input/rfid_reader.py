from micropython import const
from machine import Pin, SoftSPI
from mfrc522 import MFRC522
from utime import sleep_ms


MISO_PIN = const(19)
MOSI_PIN = const(23)
SCK_PIN = const(18)
RST_PIN = const(4)
NSS_PIN = const(5)


if __name__ == '__main__':
    spi = SoftSPI(baudrate=2500000, polarity=0, phase=0, sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
    spi.init()

    rdr = MFRC522(spi=spi, gpioCs=NSS_PIN, gpioRst=RST_PIN)

    while True:
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))

                print(f'UID: {uid}')

        sleep_ms(100)
