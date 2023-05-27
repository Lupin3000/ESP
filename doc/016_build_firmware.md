# MicroPython build firmware

## Table of Contents

- [Build ESP32 GENERIC Firmware](#build-esp32-generic-firmware)

## Build ESP32 GENERIC Firmware

### Requirements

- Debian 11
- ESP32

### Install requirements on Debian 11 (bullseye)

To build the MicroPython firmware on a Debian 11 yourself, you need a few packages.

```shell
# fetch latest versions of package list
$ sudo apt update

# install all required packages (ESP8266/ESP32)
$ sudo apt install -y git build-essential python3-virtualenv cmake libffi-dev pkg-config
```

> For the stm32 port, the ARM cross-compiler is required `$ sudo apt-get install arm-none-eabi-gcc arm-none-eabi-binutils arm-none-eabi-newlib`!

### ESP-IDF

The `esp-idf` is only required to build firmware for `ESP8266` and `ESP32` microcontroller! If you build for example firmware for Raspberry Pico, you can skip this section.

```shell
# change into user root directory
$ cd ~

# clone from repository
$ git clone -b v4.4 --recursive https://github.com/espressif/esp-idf.git

# change into cloned directory
$ cd esp-idf

# switch branch
$ git checkout v4.4

# initialize and update submodules
$ git submodule update --init --recursive

# run install script
$ ./install.sh
```

> There is also another very important and helpful file named `export.sh`! The usage will be shown later.

### MicroPython

Here is the download of the MicroPython repositories and the preparation (_for all imaginable boards or target systems_).

```shell
# change into user root directory
$ cd ~

# clone from repository
$ git clone https://github.com/micropython/micropython.git

# change into cloned directory
$ cd micropython/

# pre-compile some of the built-in scripts
$ make -C mpy-cross
```

### Build GENERIC

The MicroPython firmware is built with a few commands. The whole thing should run relatively smoothly as long as all dependencies have been resolved beforehand.

```shell
# change into esp-idf directory
$ cd ~/esp-idf/

# source export.sh
$ source export.sh

# change into esp32 port directory of micropython
$ cd ~/micropython/ports/esp32/

# make submodules
$ make submodules

# build GENERIC firmware
$ make

# verify directory content (optional)
$ ls -la build-GENERIC/

# verify firmware.bin file (optional)
$ file build-GENERIC/firmware.bin
```

> With `$ make BOARD=[board]` you also can build firmware for other boards like ESP32-S2 etc. instead only for `GENERIC`.

That was it! Here is another example of how you copy it to another system and flash the firmware on the microcontroller there.

```shell
# copy firmware
$ scp [USER]@[IP]:/home/[USER]/micropython/ports/esp32/build-GENERIC/firmware.bin ~/Projects/ESP/firmware/

# erase ESP
(venv) $ esptool.py --chip esp32 --port /dev/cu.usbserial-0001 erase_flash

# flash new firmware
(venv) $  esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 460800 write_flash -z 0x1000 firmware/firmware.bin

# connect via rshell
(venv) $ rshell -p /dev/cu.usbserial-0001 repl
```

[Home](https://github.com/Lupin3000/ESP) | [Previous](./015_game_tutorials.md) | [Next]()
