# WLAN tutorials

## Table of Contents

- [Prolog](#prolog)
- [Scan for access points](#scan-for-access-points)
- [Connect as station to access point](#connect-as-station-to-access-point)
- [Create own access point (open)](#create-own-access-point-open)
- [Create own access point (WP2)](#create-own-access-point-wp2)
- [Additional information](#additional-information)

## Prolog

If your microcontroller has WLAN capabilities, you can take advantage of networks. All you really have to do is to decide in which mode you want to operate the microcontroller. 

The local directory structure and files after all examples:

```shell
$ tree .
|____firmware
| |____esp32-20220618-v1.19.1.bin
|____examples
| |____board
|   |____esp32_memory.py
|   |____esp32_information.py
| |____mpy
|   |____example_module.py
| |____wlan
|   |____ap_scanner.py
|   |____simple_station.py
|   |____wp2_access_point.py
|   |____open_access_point.py
|____venv
| |____bin
...
```

**Advantage: station mode**

- You can connect to the microcontroller with almost any other device in the network (_e.g. home network_)
- If the access point is connected to the internet, you can also do it mostly with the microcontroller

**Advantage: access point mode**

- Other nearby devices can easily connect to the microcontroller
- The microcontroller's WLAN is initially not directly connected to the other networks (_keyword: security_)

## Scan for access points

It sometimes makes sense to scan the surrounding area for access points. You can later try to scan for the known access points and if they cannot be reached, cancel further connection establishment. But here is just the scan itself.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP32/examples/wlan

# create script
$ touch ~/Projects/ESP32/examples/wlan/ap_scanner.py
```

> [Source Code](../examples/wlan/ap_scanner.py) for `ap_scanner.py`

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/wlan/ap_scanner.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press the keys `Control` + `d` or the `reset button` and observe the output. If you want to leave the REPL, press keys `Control` + `x`.

## Connect as station to access point

Okay, now try to connect to a reachable and known access point.

```shell
# create script
$ touch ~/Projects/ESP32/examples/wlan/simple_station.py
```

> [Source Code](../examples/wlan/simple_station.py) for `simple_station.py`

> Change the values for `_AP_SSID` and `_AP_PASSWORD` before running!

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/wlan/simple_station.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press the keys `Control` + `d` and observe the output. In case of `OSError: Wifi Internal Error` try the `reset button`. If you want to leave the REPL, press keys `Control` + `x`.

> The script still has plenty of room for improvements but target was to show the minimum.

## Create own access point (open)

Even if it is now against all security, the first access point is created without a password (_for learning purposes_).

```shell
# create script
$ touch ~/Projects/ESP32/examples/wlan/open_access_point.py
```

> [Source Code](../examples/wlan/open_access_point.py) for `open_access_point.py`

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/wlan/open_access_point.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

> If you have the opportunity, scan for access points with another device.

Press the keys `Control` + `d` or the `reset button` and observe the output. If you want to leave the REPL, press keys `Control` + `x`.

## Create own access point (WP2)

Then with a security standard for wireless radio networks based on Advanced-Encryption-Standard (_AES_) technology.

```shell
# create script
$ touch ~/Projects/ESP32/examples/wlan/wp2_access_point.py
```

> [Source Code](../examples/wlan/wp2_access_point.py) for `wp2_access_point.py`

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/wlan/wp2_access_point.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press the keys `Control` + `d` or the `reset button` and observe the output. If you want to leave the REPL, press keys `Control` + `x`.

## Additional information

Later examples then fall back on this basic examples. Think about what the improved version of the examples in `boot.py` would do then!

[Home](https://github.com/Lupin3000/ESP) | [Previous](./006_board_tutorials.md) | [Next](./006_board_tutorials.md)
