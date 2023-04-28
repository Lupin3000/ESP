from micropython import const
from machine import Pin
from utime import sleep


LED_RED_GPIO_PIN = const(21)
LED_GREEN_GPIO_PIN = const(22)
LED_BLUE_GPIO_PIN = const(23)
DELAY_SECONDS = const(3)


if __name__ == '__main__':
    led_red_pin = Pin(LED_RED_GPIO_PIN, Pin.OUT)
    led_green_pin = Pin(LED_GREEN_GPIO_PIN, Pin.OUT)
    led_blue_pin = Pin(LED_BLUE_GPIO_PIN, Pin.OUT)

    while True:
        print('[INFO] LED red')
        led_red_pin.value(1)
        led_green_pin.value(0)
        led_blue_pin.value(0)
        sleep(DELAY_SECONDS)

        print('[INFO] LED green')
        led_red_pin.value(0)
        led_green_pin.value(1)
        led_blue_pin.value(0)
        sleep(DELAY_SECONDS)

        print('[INFO] LED blue')
        led_red_pin.value(0)
        led_green_pin.value(0)
        led_blue_pin.value(1)
        sleep(DELAY_SECONDS)

        print('[INFO] LED red & green')
        led_red_pin.value(1)
        led_green_pin.value(1)
        led_blue_pin.value(0)
        sleep(DELAY_SECONDS)

        print('[INFO] LED red & blue')
        led_red_pin.value(1)
        led_green_pin.value(0)
        led_blue_pin.value(1)
        sleep(DELAY_SECONDS)

        print('[INFO] LED blue & green')
        led_red_pin.value(0)
        led_green_pin.value(1)
        led_blue_pin.value(1)
        sleep(DELAY_SECONDS)

        print('[INFO] LED red & blue & green')
        led_red_pin.value(1)
        led_green_pin.value(1)
        led_blue_pin.value(1)
        sleep(DELAY_SECONDS)
