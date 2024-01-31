from micropython import const
from machine import Pin, PWM
from utime import sleep


SERVO_GPIO_PIN = const(21)
SERVO_FREQUENCY = const(50)
DELAY_SECONDS = const(1)


def servo_angle(degree: int) -> int:
    """
    Convert degrees to duty_16 value (50Hz only)
    :param degree: integer value for degrees
    :return: integer duty cycle value
    """
    value = int(degree)

    return int(6553/180 * value + 1638)


if __name__ == '__main__':
    servo = PWM(Pin(SERVO_GPIO_PIN), freq=SERVO_FREQUENCY)

    # define min and max angle variables (in degrees)
    min_angle = 45
    max_angle = 135

    while True:
        for angle in range(min_angle + 10, max_angle + 10, 10):
            duty_value = servo_angle(angle)

            print(f'[INFO] current angle: {angle} duty_u16: {duty_value}')
            servo.duty_u16(duty_value)
            sleep(DELAY_SECONDS)

        for angle in reversed(range(min_angle, max_angle, 10)):
            duty_value = servo_angle(angle)

            print(f'[INFO] current angle: {angle} duty_u16: {duty_value}')
            servo.duty_u16(duty_value)
            sleep(DELAY_SECONDS)
