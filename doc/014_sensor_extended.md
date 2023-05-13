# Sensor Extended

## Table of Contents

- [Prolog](#prolog)
- [Measure environment decibel (MAX9814 - SSD1306)](#measure-environment-decibel-max9814---ssd1306)
- [Obstacle Detection (Laser Sensor - SSD1306)](#obstacle-detection-laser-sensor---ssd1306)
- [Light Barrier (ALLNET: B18 - Pushover)](#light-barrier-allnet-b18---pushover)

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

> Note: The example uses IRQ multiplexing to respond to interrupts! If you don't understand how IRQs working, please have a look [here](./013_human_interaction_tutorials.md).

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
# download images
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/examples/sensors/go.pbm' -o examples/sensors/go.pbm
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/examples/sensors/stop.pbm' -o examples/sensors/stop.pbm

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

## Light Barrier (ALLNET: B18 - Pushover)

In the next example, a sensor with a light barrier is used. As soon as the light barrier is interrupted, a push notification should be sent to a mobile. An NTP time synchronization is carried out beforehand so that the time of the interruption can be sent.

### Requirements

- mandatory 1x Light Barrier (_[Allnet](https://www.allnet-shop.de/4DUINO/Module/ALLNET-4duino-Light-Barrier-Lichtschranke.html)_)
- mandatory Pushover Application (_[Pushover](https://pushover.net)_) 
- internet
- few cables 
- optional a breadboard

### Pinout table

Here you can see the respective wiring for the circuit.

| Light Barrier | ESP32 |
|---------------|-------|
| +5V           | 5V5   |
| GND           | GND   |
| OUT           | 23    |

### Code

The microcontroller needs to have internet connection! Therefor you need to set the device in station mode via `boot.py`. You can reuse the example from [here](./004_wlan_tutorials.md).

> [Source Code](../examples/sensors/allnet_B18_light_barrier.py) for example `allnet_B18_light_barrier.py`
> 
> [Source Code](../examples/network/boot.py) for station setup `boot.py`

Check your circuit, change constants to your needs and copy all files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy all files to esp32
/your/current/path> cp examples/sensors/allnet_B18_light_barrier /pyboard/main.py
/your/current/path> cp examples/network/boot.py /pyboard/boot.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program and to leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./014_sensor_tutorials.md) | [Next](./015_game_tutorials.md)
