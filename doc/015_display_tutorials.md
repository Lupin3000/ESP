# Display tutorials

## Table of Contents

- [Prolog](#prolog)
- [I2C OLED (ssd1306)](#i2c-oled-basics-ssd1306)

## Prolog

Today, almost nothing works for end users without displays. Displays are available in almost all sizes, shapes and colors and some still offer options (_e.g. touch_) that were unthinkable years ago. There are also different types such as LCD, OLED, TFT and so on.

You can use many of them on your ESP via MicroPython. Here are a few examples.

## I2C OLED basics (ssd1306)

The first example should show you a few basics. Play around with it (_modify the code_) and find out for yourself what else works.

### Requirements

- mandatory 1x I2C OLED (_example 0.96" 128x64_) 
- few cables 
- optional a breadboard

### Circuit

![015_circuit_diagram_i2c_oled.png](../images/examples/015_circuit_diagram_i2c_oled.png)

### Code

Install first the `ssd1306` driver! [Here](./013_package_management.md) you will find some solutions proposals about how to install.

> If you're using the SPI version, just adapt the code! [Here](https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html) it's described.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP32/examples/display

# create script
$ touch ~/Projects/ESP32/examples/display/i2c_oled_ssd1306_basics.py
```

> [Source Code](../examples/dipslay/i2c_oled_ssd1306_basics.py) for `i2c_oled_ssd1306_basics.py`

Check your circuit (_adapt pins if needed_) and copy the script to the microcontroller as `main.py`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/dipslay/i2c_oled_ssd1306_basics.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

[Home](https://github.com/Lupin3000/ESP) | [Previous](./014_i2c_helper_tutorials.md) | [Next]()
