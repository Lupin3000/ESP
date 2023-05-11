from micropython import const
from machine import Pin, SPI, ADC
from utime import sleep_ms, ticks_ms
import pcd8544


ADC_PIN = const(32)
BUTTON_GPIO_PIN = const(22)

LCD_BAUDRATE = const(2000000)
LCD_BITS = const(8)
LCD_POLARITY = const(0)
LCD_PHASE = const(0)

LCD_RST_PIN = const(14)
LCD_CE_PIN = const(5)
LCD_DC_PIN = const(19)
LCD_DIN_PIN = const(23)
LCD_CLK_PIN = const(18)
LCD_BL_PIN = const(12)


def interrupt_handler(pin) -> None:
    """
    button interrupt handler
    :param pin: number for GPIO pin
    :return: None
    """
    _ = pin
    new_time = ticks_ms()

    if (new_time - last_time) > 200:
        fire_bullet()


def draw_gun(x: int, y: int) -> None:
    """
    draw gun on screen by coordinates
    :param x: x coordinate for gun
    :param y: y coordinate for gun
    :return: None
    """
    pos_x = int(x)
    pos_y = int(y)

    lcd.fill_rect(pos_x, pos_y, 4, 4, 1)
    lcd.fill_rect(pos_x - 1, pos_y + 3, 6, 4, 1)


def fire_bullet() -> None:
    """
    set state for bullet
    :return: None
    """
    global bullet_state
    global gun_x
    global gun_y

    if bullet_state == 'ready':
        bullet_state = 'fire'
        draw_bullet(gun_x, gun_y)


def draw_bullet(x: int, y: int) -> None:
    """
    draw bullet on screen by coordinates
    :param x: x coordinate for bullet
    :param y: y coordinate for gun
    :return: None
    """
    global bullet_state
    global bullet_x_pos
    global bullet_y_pos

    bullet_x_pos = int(x)
    bullet_y_pos = int(y)

    lcd.fill_rect(bullet_x_pos, bullet_y_pos, 3, 3, 1)

    if bullet_y_pos <= 10:
        bullet_state = 'ready'


def draw_enemy(x: int, y: int) -> None:
    """
    draw enemy on the screen by coordinates
    :param x: x coordinate for gun
    :param y: y coordinate for gun
    :return: None
    """
    pos_x = int(x)
    pos_y = int(y)

    lcd.fill_rect(pos_x, pos_y, 6, 4, 1)


def is_overlap(coords_obj_a: list, coords_obj_b: list) -> bool:
    """
    calculate collision of two object
    :param coords_obj_a: list of coordinates for object a
    :param coords_obj_b: list of coordinates for object b
    :return: bool
    """
    obj_a = list(coords_obj_a)
    obj_b = list(coords_obj_b)

    if (obj_a[0] >= obj_b[2]) or (obj_a[2] <= obj_b[0]) or (obj_a[3] <= obj_b[1]) or (obj_a[1] >= obj_b[3]):
        return False
    else:
        return True


if __name__ == '__main__':
    spi = SPI(1, baudrate=LCD_BAUDRATE, bits=LCD_BITS, polarity=LCD_POLARITY, phase=LCD_PHASE,
              sck=Pin(LCD_CLK_PIN), mosi=Pin(LCD_DIN_PIN), miso=Pin(LCD_DC_PIN))
    spi.init()
    cs = Pin(LCD_CE_PIN)
    dc = Pin(LCD_DC_PIN)
    rst = Pin(LCD_RST_PIN)
    bl = Pin(LCD_BL_PIN, Pin.OUT, value=1)

    lcd = pcd8544.PCD8544_FRAMEBUF(spi, cs, dc, rst)
    lcd.contrast(0x3f, pcd8544.BIAS_1_40, pcd8544.TEMP_COEFF_2)

    adc = ADC(Pin(ADC_PIN, Pin.IN))
    adc.atten(ADC.ATTN_11DB)

    btn = Pin(BUTTON_GPIO_PIN, Pin.IN, Pin.PULL_UP)
    btn.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_handler)

    lcd.fill(0)
    intro = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc0, 0x60, 0xb0, 0x10,
        0x08, 0x00, 0x80, 0x84, 0x80, 0x84, 0x84, 0x80, 0x80, 0x84, 0x80, 0x88, 0x10, 0x90, 0xa0, 0x60, 0x80, 0x80,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x40, 0xc0, 0xe0, 0xe0, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0, 0xe0, 0x88,
        0x38, 0xfc, 0xe0, 0x8c, 0x7c, 0xf4, 0x74, 0xc4, 0xa4, 0x80, 0x80, 0x82, 0x83, 0xc3, 0x03, 0x41, 0x83, 0xc3,
        0x83, 0xc1, 0x43, 0xc1, 0xc3, 0x01, 0x81, 0x43, 0xc3, 0x41, 0xc3, 0x41, 0x81, 0xc3, 0x83, 0x03, 0x83, 0xc3,
        0x83, 0x80, 0xc0, 0xc4, 0x64, 0xe4, 0xf8, 0x3c, 0x88, 0xe4, 0xf8, 0x38, 0x88, 0xe8, 0xf0, 0xf0, 0xf0, 0xf0,
        0xe0, 0xe0, 0xe0, 0x60, 0x40, 0x80, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x0e, 0x1e, 0x0d, 0x29, 0x5a, 0x34, 0x75, 0x33, 0xbb, 0xdf, 0xf3, 0xf7, 0xff, 0xf7,
        0xfc, 0xfd, 0xbb, 0xff, 0xdf, 0xd9, 0xee, 0xfe, 0xef, 0xfd, 0xfe, 0x75, 0x3e, 0xf6, 0xff, 0xb7, 0x37, 0x9e,
        0x17, 0x1e, 0x1b, 0x1e, 0x16, 0x1f, 0x17, 0x1e, 0x1f, 0x16, 0x1f, 0x1a, 0x16, 0xbe, 0xd7, 0xff, 0xfe, 0x36,
        0x7d, 0xf6, 0xfd, 0xee, 0xfe, 0xef, 0xed, 0xdf, 0xbb, 0xff, 0xbe, 0xf8, 0xff, 0xf7, 0xff, 0xf3, 0xd7, 0x9f,
        0xb9, 0x25, 0x56, 0x3a, 0x3a, 0x0d, 0x1e, 0x07, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x03, 0x03,
        0x05, 0x03, 0x0b, 0x07, 0x07, 0x07, 0x0f, 0x24, 0x39, 0xa7, 0x4f, 0x9f, 0xfe, 0xf8, 0xe3, 0xef, 0x7f, 0x60,
        0x60, 0x30, 0x20, 0x30, 0x30, 0x30, 0x20, 0x30, 0x20, 0x30, 0x20, 0x30, 0x6c, 0x69, 0xef, 0xf3, 0xfc, 0xfe,
        0x9f, 0x6f, 0xb7, 0x19, 0x24, 0x0b, 0x0f, 0x07, 0x07, 0x07, 0x01, 0x07, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x03, 0x03, 0x07, 0x43, 0x06, 0x06,
        0x26, 0x04, 0x0e, 0x04, 0x06, 0x2c, 0x04, 0x04, 0x0c, 0x04, 0x84, 0x06, 0x06, 0x86, 0x07, 0x03, 0x03, 0x03,
        0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x01, 0x40, 0x00, 0x01, 0x80, 0x08,
        0x00, 0x00, 0x48, 0x00, 0x00, 0x51, 0x00, 0x00, 0x01, 0x80, 0x00, 0x04, 0x80, 0x00, 0x04, 0x20, 0x00, 0x04,
        0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ])
    lcd.data(intro)
    sleep_ms(3000)

    last_time = 0
    score = 0

    gun_y = 40
    gun_x = 0

    bullet_y_speed = 5
    bullet_state = "ready"
    bullet_x_pos = gun_x
    bullet_y_pos = gun_y

    enemy_x = 20
    enemy_y = 12
    enemy_x_speed = 2
    enemy_y_speed = 2

    while True:
        lcd.fill(0)
        lcd.rect(0, 0, 84, 48, 1)
        lcd.fill_rect(0, 0, 84, 10, 1)
        lcd.text(f'Score:{str(score)}', 1, 2, 0)

        adc_val = adc.read_u16()
        gun_x = int(adc_val * (84 / 65535))
        if gun_x <= 2:
            gun_x = 2
        if gun_x >= 78:
            gun_x = 78

        draw_gun(gun_x, gun_y)

        enemy_x += enemy_x_speed
        if enemy_x > 70:
            enemy_x_speed *= -1
            enemy_y += enemy_y_speed
        if enemy_x < 10:
            enemy_x_speed *= -1
            enemy_y += enemy_y_speed

        draw_enemy(enemy_x, enemy_y)

        if bullet_state == 'fire':
            bullet_y_pos -= bullet_y_speed
            draw_bullet(bullet_x_pos, bullet_y_pos)

        collision_bullet_enemy = is_overlap(
            [enemy_x, enemy_y, (enemy_x + 6), (enemy_y + 4)],
            [bullet_x_pos, bullet_y_pos, (bullet_x_pos + 3), (bullet_y_pos + 3)]
        )
        if collision_bullet_enemy:
            score += 1
            enemy_x = 20
            enemy_y = 12
            bullet_x_pos = gun_x
            bullet_y_pos = gun_y
            bullet_state = 'ready'

        collision_gun_enemy = is_overlap(
            [enemy_x, enemy_y, (enemy_x + 6), (enemy_y + 4)],
            [gun_x, gun_y, (gun_x + 4), (gun_y + 8)]
        )
        if collision_gun_enemy:
            break

        lcd.show()
        sleep_ms(175)

    lcd.fill(0)
    lcd.text('You are', 0, 10, 1)
    lcd.text('KILLED', 0, 20, 1)
    lcd.show()
