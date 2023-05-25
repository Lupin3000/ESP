from micropython import const
from st7735s_096_lcd import LCD
from umachine import freq
from uos import uname
from utime import sleep


WHITE = const(0xFFFF)
BLACK = const(0x0000)
BLUE = const(0x1F00)
LIME = const(0x07E0)
GREEN = const(0xE007)
MAGENTA = const(0xF81F)


def get_values() -> tuple:
    values = uname()

    return f'System: {values[0]}', f'Python: {values[2]}', f'Freq: {freq()}'


if __name__ == '__main__':
    lcd = LCD()
    sleep(1)

    system_information = get_values()

    lcd.fill(BLACK)
    lcd.text('ESP32-S2 LCD 0.96', 2, 0, WHITE)
    lcd.hline(0, 12, lcd.width, WHITE)

    i = 10
    for item in system_information:
        i += 10
        lcd.text(f'* {str(item)}', 2, i, BLUE)

    lcd.fill_rect(2, 60, 20, 10, LIME)
    lcd.ellipse(40, 65, 10, 5, MAGENTA, True)
    lcd.fill_rect(60, 60, 40, 10, GREEN)
    lcd.ellipse(120, 65, 10, 5, MAGENTA, True)
    lcd.fill_rect(138, 60, 20, 10, LIME)

    lcd.show()
    sleep(30)

    lcd.backlight_off()
