# Sensor Extended

## Table of Contents

- [Prolog](#prolog)
- [Measure environment decibel (MAX9814 - SSD1306)](#measure-environment-decibel-max9814---ssd1306)
- [Obstacle Detection (Laser Sensor - SSD1306)](#obstacle-detection-laser-sensor---ssd1306)

## Prolog

This time we turn to other sensors and various possibilities to display the measured values or to react to them. Depending on the options and sensors that are available, simply adapt the examples to your needs.

## Measure environment decibel (MAX9814 - SSD1306)

In this example, the ambient noise is to be measured and shown on a display (_in decibel_).

### Requirements

- mandatory 1x Microphone (_example MAX9814_)
- mandatory 1x I2C OLED (_example 0.96" 128x64_)
- few cables 
- optional a breadboard

### Pinout table

Here you can see the respective wiring for the circuit.

| Device Name  | Device Pin | ESP32 Pin |
|--------------|------------|-----------|
| OLED Display | GND        | GND       |
| OLED Display | VCC        | 3V3       |
| OLED Display | SCL        | 22        |
| OLED Display | SDA        | 21        |
| Microphone   | GND        | GND       |
| Microphone   | Vdd        | 3V3       |
| Microphone   | Out        | 34        |

### Code

Since an OLED display is used here to display the decibel values, other modules and fonts are required in addition to the example script.

> [Source Code](../examples/sensors/max9814.py) for example `max9814.py`
> 
> [Source Code](../lib/ssd1306.py) for module `ssd1306.py`
> 
> [Source Code](../lib/writer.py) for module `writer.py`
> 
> [Source Code](../lib/freesans20.py) for font `freesans20.py`

Check your circuit and copy all files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy all files to esp32
/your/current/path> cp lib/ssd1306.py /pyboard/lib/
/your/current/path> cp lib/writer.py /pyboard/lib/
/your/current/path> cp lib/freesans20.py /pyboard/lib/
/your/current/path> cp examples/sensors/max9814.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the loop press keys `Control`+ `c`, to leave the REPL, press keys `Control` + `x`.

## Obstacle Detection (Laser Sensor - SSD1306)

Everything goes super fast and your vehicles and robots must be able to stop and resume movements very quickly. With the following example you will learn to control these fast movements via obstacle detection. A laser sensor is used for this.  

> Note: The example uses IRQ multiplexing to respond to interrupts! If you don't understand how IRGs working, please have a look [here](./013_human_interaction_tutorials.md).

### Requirements

- mandatory 1x Laser Sensor 10929 (_[Waveshare](https://www.waveshare.com/laser-sensor.htm)_)
- mandatory 1x I2C OLED (_example 0.96" 128x64_)
- few cables 
- optional a breadboard

### Pinout table

Here you can see the respective wiring for the circuit.

| Device Name  | Device Pin | ESP32 Pin |
|--------------|------------|-----------|
| OLED Display | GND        | GND       |
| OLED Display | VCC        | 3V3       |
| OLED Display | SCL        | 22        |
| OLED Display | SDA        | 21        |
| Laser Sensor | GND        | GND       |
| Laser Sensor | VCC        | 3V3       |
| Laser Sensor | DOUT       | 23        |


### Code

The OLED display is used to display 2 images for obstacle detection (_Stop & Go_). Therefor 2x `*.pbm` images and 1x driver module are required in addition to the example script.

> [Source Code](../examples/sensors/laser_sensor_10929.py) for example `laser_sensor_10929.py`
> 
> [Source Code](../lib/ssd1306.py) for module `ssd1306.py`

Check your circuit and copy all files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy all files to esp32
/your/current/path> cp examples/sensors/go.pbm /pyboard/
/your/current/path> cp examples/sensors/stop.pbm /pyboard/
/your/current/path> cp examples/sensors/laser_sensor_10929.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program and to leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./014_sensor_tutorials.md) | [Next](./015_game_tutorials.md)
