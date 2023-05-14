# Network

## Table of Contents

- [Prolog](#prolog)
- [Important preparation](#important-preparation)
- [Time synchronisation with NTP](#time-synchronisation-with-ntp)
- [DNS resolve](#dns-resolve)
- [HTTP status](#http-status)
- [REST API](#rest-api)
- [HTML webserver](#html-webserver)
- [Additional information](#additional-information)

## Prolog

Here are a few examples of network very basic interactions. These are then reused in later examples.

## Important preparation

Since all examples in this section require an internet connection, the file `boot.py` is required to connect to the access point as a station. This saves a lot of duplicate code and helps with structuring.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP/examples/network

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

The time always starts (_without prior change_) with `00:00 01.01.2000`! If you followed the example [I2C OLED date and time (ssd1306)](./011_display_ssd1306_tutorials.md), you should have noticed. That should change now.

```shell
# create script
$ touch ~/Projects/ESP/examples/network/time_synchronisation_ntp.py
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

## DNS resolve

This example contains very little code, but it can become very important! It is about resolving the corresponding IP (_v4_) from a domain.

```shell
# create script
$ touch ~/Projects/ESP/examples/network/dns_resolve.py
```

> [Source Code](../examples/network/dns_resolve.py) for `dns_resolve.py`

To change the target, just modify the value of constant `DNS_TARGET`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/dns_resolve.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` button. To leave the REPL, press keys `Control` + `x`.

## HTTP status

Similar to the previous example (_DNS resolve_), this example can be extremely helpful. The HTTP status code of a domain is checked here.

**Overview**

- 1xx for information
- 2xx for successful operations
- 3xx for redirects
- 4xx for client side issues
- 5xx for server side issues

```shell
# create script
$ touch ~/Projects/ESP/examples/network/http_status.py
```

> [Source Code](../examples/network/http_status.py) for `http_status.py`

To change the target, just modify the value of constant `TARGET_URL`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/http_status.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` button. To leave the REPL, press keys `Control` + `x`.

## REST API

REST APIs are essential these days. These are also extremely important for IoT. So here is a small example for a `GET` request.

```shell
# create script
$ touch ~/Projects/ESP/examples/network/rest_api.py
```

> [Source Code](../examples/network/rest_api.py) for `rest_api.py`

To change the target, just modify the values of constant `API_TARGET` and variable `url`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/rest_api.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` button. To leave the REPL, press keys `Control` + `x`.

## HTML webserver

Now you will learn to create your first web server. This delivers a very simple HTML page.

```shell
# create script
$ touch ~/Projects/ESP/examples/network/html_webserver.py
```

> [Source Code](../examples/network/html_webserver.py) for `html_webserver.py`

Upload `html_webserver.py` as `main.py` to ESP microcontroller.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/html_webserver.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` button. Now search the IP and connect.

```shell
# start ARP scan to find IP (optional)
$ arp -a

# connect via curl
$ curl 'http://[IP MICROCONTROLLER]'
```

To stop the loop press keys `Control` and `c`, to leave the REPL, press keys `Control` + `x`.

## Additional information

When it comes to sensors, the WLAN and web server will be used again (_in a different forms_).

> You can delete or comment out the content of `boot.py` to save resources! As soon as it is needed again, you will be informed.

```shell
# start remote editor
(venv) $ rshell -p [SERIAL-PORT] edit /pyboard/boot.py
```

[Home](https://github.com/Lupin3000/ESP) | [Previous](./011_display_sh1106_tutorials.md) | [Next](./013_human_interaction_tutorials.md)
