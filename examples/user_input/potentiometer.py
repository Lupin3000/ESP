from micropython import const
from machine import Pin, ADC
from utime import sleep_ms


ADC_PIN = const(32)
DURATION_MILLISECONDS = const(250)


if __name__ == '__main__':
    adc = ADC(Pin(ADC_PIN, mode=Pin.IN))
    adc.atten(ADC.ATTN_11DB)

    while True:
        adc_val = adc.read_u16()
        val = adc_val * (3.3 / 65535)

        print(f'[INFO] {round(val, 2)} V')
        sleep_ms(DURATION_MILLISECONDS)
