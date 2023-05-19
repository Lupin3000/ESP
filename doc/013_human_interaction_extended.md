# Human interaction Extended

## Table of Contents

- [Prolog](#prolog)
- [Move crosshair via joystick (sh1106)](#move-crosshair-via-joystick-sh1106)

## Prolog

As with the previous tutorials, here are a few more examples that should help you to solve any questions and problems you may have.

## Move crosshair via joystick (sh1106)

The goal of this tutorial is to use a joystick to move a crosshair on a screen. The respective XY position and the status of the button should also be displayed.

### Requirements

- mandatory SPI OLED display (_SH1106 [Waveshare](https://www.waveshare.com/1.3inch-oled-a.htm)_)
- mandatory 1x joystick
- few cables
- optional breadboard

### Pinout table

Here you can see the respective wiring for the circuit.

| Device   | Device Pin | ESP Pin |
|----------|------------|---------|
| OLED     | VCC        | 3V3     |
| OLED     | GND        | GND     |
| OLED     | NC         | -       |
| OLED     | DIN        | 23      |
| OLED     | CLK        | 18      |
| OLED     | CS         | 2       |
| OLED     | DC         | 5       |
| OLED     | RES        | 4       |
| Joystick | +5V        | 3V3     |
| Joystick | GND        | GND     |
| Joystick | X          | 32      |
| Joystick | Y          | 33      |
| Joystick | BUT        | 35      |

### Code

Actually the code is very simple. Correct wiring without creating a short circuit is a bit more difficult in this example.

> [Source Code](../examples/user_input/joystick_display.py) for example `joystick_display`
> 
> [Source Code](../lib/sh1106.py) for module `sh1106.py`

Check your circuit and copy all files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy all files to esp32
/your/current/path> cp lib/sh1106.py /pyboard/lib/
/your/current/path> cp examples/user_input/joystick_display.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the loop press keys `Control`+ `c`, to leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./013_human_interaction_tutorials.md) | [Next](./014_sensor_tutorials.md)
