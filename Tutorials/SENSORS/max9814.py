from micropython import const
from machine import Pin, ADC
from utime import sleep_ms


# define constant
ADC_GPIO_PIN = const(34)
DELAY = const(1)

# create ADC object
mic = ADC(Pin(ADC_GPIO_PIN))
mic.atten(ADC.ATTN_11DB)


if __name__ == '__main__':
    while True:
        print(f'[INFO] Microphone ADC value {mic.read()}')
        sleep_ms(DELAY)
