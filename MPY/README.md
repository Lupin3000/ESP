# MicroPython MPY

[Here](https://docs.micropython.org/en/latest/reference/mpyfiles.html) you will find all needed information about *.mpy files.

## Requirements

```shell
# install mpy-cross
(venv) $ pip3 install mpy-cross 
```

## Create binary container file format (_mpy_)

### Compile py to mpy

```shell
# change directory
(venv) $ cd Tutorials/MPY/

# run compile
(venv) $ mpy-cross example.py

# list directory files (optional)
(venv) $ ls -la
```

### Copy mpy to device

```shell
# copy mpy via RSHELL
(venv) $ rshell -p [SERIAL-PORT] cp example.mpy /pyboard/example.mpy
```

## Run mpy via REPL

```shell
# copy mpy via RSHELL
(venv) $ rshell -p [SERIAL-PORT] repl
```

```python
>>> import example
[INFO] MPY example
[INFO] Memory free 108400 bytes
[INFO] MCU 118 Fahrenheit
```

[Go Back](https://github.com/Lupin3000/ESP)
