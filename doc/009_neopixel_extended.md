# NeoPixel Extended

## Table of Contents

- [Prolog](#prolog)
- [NeoPixel Matrix Module](#neopixel-matrix-module)
- [NeoPixel Matrix Icons](#neopixel-matrix-icons)
- [NeoPixel Matrix Bounce](#neopixel-matrix-bounce)

## Prolog

If you work a lot with NeoPixel, you will quickly notice that the standard module already provides you with a lot, but you still have to code a lot yourself. So that you can save some time and work, here are a few modules that can help you.

## NeoPixel Matrix Module

With a NeoPixel Matrix you can create incredibly beautiful effects. This module offers you methods to control the LEDs not only via index. You can use x,y - coordinates, draw lines (_horizontal, vertical_) as well rectangles and numbers (_from 0 - 9_).

### Requirements

- [Waveshare - Pico RGB LED](https://www.waveshare.com/wiki/Pico-RGB-LED)
- or you create own matrix with NeoPixel strips (_with rows & cols_)

**Example**

![rgb_matrix_panel.jpg](../images/modules/rgb_matrix_panel.jpg)

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

## NeoPixel Matrix Icons

Through inheritance of the `neopixelmatrix` module, you can easily extend the module to draw simple icons on the Matrix. This saves you a lot of time, and you don't have to control every NeoPixel (_using the existing methods of the module_).

> The icons are not real pictures! By the way ... the same principle is used in the tutorial for [OLED Display (ssd1306)](./011_display_ssd1306_tutorials.md).

### Code

> [Source Code](../examples/neopixel/neopixel_matrix_icon.py) for `neopixel_matrix_icon.py`

```shell
# copy example file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/neopixel/neopixel_matrix_icon.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the loop press keys `Control`+ `c`, to leave the REPL, press keys `Control` + `x`.

> You could also display multicolored icons! For example by specifying further numbers like 2, 3, 4 (_inside the icon definition_) and so on with the respective RGB tuples (_as method parameters_).

## NeoPixel Matrix Bounce

This small example should show you further possibilities with an LED matrix. You will also learn a few basics about random number generators.

### Code

> [Source Code](../examples/neopixel/neopixel_matrix_bounce.py) for `neopixel_matrix_bounce.py`

```shell
# copy example file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/neopixel/neopixel_matrix_bounce.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the loop press keys `Control`+ `c`, to leave the REPL, press keys `Control` + `x`.


[Home](https://github.com/Lupin3000/ESP) | [Previous](./009_neopixel_tutorials.md) | [Next](./010_package_management.md)
