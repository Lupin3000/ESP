# Micropython firmware

## Table of Contents

- [Get MicroPython version](#get-micropython-version)
- [Download MicroPython](#download-micropython)
- [Flash firmware](#flash-firmware)

## Get MicroPython Version

To avoid problems you need to know which MicroPython firmware and features your microcontroller supports. You can find out with [esptool.py](https://docs.espressif.com/projects/esptool/en/latest/esp32/index.html).

> Don't forget to connect the microcontroller and start the virtual environment (_in the project folder_).

```shell
# show information
(venv) $ esptool.py --port [SERIAL-PORT] flash_id
```

Note or write down the important information for chip type and features. Additional information such as MAC address, flash size, manufacturer, stub and so on can be helpful.

## Download MicroPython

Now open the MicroPython website for the downloads inside your browser. Here the direct [link](https://micropython.org/download/). Now search for the port (_chip type_) and matching features.

Select and download the latest `*.bin` file to your local device. Create another folder named `firmware` in the project folder and move the `*.bin` file into it.

```shell
# create local project directory
$ mkdir -p ~/Projects/ESP/firmware
```

Inside your project root the structure should be similar to this example:

```shell
$ tree .
|____firmware
| |____esp32-20230426-v1.20.0.bin
|____venv
| |____bin
...
```

> As you can see, all following examples are with MicroPython **version:`1.20.0`**.

## Flash firmware

Erase everything before flashing a new version. Here few examples for different chip types:

```shell
# erease flash (ESP32)
(venv) $ esptool.py --chip esp32 --port [SERIAL-PORT] erase_flash

# erease flash (ESP32-S2-WROVER)
(venv) $ esptool.py --chip esp32s2 --port [SERIAL-PORT] erase_flash

# erease flash (ESP32-S3)
(venv) $ esptool.py --chip esp32s3 --port [SERIAL-PORT] erase_flash
```

Now flash the new firmware. Pay attention to the respective information about the chip type as well as notes on the MicroPython download page!

Here an example for ESP32 with usage of `firmware` directory. 

```shell
# flash firmware (ESP32)
(venv) $ esptool.py --chip esp32 --port [SERIAL-PORT] --baud 460800 write_flash -z 0x1000 firmware/esp32-20230426-v1.20.0.bin
```

> Read careful the respective `Installation instructions` on download page!

This process can take some time.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./001_local_environment.md) | [Next](./003_serial_connection.md)
