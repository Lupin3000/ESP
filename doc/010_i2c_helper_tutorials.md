# I2C helper tutorials

## Table of Contents

- [Prolog](#prolog)
- [I2C scanner](#i2c-scanner)
- [SoftI2C scanner](#softi2c)

## Prolog

Many devices such as sensors and displays use the I2C (_Inter-Integrated Circuit_), but this presents a few hurdles for beginners. It starts with the fact that soldering has to be done very often here. Then the addresses must also be found (_in the case of bad or missing documentation_). Already 2 sources of error that deters so many people from using it.

It is therefore advantageous to create a script that confirms the basic functionality and outputs the necessary addresses.

## I2C scanner

Build now an I2C scanner, which will save you time in the future!

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP/examples/i2c_helper

# create script
$ touch ~/Projects/ESP/examples/i2c_helper/i2c_scanner.py
```

> [Source Code](../examples/i2c_helper/i2c_scanner.py) for `i2c_scanner.py`

Now connect the I2C device (_pay attention to the correct polarity_), copy the I2C scanner script to the ESP microcontroller and start the scan.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/i2c_helper/i2c_scanner.py /pyboard/i2c_scanner.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d`. Make a note of the important values of the output and leave the REPL, press keys `Control` + `x`. Don't forget to delete the scanner script on the microcontroller (_waste of resources_).

## SoftI2C

Since MicroPython version 1.14.x a message is displayed, that the usage of I2C is deprecated and [SoftI2C](https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=softi2c#software-i2c-bus) should be used. I won't go into the advantages of SoftI2C here, but I would like to mention that the switch is not that difficult and that it will probably be necessary at some point.

> In the later tutorials, for example the OLED display (_with ssd1306 driver_) you will come into contact with SoftI2C.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./010_package_management.md) | [Next](./011_display_tutorials.md)
