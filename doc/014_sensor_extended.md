# Sensor Extended

## Table of Contents

- [Prolog](#prolog)
- [Measure environment decibel (MAX9814 - SSD1306)](#measure-environment-decibel-max9814---ssd1306)
- [Obstacle Detection (Laser Sensor - SSD1306)](#obstacle-detection-laser-sensor---ssd1306)
- [Light Barrier (ALLNET: B18 - Pushover)](#light-barrier-allnet-b18---pushover)
- [Environment Sensing (Bosh: BME680 - Web Server)](#environment-sensing-bosh-bme680---web-server)
- [Measure Distance (Pimoroni: VL53L1X - SSD1306)](#measure-distance-pimoroni-vl53l1x---ssd1306)
- [Temperature via WebBLE (Allnet: B38 Temp. Sensor)](#temperature-via-webble-allnet-b38-temp-sensor)

## Prolog

This time we turn to other sensors and various possibilities to display the measured values or to react to them. Depending on the options and sensors that are available, simply adapt the examples to your needs.

## Measure environment decibel (MAX9814 - SSD1306)

In this example, the ambient noise is to be measured and shown on a display (_in decibel_).

### Requirements

- mandatory 1x Microphone (_example MAX9814_)
- mandatory 1x I2C OLED (_example 0.96" 128x64_)
- few cables 
- optional a breadboard

**Example**

![max9814.jpg](../images/modules/max9814.jpg)

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

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/max9814.py
```

Since an OLED display is used here to display the decibel values, other modules and fonts are required in addition to the example script.

> [Source Code](../examples/sensors/max9814.py) for example `max9814.py`
> 
> [Source Code](../lib/ssd1306.py) for module `ssd1306.py`
> 
> [Source Code](../lib/writer.py) for module `writer.py`
> 
> [Source Code](../lib/freesans20.py) for font `freesans20.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy module file into /pyboard/lib/
/your/current/path> cp lib/ssd1306.py /pyboard/lib/
/your/current/path> cp lib/writer.py /pyboard/lib/
/your/current/path> cp lib/freesans20.py /pyboard/lib/

# copy script as main.py
/your/current/path> cp examples/sensors/max9814.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the loop press keys `Control`+ `c`, to leave the REPL, press keys `Control` + `x`.

## Obstacle Detection (Laser Sensor - SSD1306)

Everything goes very fast and your vehicles and robots must be able to stop and resume movements very quickly. With the following example you will learn to control these fast movements via obstacle detection. A laser sensor is used for this.  

> Note: The example uses IRQ multiplexing to respond to interrupts! If you don't understand how IRQs working, please have a look [here](./013_human_interaction_tutorials.md).

### Requirements

- mandatory 1x Laser Sensor 10929 (_[Waveshare](https://www.waveshare.com/laser-sensor.htm)_)
- mandatory 1x I2C OLED (_example 0.96" 128x64_)
- few cables 
- optional a breadboard

**Example**

![laser_sensor.jpg](../images/modules/laser_sensor.jpg)

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

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/laser_sensor_10929.py

# download images
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/images/src/go.pbm' -o images/src/go.pbm
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/images/src/stop.pbm' -o images/src/stop.pbm
```

The OLED display is used to display 2 images for obstacle detection (_Stop & Go_). Therefor 2x `*.pbm` images and 1x driver module are required in addition to the example script.

> [Source Code](../examples/sensors/laser_sensor_10929.py) for example `laser_sensor_10929.py`
> 
> [Source Code](../lib/ssd1306.py) for module `ssd1306.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy images into /pyboard/ directory
/your/current/path> cp images/src/go.pbm /pyboard/
/your/current/path> cp images/src/stop.pbm /pyboard/

# copy script as main.py
/your/current/path> cp examples/sensors/laser_sensor_10929.py /pyboard/main.py

# copy module file into /pyboard/lib/
/your/current/path> cp lib/ssd1306.py /pyboard/lib/

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

**Example**

![light_barrier.jpg](../images/modules/light_barrier.jpg)

### Pinout table

Here you can see the respective wiring for the circuit.

| Light Barrier | ESP32 |
|---------------|-------|
| +5V           | 5V5   |
| GND           | GND   |
| OUT           | 23    |

### Code

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/allnet_B18_light_barrier.py
```

The microcontroller needs to have internet connection! Therefor you need to set the device in station mode via `boot.py`. You can reuse the example from [here](./004_wlan_tutorials.md).

> [Source Code](../examples/sensors/allnet_B18_light_barrier.py) for example `allnet_B18_light_barrier.py`
> 
> [Source Code](../examples/network/boot.py) for station setup `boot.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy script as main.py
/your/current/path> cp examples/sensors/allnet_B18_light_barrier.py /pyboard/main.py

# copy boot.py into /pyboard/
/your/current/path> cp examples/network/boot.py /pyboard/boot.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program and to leave the REPL, press keys `Control` + `x`.

## Environment Sensing (Bosh: BME680 - Web Server)

In this example, the measurement data of the BME680 are displayed in the browser.

### Requirements

- mandatory 1x Bosh Sensortec BME680 (_or similar_)
- few cables
- optional a breadboard

**Example**

![bme680.jpg](../images/modules/bme680.jpg)

### Pinout table

Here you can see the respective wiring for the circuit.

| BME680 | ESP32 |
|--------|-------|
| GND    | GND   |
| VCC    | 3V3   |
| SCL    | 22    |
| SDA    | 21    |

### Code

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/bosch_sensortec_bme680.py
```

The connection will be via WLAN (_access point mode_). For html a template is used. 

> [Source Code](../examples/sensors/bosch_sensortec_bme680.py) for example `bosch_sensortec_bme680.py`
> 
> [Source Code](../examples/sensors/template.htm) for template `template.htm`
>
> [Source Code](../lib/bme680.py) for module `bme680.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy script as main.py
/your/current/path> cp examples/sensors/bosch_sensortec_bme680.py /pyboard/main.py

# copy template.htm into /pyboard/
/your/current/path> cp examples/sensors/template.htm /pyboard/

# copy module file into /pyboard/lib/
/your/current/path> cp lib/bme680.py /pyboard/lib/

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program and to leave the REPL, press keys `Control` + `x`.

## Measure Distance (Pimoroni: VL53L1X - SSD1306)

In this example two I2C devices are used in the bus. With the sensor you can measure distances and show them on the display.

> If you don't know the HEX addresses, just use the [I2C scanner](./010_i2c_helper_tutorials.md) from one of the previous tutorials.

### Requirements

- mandatory 1x [Pimoroni](https://shop.pimoroni.com/products/vl53l1x-breakout) VL53L1X TOF (_or similar_)
- mandatory 1x I2C OLED (_SSD1306_)
- few cables
- optional a breadboard

**Example**

![vl53l1x.jpg](../images/modules/vl53l1x.jpg)

### Pinout table

Here you can see the respective wiring for the circuit.

| VL53L1X | SSD1306 | ESP32 |
|---------|---------|-------|
| GND     | GND     | GND   |
| VCC     | VCC     | 3V3   |
| SCL     | SCL     | 22    |  
| SDA     | SDA     | 21    |

> All connections of the circuit are connected in parallel.

### Code

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/pimoroni_vl53l1x.py
```

Two driver modules are needed! One for the sensor and a second for the display.

> [Source Code](../examples/sensors/pimoroni_vl53l1x.py) for example `pimoroni_vl53l1x.py`
> 
> [Source Code](../lib/vl53l1x.py) for module `lib/vl53l1x.py`
>
> [Source Code](../lib/ssd1306.py) for module `lib/ssd1306.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy script as main.py
/your/current/path> cp examples/sensors/pimoroni_vl53l1x.py /pyboard/main.py

# copy module files into /pyboard/lib/
/your/current/path> cp lib/vl53l1x.py /pyboard/lib/
/your/current/path> cp lib/ssd1306.py /pyboard/lib/

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program press keys `Control` + `c` and to leave the REPL, press keys `Control` + `x`.

> It can happen that there are problems with the `rshell` connection, simply prepare everything in the terminal and execute the command immediately after the USB connection. If that doesn't work either, interrupt the 3V power supply first.

## Temperature via WebBLE (Allnet: B38 Temp. Sensor)

Web Bluetooth (_WebBLE_) is an exciting advance in Bluetooth Low Energy (_BLE_) development. With less effort you can create awesome applications for example without any internet connection, LAN/WLAN technologies, server or heavy backend programming. Also, (_for IoT somehow important_) with less power consumption. Here now a very basic example.

### Requirements

- mandatory 1x temperature sensor (_Allnet: B38 Temperature Sensor_)
- mandatory 1x device with Google Chrome Browser (_with [WebBLE](https://developer.chrome.com/articles/bluetooth/) support_)
- few cables
- optional a breadboard

**Example**

![temperature_sensor.jpg](../images/modules/temperature_sensor.jpg)

### Pinout table

Here you can see the respective wiring for the circuit.

| B38 | ESP32 |
|-----|-------|
| GND | GND   |
| +5V | V5    |
| SCL | 22    |  
| SDA | 21    |

### Code

```shell
# create local script
$ touch ~/Projects/ESP/examples/sensors/allnet_B38_temperature.py

# create local html
$ touch ~/Projects/ESP/examples/sensors/webBLE.htm
```

One helper module and an HTML page is needed! The HTML page stays at the device where Bluetooth is enabled and Google Chrome browser is installed.

> [Source Code](../examples/sensors/allnet_B38_temperature.py) for example `allnet_B38_temperature.py`
> 
> [Source Code](../lib/ble_advertising.py) for helper module `lib/ble_advertising.py`
> 
> [Source Code](../examples/sensors/webBLE.htm) for local `webBLE.htm`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy script as main.py
/your/current/path> cp examples/sensors/allnet_B38_temperature.py /pyboard/main.py

# copy module file into /pyboard/lib/
/your/current/path> cp lib/ble_advertising.py /pyboard/lib/

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To stop the program press keys `Control` + `c` and to leave the REPL, press keys `Control` + `x`.

> Enable `Bluetooth` on the device and open the HTML `webBLE.htm` inside Google Chrome. Press `Connect to device` button. Select the `ESP32` and wait for few seconds.

**Helpful Chrome URLs**

- [chrome://bluetooth-internals/#adapter](chrome://bluetooth-internals/#adapter) to connect without HTML `webBLE.htm` example
- [chrome://flags](chrome://flags) to enable "Experimental Web Platform features"

[Home](https://github.com/Lupin3000/ESP) | [Previous](./014_sensor_tutorials.md) | [Next](./015_game_tutorials.md)
