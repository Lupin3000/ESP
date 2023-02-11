from gc import mem_free
from esp32 import raw_temperature


print('[INFO] MPY example')
print(f'[INFO] Memory free {mem_free()} bytes')
print(f'[INFO] MCU {raw_temperature()} Fahrenheit')
