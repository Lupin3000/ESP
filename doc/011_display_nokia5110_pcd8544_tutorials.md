# Display Nokia 5110 (pcd8544)

## Table of Contents

- [Prolog](#prolog)
- [SPI LCD basics (ssd1306)](#spi-lcd-basics-ssd1306)

## Prolog

The Nokia 5110 LCD display comes with  84x48 monochrome pixels. It's a very cheap display and connected via SPI (_6 cables but one-way only_).  

## SPI LCD basics (ssd1306)

It took me a while to find the proper connection, but after few minutes of reading different online resources I was successful. Also the initial basic example of [GitHub](https://github.com/mcauser/micropython-pcd8544) page was on a first view, some confusing. I hope that you will get started much faster with the following example!

### Requirements

- mandatory Nokia 5110 display
- few cables
- optional breadboard

### Connection/Wiring

On NodeMCU-ESP32 following connection is used:

| Nokia 5110 | ESP32          |
|------------|----------------|
| Pin RST    | GPIO 14        |
| Pin CE     | GPIO 05 (SS)   |
| Pin DC     | GPIO 19 (Miso) |
| Pin DIN    | GPIO 23 (Mosi) |
| Pin CLK    | GPIO 18 (SCK)  |
| Pin VCC    | 3.3V (3V3)     |
| Pin BL     | GPIO 12        |
| Pin GND    | GND            |

> Check the pinout for your ESP32, it can be slightly different!
> 
> If you use 5V instead of 3.3V, you need limiting resistor (_min. 220 ohms_) for Backlight `Pin: BL`!

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/display/spi_lcd_nokia5110_pcd8544.py

# download pcd8544
$ curl -L 'https://raw.githubusercontent.com/mcauser/micropython-pcd8544/master/pcd8544.py' -o lib/pcd8544.py
```

> [Source Code](../examples/display/spi_lcd_nokia5110_pcd8544.py) for `spi_lcd_nokia5110_pcd8544.py`

Check your circuit (_adapt pins if needed via constants_) and copy the driver as `/pyboard/lib/pcd8544.py` and the script to the microcontroller as `/pyboard/main.py`.

```shell
# connect to ESP32
(venv) $ rshell -p [SERIAL-PORT] 

# copy pcd8544 driver
/your/current/path> cp lib/pcd8544.py /pyboard/lib/

# copy example as main.py
/your/current/path> cp examples/display/spi_lcd_nokia5110_pcd8544.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d`. Stop the loop with keys `Control` + `c`. To leave the REPL, press keys `Control` + `x`.

> To convert your image into bytes, use this free [service](https://sparks.gogo.co.nz/pcd8554-bmp.html).

[Home](https://github.com/Lupin3000/ESP) | [Previous](./011_display_ssd1306_tutorials.md) | [Next](./011_display_sh1106_tutorials.md)
