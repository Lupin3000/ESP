from micropython import const
from machine import Pin, ADC
from utime import sleep


# define constants
ADC_PIN_GPIO = const(32)
LED_GPIO_PIN = const(21)
MAX_SHADOW = const(75)
DELAY = const(1)

# initialize ADC
adc = ADC(Pin(ADC_PIN_GPIO))
led = Pin(LED_GPIO_PIN, Pin.OUT)

while True:
    adc_value = adc.read_u16()
    value = round(adc_value / 65535 * 100, 2)
    print(f'[INFO] shadow {value} %')

    if value > MAX_SHADOW:
        print('[INFO] LED ON')
        led.value(1)
    else:
        print('[INFO] LED OFF')
        led.value(0)

    sleep(DELAY)
