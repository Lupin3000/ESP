# Environment & ESP Setup

## Table of Contents

- [Requirements](#Requirements)
- [Environment](#Environment)
- [MicroPython](#MicroPython)

### Requirements

**Mandatory**

> To setup your ESP device, you need following items:

- USB cable(s)
- Python 3.x
- Internet access
- ESP device(s)

**Optional**

> To the ESP tutorials/examples, you need following items:

- USB Hub(s)
- Breadboard
- Resistor(s)
- Sensor(s)
- LED(s)
- Dupont/Jumper cable(s)
- Servomotor(s)
- Piezo Buzzer
- NeoPixel LED Strip(s)

> Have a look on specific "Help pages" for more details!

- [Help page for LED examples](../Tutorials/LED/help.md)
- [Help page for Sensor examples](../Tutorials/SENSORS/help.md)

### Environment

> Many sources recommend using various IDE's (_e.g. Arduino, Thonny, uPyCraft, Mu, etc._). They are all very good but not really needed.

**Documentation**

- [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/)
- [rshell](https://github.com/dhylands/rshell)
- [mpfshell](https://github.com/wendlers/mpfshell)

**Installation**

```shell
# create project
$ mkdir -p ~/Projects/ESP32

# change into project directory
$ cd ~/Projects/ESP32/

# create Python virtualenv
$ python3 -m venv venv

# activate virtualenv
$ source venv/bin/activate

# install packages (manually)
(venv) $ pip3 install pyserial adafruit-ampy esptool rshell

# install packages (automatically)
(venv) $ pip3 install -r requirements.txt

# show installed packages (optional)
(venv) $ pip3 freeze
```

### MicroPython

> It is very important to use the appropriate MicroPython binary for the ESP chip! You can quickly find out this information via `esptool`. Depending on the operating system, you also need the VCP drivers (_before you start_).

- [VCP Driver for macOS/Windows](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads)

```shell
# get SERIAL-PORT (on macOS)
$ ls -l /dev/cu.usb*

# get SERIAL-PORT (on linux)
$ ls -l /dev/ttyUSB*
```

On macOS (_depending to ESP board_) you can find `/dev/tty.usbmodem*` or `/dev/tty.usbserial*`. On Linux `/dev/ttyUSB*` or `/dev/ttyACM*`.

```shell
# show information
(venv) $ esptool.py --port [SERIAL-PORT] flash_id
```

**Flash Firmware**

- [MicroPython firmware](https://micropython.org/download/)

Download the `*.bin` file suitable for ESP devices and flash MicroPython.

```shell
# erease flash (ESP32)
(venv) $ esptool --chip esp32 --port [SERIAL-PORT] erase_flash

# upload mircopython firmware (ESP32)
(venv) $ esptool --chip esp32 --port [SERIAL-PORT] --baud 460800 write_flash -z 0x1000 [BINFILE]
```

**Connect to ESP**

> As already mentioned there are many possibilities to create a connection. Here now few examples. For macOS `screen` is already available (_no installation needed_). For Linux tools like `picocom` or `minicom` could be interesting.

```shell
# create remote connection (SCREEN)
$ screen [SERIAL-PORT] 115200

# create remote connection (RSHELL)
(venv) $ rshell --port [SERIAL-PORT]

# create remote connection (MPFSHELL)
(venv) $ mpfshell -o [SERIAL-PORT]
```

**MicroPython Documentation**

- [MicroPython](https://docs.micropython.org/en/latest/)

[Go Back](https://github.com/Lupin3000/ESP)
