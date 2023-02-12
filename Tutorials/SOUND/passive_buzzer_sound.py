from micropython import const
from machine import Pin, PWM
from utime import sleep


# define constant
BUZZER_GPIO_PIN = const(23)
BUZZER_DUTY_CYCLE = const(1000)
DELAY = const(.3)

# create PWM object
buzzer = PWM(Pin(BUZZER_GPIO_PIN))

# define variables
tones = {"B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44, "FS1": 46, "G1": 49, "GS1": 52,
         "A1": 55, "AS1": 58, "B1": 62, "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93,
         "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123, "C3": 131, "CS3": 139, "D3": 147, "DS3": 156,
         "E3": 165, "F3": 175, "FS3": 185, "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262,
         "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370, "G4": 392, "GS4": 415, "A4": 440,
         "AS4": 466, "B4": 494, "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740,
         "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988, "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245,
         "E6": 1319, "F6": 1397, "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093,
         "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520,
         "AS7": 3729, "B7": 3951, "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978}

mario = ["E7", "E7", "P", "E7", "P", "C7", "E7", "P", "G7", "P", "P", "P", "G6", "P", "P", "P", "C7", "P", "P", "G6",
         "P", "P", "E6", "P", "P", "A6", "P", "B6", "P", "AS6", "A6", "P", "G6", "E7", "P", "G7", "A7", "P", "F7", "G7",
         "P", "E7", "P", "C7", "D7", "B6", "P", "P", "C7", "P", "P", "G6", "P", "P", "E6", "P", "P", "A6", "P", "B6",
         "P", "AS6", "A6", "P", "G6", "E7", "P", "G7", "A7", "P", "F7", "G7", "P", "E7", "P", "C7", "D7", "B6"]


def stop_tone() -> None:
    """
    Stop buzzer tone
    :return:
    """
    buzzer.duty_u16(0)


def play_tone(frequency: int) -> None:
    """
    Play tone by specific frequency
    :param frequency: int of frequency
    :return: None
    """
    buzzer.freq(frequency)
    buzzer.duty_u16(BUZZER_DUTY_CYCLE)
    sleep(DELAY)
    stop_tone()


def player(sound: list) -> None:
    """
    Simple sound player
    :param sound: list of song items
    :return: None
    """
    for item in range(len(sound)):
        if sound[item] == 'P':
            stop_tone()
        else:
            play_tone(tones[sound[item]])


print('[INFO] Play mario sound')
player(mario)
