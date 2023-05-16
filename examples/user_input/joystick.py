from micropython import const
from machine import Pin, ADC
from utime import sleep_ms, ticks_ms


GPIO_X = const(32)
GPIO_Y = const(33)
GPIO_BTN = const(35)


def btn_handler(pin) -> None:
    """
    debounce btn press and show information
    :param pin: class pin
    :return: None
    """
    global last_time

    new_time = ticks_ms()

    if (new_time - last_time) > 200:
        print(f'[INFO] Button pressed by {pin}')


if __name__ == '__main__':
    last_time = 0

    adc_x = ADC(Pin(GPIO_X, Pin.IN))
    adc_x.atten(ADC.ATTN_11DB)

    adc_y = ADC(Pin(GPIO_Y, Pin.IN))
    adc_y.atten(ADC.ATTN_11DB)

    btn = Pin(GPIO_BTN, Pin.IN, Pin.PULL_UP)
    btn.irq(trigger=Pin.IRQ_FALLING, handler=btn_handler)

    while True:
        adc_x_val = adc_x.read_u16()
        adc_y_val = adc_y.read_u16()

        print(f'[INFO] x:{adc_x_val} y:{adc_y_val}')
        sleep_ms(500)
