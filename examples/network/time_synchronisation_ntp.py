from micropython import const
from utime import time, localtime
from ntptime import settime


UTC_OFFSET = const(3600)


if __name__ == '__main__':
    estimated = localtime()
    estimated_date = f'{estimated[2]:02d}.{estimated[1]:02d}.{estimated[0]}'
    estimated_time = f'{estimated[3]:02d}:{estimated[4]:02d}'

    try:
        settime()
    except Exception as err:
        print(f'[ERROR] Connection to NTP server failed: {err}')

    actual = localtime(time() + UTC_OFFSET)
    actual_date = f'{actual[2]:02d}.{actual[1]:02d}.{actual[0]}'
    actual_time = f'{actual[3]:02d}:{actual[4]:02d}'

    print(f'[INFO] Non-synced time: {estimated_time} {estimated_date}')
    print(f'[INFO] Synced time: {actual_time} {actual_date}')
