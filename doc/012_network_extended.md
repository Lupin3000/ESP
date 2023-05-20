# Network Extended

## Table of Contents

- [Prolog](#prolog)
- [Toggle LEDs via Webserver](#toggle-leds-via-webserver)

## Prolog

Now that you've learned a few basics about network functions, here are a few application examples.

## Toggle LEDs via Webserver

In this example, a website is displayed in the browser using station mode. There are two toggle options on this web page to turn LEDs on or off.

> The example is kept very simple (_without further checks_). Once you have understood it, you can expand it at any time.

### Requirements

- mandatory 2x LEDs (_any color_)
- mandatory 2x resistors (_min. 220 ohms_)
- few cables
- optional a breadboard

### Circuit

![012_circuit_diagram_led_server.png](../images/circuits/012_circuit_diagram_led_server.png)

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/network/led_controller_webserver.py

# create html
$ touch ~/Projects/ESP/examples/network/index.html
```

> [Source Code](../examples/network/led_controller_webserver.py) for `led_controller_webserver.py`
> 
> [Source Code](../examples/network/index.html) for html `index.html`
> 
> [Source Code](../examples/network/boot.py) for `boot.py`

Adjust the constants (_`boot.py` and `led_controller_webserver.py`_) according to your needs and check the circuit. Connect the microcontroller and transfer the files.

```shell
# copy script as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/led_controller_webserver.py /pyboard/main.py

# copy html
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/index.html /pyboard/

# copy boot.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/network/boot.py /pyboard/

# start repl on microcontroller
(venv) $ rshell -p [SERIAL-PORT] repl
```

To start your game press `reset` key or start with keys `Control` + `d`. To interrupt press keys `Control` + `c`. To finish the `rshell` - `repl` session, press keys `Control` + `x`.

> If you don't know the IP, use for example `$ arp -a` (_inside local terminal_) and then enter 'http://[IP OF MICROCONTROLLER]' in the browser.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./012_network_tutorials.md) | [Next](./013_human_interaction_tutorials.md)
