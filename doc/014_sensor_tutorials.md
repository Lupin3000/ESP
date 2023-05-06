# Sensors

## Table of Contents

- [Prolog](#prolog)
- [Temperature/Humidity sensor (DHT11/DHT22)](#temperaturehumidity-sensor-dht11dht22)
- [PIR sensor (HC-SR501)](#pir-sensor-hc-sr501)
- [Ultrasonic sensor (HC-SR04)](#ultrasonic-sensor-hc-sr04)

## Prolog

After the many previous examples, it is time to measure and collect data from the environment. Sensors are required for this. Depending on what is to be measured, special sensors are used. But there are also sensors that record several environmental variables!

## Temperature/Humidity sensor (DHT11/DHT22)

With the `DHT11/DHT22` you can record the temperature and humidity. The respective modules for both are already integrated in the standard firmware of MicroPython.


| Device | Delay  | Temperature  | Humidity   |
|--------|--------|--------------|------------|
| DHT11  | 1 sec. | 0 to 50 °C   | 20 to 90%  |
| DHT22  | 2 sec. | -40 to 80 °C | 0 to 100%  |

### Requirements

- mandatory 1x DHT11/DHT22 Sensor
- mandatory 1x Resistor (_min. 10 kilo ohms_)
- few cables
- optional breadboard

### Circuit

![014_circuit_diagram_dht22.png](../images/examples/014_circuit_diagram_dht22.png)

### Code

> You can use the same source code and circuit diagram for `DHT11` and `DHT22`! Only the import  and object must adapted for specific device.

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP/examples/sensors

# create script
$ touch ~/Projects/ESP/examples/sensors/dht11.py
```

> [Source Code](../examples/sensors/dht11.py) for `dht11.py`

Check your circuit and copy the script to the microcontroller as `main.py`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/sensors/dht11.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d`. Stop the loop with keys `Control` + `c`. To leave the REPL, press keys `Control` + `x`.

## PIR sensor (HC-SR501)

If you want to detect movements in the area, the PIR sensor is already suitable. The sensors are available in various variants. 

### Requirements

- mandatory PIR Sensor (_HC-SR501_)
- few cables
- optional breadboard

### Circuit

![014_circuit_diagram_pir.png](../images/examples/014_circuit_diagram_pir.png)

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/sensors/pir.py
```

> [Source Code](../examples/sensors/pir.py) for `pir.py`

Check your circuit and copy the script to the microcontroller as `main.py`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/sensors/pir.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d`. Stop the loop with keys `Control` + `c`. To leave the REPL, press keys `Control` + `x`.


## Ultrasonic sensor (HC-SR04)

There are various ways of measuring the distance to objects. Depending on the area of application and the environment, they have strengths and weaknesses. Here is a sensor that uses ultrasound.

### Requirements

- mandatory Ultrasonic Sensor (_HC-SR04_)
- few cables
- optional breadboard

### Circuit

![014_circuit_diagram_hcsr04.png](../images/examples/014_circuit_diagram_hcsr04.png)

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/sensors/hcsr04.py
```

> [Source Code](../examples/sensors/hcsr04.py) for `hcsr04.py`

Check your circuit and copy the script to the microcontroller as `main.py`.

```shell
# copy file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/sensors/hcsr04.py /pyboard/main.py

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Start with keys `Control` + `d`. Stop the loop with keys `Control` + `c`. To leave the REPL, press keys `Control` + `x`.


[Home](https://github.com/Lupin3000/ESP) | [Previous](./013_human_interaction_tutorials.md) | [Next]()
