# NeoPixel Extended

## Table of Contents

- [Prolog](#prolog)
- [NeoPixel Matrix Module](#neopixel-matrix-module)

## Prolog

If you work a lot with NeoPixel, you will quickly notice that the standard module already provides you with a lot, but you still have to code a lot yourself. So that you can save some time and work, here are a few modules that can help you.

## NeoPixel Matrix Module

With a NeoPixel Matrix you can create incredibly beautiful effects. This module offers you methods to control the LEDs not only via index. You can use x,y - coordinates, draw lines (_horizontal, vertical_) as well rectangles and numbers (_from 0 - 9_).

### Requirements

- [Waveshare - Pico RGB LED](https://www.waveshare.com/wiki/Pico-RGB-LED)
- or you create own matrix with NeoPixel strips (_with rows & cols_)

### Code

**Library & example script**

> [Source Code: Module](../lib/neopixelmatrix.py) for `lib/neopixelmatrix.py`

```shell
# download module
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/lib/neopixelmatrix.py' -o lib/neopixelmatrix.py
```

> [Source Code: Example script](../examples/neopixel/neopixel_matrix.py) for `neopixel_matrix.py`

**Usage example**

```shell
# copy module file into lib
(venv) $ rshell -p [SERIAL-PORT] cp lib/neopixelmatrix.py

# copy example file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/neopixel/neopixel_matrix.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d`. To leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./009_neopixel_tutorials.md) | [Next](./010_package_management.md)