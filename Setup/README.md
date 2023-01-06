# Setup

## Table of Contents

- [Requirements](#Requirements)
- [Environment](#Environment)
- [Micropython](#Micropython)

### Requirements

- USB cable(s)
- Python 3
- Internet access
- ESP device(s)

### Environment

> Many sources recommend using various IDE's (_e.g. Thonny, uPyCraft, Mu, etc._). They are all very good but not really needed.

**Documentation**

- [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/)
- [rshell](https://github.com/dhylands/rshell)

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

# install packages
(venv) $ pip3 install rshell esptool

# show installed packages (optional)
(venv) $ pip3 freeze
```

### Micropython

will follow soon...

**Firmware**

- [Firmware](https://micropython.org/download/)

**Documentation**

- [MicroPython](https://docs.micropython.org/en/latest/)

[Go Back](https://github.com/Lupin3000/ESP)
