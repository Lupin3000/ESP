# Package management

## Table of Contents

- [Prolog](#prolog)
- [Download and installation of external libraries](#download-and-installation-of-external-libraries)
- [Microcontroller without LAN/WLAN](#microcontroller-without-lanwlan)
- [Microcontroller with LAN/WLAN](#microcontroller-with-lanwlan)

## Prolog

If you want to use for example, displays and sensors, you don't always have to develop everything yourself. There are already many resources that you can use.

However, you should always ask yourself the following questions:

- Does my ESP Microcontroller support LAN/WLAN?
- Can or do I always want to connect the device to the Internet?
- Did it even make sense for my goal or can I save resources?

## Download and installation of external libraries

Depending on the answer to these questions, you then have to decide how and when to install these external libraries! Here are a few hints/solution suggestions for possible scenarios.

### Microcontroller without LAN/WLAN

In this scenario, the microcontroller has no LAN/WLAN network features. In addition, no own firmware should be created.

In the local project (_root folder_) create another folder named `lib`.

> It is recommended to use the "lib" directory (_best practice_), but you can also save libraries to the `root` or other folders. But always note `sys.path` for other folders!

```shell
# create new directory
$ mkdir -p ~/Projects/ESP/lib
```

Download now the library into the folder. Here is an example for SSD1306:

```shell
# download resource into directory
$ curl -L 'https://raw.githubusercontent.com/micropython/micropython-lib/master/micropython/drivers/display/ssd1306/ssd1306.py' -o ~/Projects/ESP/lib/ssd1306.py
```

Now decide if you will freeze the downloaded module. You have already learned how to do this in the [MicroPython frozen code](./002_frozen_code.md).

Optional you can verify first, if directory `lib` exits on the ESP microcontroller. In my example only the `boot.py` exists.

```shell
# verify if directory exits (optional)
(venv) $ rshell -p [SERIAL-PORT] ls /pyboard/
...
/your/current/path>  boot.py
...
```

Upload the directory including the module and optional verify.

```shell
# upload directory incl file(s)
(venv) $ rshell -p [SERIAL-PORT] cp -r lib/ /pyboard/

# verify if upload was sucessful
(venv) $ rshell -p [SERIAL-PORT] ls /pyboard/lib/
...
/your/current/path> ssd1306.py
...
```

That's it! Wasn't it super easy?

### Microcontroller with LAN/WLAN

In this scenario, the ESP microcontroller has WLAN. However, the WLAN functionality will not be used later (_only for installation/downloading_). Also, the library is not stored locally.

Here you simply use the `REPL` and `mip`.

> Earlier versions of MicroPython still had `upip`. However, this is considered obsolete from **version:** `1.20.0`.

```shell
# start REPL from rshell
(venv) $ rshell -p [SERIAL-PORT] repl
```

```python
# import WLAN and STA_IF
>>> from network import WLAN, STA_IF

# create station object
>>> sta = WLAN(STA_IF)

# activate station network interface
>>> sta.active(True)

# establish connection to access point
>>> sta.connect('YOUR SSID', 'YOUR PASSWORD')

# verify connection (after few seconds)
>>> sta.isconnected()

# import mip
>>> import mip

# install module
>>> mip.install('ssd1306')

# verify installation/download (optional)
>>> import uos
>>> uos.listdir('/lib/')
['ssd1306.mpy']
```

To exit the `REPL` press keys `Control` + `x`.

This option was super easy too... wasn't it? There are many other options! No matter which one you want to use, simply adapt it to your needs and the environment. Also, have a look on MicroPython [documentation](https://docs.micropython.org/en/latest/reference/packages.html)!

[Home](https://github.com/Lupin3000/ESP) | [Previous](./009_neopixel_extended.md) | [Next](./010_i2c_helper_tutorials.md)
