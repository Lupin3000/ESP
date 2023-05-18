# Learn MicroPython with ESP32 microcontroller

[![Static](https://img.shields.io/badge/Microcontroller-ESP32-green)](https://www.espressif.com)
[![Static](https://img.shields.io/badge/Language-MicroPython_1.20.0-green)](https://github.com/micropython)
[![Static](https://img.shields.io/badge/Status-In_Progress-red)](https://github.com/Lupin3000/ESP)

## Very Important

The author of this repository (_information, scripts, code_) take no responsibility for your use or misuse (_or any damage to your devices_)! Respect the law in your country/location/area! The information included at this repository is for educational purposes only!

## Information

> Depending on your `ESP32` microcontroller device, sensors and environment you may need to adapt values for GPIO pins. The important values are defined as constants after imports. Many of the examples also run on the `ESP8266`, `RP2040` / `Pico` or other MicroPython compatible devices, you have to adjust the pins!

> If you do not yet own an ESP32 microcontroller or are unsure about your circuit, on [wokwi](https://wokwi.com) you can test mostly all scripts and simulate your circuit/code inside the browser.

## Tutorials & examples

### Table of Contents

- 001 - Introduction
  - [Setup local environment](./doc/001_local_environment.md)
  - [Micropython firmware](./doc/001_firmware.md)
  - [Serial connection](./doc/001_serial_connection.md)
  - [MicroPython REPL](./doc/001_python_repl.md)
- 002 - Frozen Code
  - [MicroPython frozen code](./doc/002_frozen_code.md)
    - (code example) [Frozen code](./examples/mpy/example_module.py) 
- 003 - Board information
  - [Board tutorial](./doc/003_board_tutorials.md)
    - (code example) [ESP32 board information](./examples/board/esp32_information.py)
    - (code example) [ESP32 disc space and memory information](./examples/board/esp32_memory.py)
- 004 - WLAN
  - [WLAN tutorial](./doc/004_wlan_tutorials.md)
    - (code example) [Access point scanner](./examples/wlan/ap_scanner.py)
    - (code example) [Simple station mode](./examples/wlan/simple_station.py)
    - (code example) [Open access point mode](./examples/wlan/open_access_point.py)
    - (code example) [WPA access point mode](./examples/wlan/wpa_access_point.py)
- 005 - Bluetooth Low Energy
  - [Bluetooth Low Energy tutorial](./doc/005_bluetooth_tutorials.md)
    - (code example) [BLE scanner](./examples/ble/ble_scanner.py)
    - (code example) [Own BLE service](./examples/ble/ble_service.py)
- 006 - GPIO basic
  - [GPIO basic tutorial](./doc/006_gpio_basic_tutorials.md)
    - (code example) [Blink a single LED](./examples/gpio_basic/blink_single_led_high_low.py)
    - (code example) [Blink a single LED with PWM](./examples/gpio_basic/blink_single_led_high_low_pwm.py)
    - (code example) [Blink a single LED with Timer](./examples/gpio_basic/blink_single_led_high_low_timer.py)
    - (code example) [Fade a single LED with PWM](./examples/gpio_basic/fade_single_led_high_low.py)
    - (code example) [Heartbeat a single LED with PWM](./examples/gpio_basic/heartbeat_single_led.py)
    - (code example) [Change RGB LED color](./examples/gpio_basic/change_rgb_led_color_high_low.py)
- 007 - Sound
  - [Sound tutorial](./doc/007_sound_tutorials.md)
    - (code example) [Create single tone (Passive piezo buzzer)](./examples/sound/passive_buzzer_simple.py)
    - (code example) [Create different tones (Passive piezo buzzer)](./examples/sound/passive_buzzer_tones.py)
    - (code example) [Play a song (Passive piezo buzzer)](./examples/sound/passive_buzzer_sound.py)
- 008 - Motor
  - [Motor tutorial](./doc/008_motor_tutorials.md)
    - (code example) [Control servo via duty](./examples/motor/servo_duty.py)
    - (code example) [Control servo via duty_ns](./examples/motor/servo_duty_ns.py)
    - (code example) [Control servo via duty_u16](./examples/motor/servo_duty_u16.py)
- 009 - NeoPixel
  - [NeoPixel tutorial](./doc/009_neopixel_tutorials.md)
    - (code example) [NeoPixel basics](./examples/neopixel/neopixel_basics.py)
    - (code example) [NeoPixel morse code](./examples/neopixel/neopixel_morse.py)
  - [NeoPixel extended](./doc/009_neopixel_extended.md)
    - (code example) [NeoPixel Matrix example](./examples/neopixel/neopixel_matrix.py)
    - (code example) [NeoPixel Matrix icons](./examples/neopixel/neopixel_matrix_icon.py)
    - (code example) [NeoPixel Matrix bounce](./examples/neopixel/neopixel_matrix_bounce.py)
- 010 - More introduction
  - [Package management](./doc/010_package_management.md)
  - [I2C helper tutorial](./doc/010_i2c_helper_tutorials.md)
    - (code example) [I2C scanner](./examples/i2c_helper/i2c_scanner.py) 
- 011 - Displays
  - [OLED Display tutorial (SSD1306)](./doc/011_display_ssd1306_tutorials.md)
    - (code example) [I2C OLED basics (SSD1306)](./examples/display/i2c_oled_ssd1306_basics.py)
    - (code example) [I2C OLED date/time and fonts (SSD1306)](./examples/display/i2c_oled_ssd1306_time.py)
    - (code example) [I2C OLED icons (SSD1306)](./examples/display/i2c_oled_ssd1306_icons.py)
  - [LCD Display tutorial Nokia 5110 (PCD8544)](./doc/011_display_nokia5110_pcd8544_tutorials.md)
    - (code example) [SPI LCD Nokia 5110 basics (PCD8544)](./examples/display/spi_lcd_nokia5110_pcd8544.py)
  - [OLED Display tutorial (SH1106)](./doc/011_display_sh1106_tutorials.md)
    - (code example) [SPI OLED basics (SH1106)](./examples/display/spi_oled_sh1106_basics.py)
- 012 - Network
  - [Network tutorial](./doc/012_network_tutorials.md)
    - (code example) [Time synchronisation with NTP](./examples/network/time_synchronisation_ntp.py)
    - (code example) [DNS resolve](./examples/network/dns_resolve.py)
    - (code example) [HTTP status](./examples/network/http_status.py)
    - (code example) [REST API](./examples/network/rest_api.py)
    - (code example) [HTML webserver](./examples/network/html_webserver.py)
- 013 - Human interaction
  - [Human interaction tutorial](./doc/013_human_interaction_tutorials.md)
    - (code example) [Button (Polling)](./examples/user_input/btn_led_polling.py)
    - (code example) [Button (Interrupt Handler)](./examples/user_input/btn_led_interrupt_handler.py)
    - (code example) [Button (Interrupt Handler and Debounce)](./examples/user_input/btn_led_interrupt_handler_debounce.py)
    - (code example) [Potentiometer](./examples/user_input/potentiometer.py)
    - (code example) [Potentiometer and OLED (SSD1306)](./examples/user_input/potentiometer_display.py)
    - (code example) [Joystick (XY + Button)](./examples/user_input/joystick.py)
  - [Human interaction extended](./doc/013_human_interaction_extended.md)
    - (code example) [Move crosshair via joystick (SH1106)](./examples/user_input/joystick_display.py) 
- 014 - Sensors
  - [Sensor tutorials](./doc/014_sensor_tutorials.md)
    - (code example) [Temperature/Humidity sensor (DHT11/DHT22)](./examples/sensors/dht11.py) 
    - (code example) [PIR sensor (HC-SR501)](./examples/sensors/pir.py)
    - (code example) [Ultrasonic sensor (HC-SR04)](./examples/sensors/hcsr04.py)
  - [Sensor extended](./doc/014_sensor_extended.md)
    - (code example) [Measure environment decibel (MAX9814 - SSD1306)](./examples/sensors/max9814.py)
    - (code example) [Obstacle Detection (Laser Sensor - SSD1306)](./examples/sensors/laser_sensor_10929.py)
    - (code example) [Light Barrier (ALLNET: B18 - Pushover)](./examples/sensors/allnet_B18_light_barrier.py)
    - (code example) [Environment Sensing (Bosh: BME680 - Web Server)](./examples/sensors/bosch_sensortec_bme680.py)
- 015 - Games
  - [Game tutorials](./doc/015_game_tutorials.md)
    - (code example) [Crazy Car Racer (SSD1306)](./examples/games/racer.py)
    - (code example) [Space Invaders (PCD8544)](./examples/games/invader.py)
    - (code example) [Pong (NeoPixel Matrix)](./examples/games/pong.py)
    - (code example) [Snake (SH1106)](./examples/games/snake.py)

## External libraries

- Font
  - [freesans20](./lib/freesans20.py)
  - [vga bold 16x16](./lib/vga1_bold_16x16.py)
- Display
  - [SSD1306](./lib/ssd1306.py)
  - [PCD8544](./lib/pcd8544.py)
  - [Writer](./lib/writer.py)
  - [ST7789](./lib/st7789py.py)
  - [SH1106](./lib/sh1106.py)
- Sensors
  - [BME680](./lib/bme680.py)
  - [Vl53L1X](./lib/vl53l1x.py)
- NeoPixel
  - [NeoPixel-Matrix](./lib/neopixelmatrix.py)
- BLE
  - [BLE Advertising](./lib/ble_advertising.py) 

## Important MicroPython sources

- [MicroPython Website](https://micropython.org)
- [MicroPython Documentation](https://docs.micropython.org/en/latest/)
- [MicroPython Core Repository (GitHub)](https://github.com/micropython/micropython)
- [MicroPython Libraries Repository (GitHub)](https://github.com/micropython/micropython-lib)
- [MicroPython Discussions (GitHub)](https://github.com/orgs/micropython/discussions)
- [Awesome MicroPython](https://awesome-micropython.com)

## IN PROGRESS (_to be refactored_)

- Sensors
  - [IR Flame detection](./examples/sensors/ir_flame_detection.py)
  - [Light/Shadow detection with LED](./examples/sensors/shadow_detection.py)
  - [ALLNET: B38 Temperature I2C Sensor](./examples/sensors/allnet_B38_temperature.py)
  - [Pimoroni: VL53L1X TOF Sensor](./examples/sensors/pimoroni_vl53l1x.py)
