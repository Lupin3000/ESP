# Board tutorials

## Table of Contents

- [Know your options](#know-your-options)
- [The first script about board information](#the-first-script-about-board-information)
- [The second script about disc space and memory](#the-second-script-about-disc-space-and-memory)

## Know your options

Before you start you should always check which features your microcontroller and the MircoPython firmware support. If you have flashed the firmware for your microcontroller that is not 100% suitable, errors can occur. Therefore, test with the REPL first before you upload and run your code.

Connect your microcontroller to your local device, start the local environment and connect via `rshell`.

```shell
# change into project root directory
$ cd ~/Projects/ESP32

# activate python virtual environment
$ source venv/bin/activate

# connect and start REPL
(venv) $ rshell -p [SERIAL-PORT] repl
```

Have the modules displayed in the repl.

```python
# list MicroPython modules
>>> help('modules')
```

### MicroPython information (_usys_)

The firmware information can be displayed very easily via the `usys` module.

```python
# import platform and version from usys
>>> from usys import platform, version

# print platform information
>>> print(platform)

# print version information
>>> print(version)
```

### CPU frequency (_machine_)

Show the CPU frequency in `Hertz`.

```python
# import unique_id and freq from machine
>>> from machine import unique_id, freq

# import hexlify from ubinascii
>>> from ubinascii import hexlify

# print unique id trough hexlify
>>> print(hexlify(unique_id(), ':'))

# print frequency information
>>> print(f"{freq()} Hz")
```

### Hall and temperature sensor information (_esp32_)

Show information about hall sensor and current temperature in `Fahrenheit`.

```python
# import hall_sensor and raw_temperature from esp32
>>> from esp32 import hall_sensor, raw_temperature

# print internal hall sensor
>>> print(hall_sensor())

# print internal temperature of the MCU, in Fahrenheit
>>> print(f"{raw_temperature()} F")
```

I hope no issues occur till here! To know more about MicroPython libraries, read the content of this [link](https://docs.micropython.org/en/latest/). To leave the REPL press keys `Control` + `x`.

## The first script about board information

> The assumption is that you are already in the root folder of your project.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP32/examples/board

# create script
$ touch ~/Projects/ESP32/examples/board/esp32_information.py
```

> [Source Code](../examples/board/esp32_information.py) for `esp32_information.py`

Now connect via rshell to your microcontroller, copy the file as `main.py` and execute.

```shell
# start serial connection
(venv) $ rshell -p [SERIAL-PORT]

# list content of pyboard (optional)
/your/current/path> ls /pyboard/

# copy file into pyboard as main.py
/your/current/path> cp examples/board/esp32_information.py /pyboard/main.py

# change into REPL
/your/current/path> repl
```

Press the keys `Control` + `d` and observe the output. Inside the repl you also can press the `reset button` of your microcontroller. If you want to leave the REPL, press keys `Control` + `x`.

```shell
# exit rshell connection
/your/current/path> exit
```

## The second script about disc space and memory

The second script should output information about the current disc space and memory.

```shell
# create script
$ touch ~/Projects/ESP32/examples/board/esp32_memory.py
```

> [Source code](../examples/board/esp32_memory.py) for `esp32_memory.py`

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/board/esp32_memory.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press the keys `Control` + `d` or the `reset button` and observe the output. If you want to leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./005_frozen_code.md) | [Next]()
