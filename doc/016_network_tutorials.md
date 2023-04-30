# Network tutorials

## Table of Contents

- [Prolog](#prolog)
- [Important preparation](#important-preparation)
- [Time synchronisation with NTP](#time-synchronisation-with-ntp)

## Prolog

Here are a few examples of network very basic interactions. These are then reused in later examples.

## Important preparation

Since all examples in this section require an internet connection, the file `boot.py` is required to connect to the access point as a station. This saves a lot of duplicate code and helps with structuring.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP32/examples/network

# download boot.py from microcontroller
(venv) $ rshell -p [SERIAL-PORT] cp /pyboard/boot.py examples/network/

# verify download (optional)
$ cat examples/network/boot.py
```

Here is the `boot.py` code for connecting as a station.

> [Source Code](../examples/network/boot.py) for `boot.py`

Adjust the values for `WLAN_SSID` and `WLAN_PASSWORD` to your environment. Load the `boot.py` back onto your ESP microcontroller.

```shell
# upload file from local environment to esp
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/boot.py /pyboard/

# verify remote file (optional)
(venv) $ rshell -p [SERIAL-PORT] cat /pyboard/boot.py
```

You can check if the connection really works before you continue with the next examples. If you notice an error, you can also fix it directly!

```shell
# edit remote file (optional)
(venv) $ rshell -p [SERIAL-PORT] edit /pyboard/boot.py
```

## Time synchronisation with NTP

The time always starts (_without prior change_) with `00:00 01.01.2000`! If you followed the example [I2C OLED date and time (ssd1306)](./015_display_tutorials.md), you should have noticed. That should change now.

```shell
# create script
$ touch ~/Projects/ESP32/examples/network/time_synchronisation_ntp.py
```

> [Source Code](../examples/network/time_synchronisation_ntp.py) for `time_synchronisation_ntp.py`

> You have to adapt the value for `UTC_OFFSET` to your local environment!

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/time_synchronisation_ntp.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` button. To leave the REPL, press keys `Control` + `x`.

> Test also without `rshell` connection! For example with `screen`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./015_display_tutorials.md) | [Next]()
