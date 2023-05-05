# Learn MicroPython with ESP32 microcontroller

[![Static](https://img.shields.io/badge/Microcontroller-ESP32-green)](https://www.espressif.com)
[![Static](https://img.shields.io/badge/Language-MicroPython_1.20.0-green)](https://github.com/micropython)
[![Static](https://img.shields.io/badge/Status-In_Progress-red)](https://github.com/Lupin3000/ESP)

## Very Important

The author of this repository (_information, scripts, code_) take no responsibility for your use or misuse (_or any damage to your devices_)! Respect the law in your country/location/area! The information included at this repository is for educational purposes only!

## Information

> Depending on your `ESP32` microcontroller device, sensors and environment you may need to adapt values for GPIO pins. The important values are defined as constants after imports. Many of the examples also run on the `ESP8266`, you have to adjust the pins here too!

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
    - :page_facing_up: [Frozen code](./examples/mpy/example_module.py) 
- 003 - Board information
  - [Board tutorial](./doc/003_board_tutorials.md)
    - (code example) [ESP32 board information](./examples/board/esp32_information.py)
    - (code example) [ESP32 disc space and memory information](./examples/board/esp32_memory.py)
- 004 - WLAN
  - [WLAN tutorial](./doc/004_wlan_tutorials.md)
    - (code example) [Access point scanner](./examples/wlan/ap_scanner.py)
    - (code example) [Simple station mode](./examples/wlan/simple_station.py)
    - (code example) [Open access point mode](./examples/wlan/open_access_point.py)
    - (code example) [WP2 access point mode](./examples/wlan/wp2_access_point.py)
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
    - (code example) [Create single tone (passive buzzer)](./examples/sound/passive_buzzer_simple.py)
    - (code example) [Create different tones (passive buzzer)](./examples/sound/passive_buzzer_tones.py)
    - (code example) [Play a song (passive buzzer)](./examples/sound/passive_buzzer_sound.py)
- 008 - Motor
  - [Motor tutorial](./doc/008_motor_tutorials.md)
    - (code example) [Control servo via duty](./examples/motor/servo_duty.py)
    - (code example) [Control servo via duty_ns](./examples/motor/servo_duty_ns.py)
    - (code example) [Control servo via duty_u16](./examples/motor/servo_duty_u16.py)
- 009 - NeoPixel
  - [NeoPixel tutorial](./doc/009_neopixel_tutorials.md)
    - (code example) [NeoPixel basics](./examples/neopixel/neopixel_basics.py)
    - (code example) [NeoPixel morse code](./examples/neopixel/neopixel_morse.py)
- 010 - More introduction
  - [Package management](./doc/010_package_management.md)
  - [I2C helper tutorial](./doc/010_i2c_helper_tutorials.md)
    - (code example) [I2C scanner](./examples/i2c_helper/i2c_scanner.py) 
- 011 - Displays
  - [Display tutorial](./doc/011_display_tutorials.md)
    - (code example) [I2C OLED (ssd1306) basics](./examples/display/i2c_oled_ssd1306_basics.py)
    - (code example) [I2C OLED (ssd1306) date/time and fonts](./examples/display/i2c_oled_ssd1306_time.py)
    - (code example) [Icons on OLED (ssd1306)](./examples/display/i2c_oled_ssd1306_icons.py)
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
    - (code example) [Potentiometer and SSD1306 OLED](./examples/user_input/potentiometer_display.py)
- 014 - Sensors
- 015 - Games

## external libraries

Display
- [SSD1306 driver](./lib/ssd1306.py)
- [Writer module](./lib/writer.py)
- [freesans20 font](./lib/freesans20.py)

Sensors
- [BME680 driver](./lib/bme680.py)
- [Vl53L1X driver](./lib/vl53l1x.py)

NeoPixel
- [NeoPixel-Ring module](./lib/neopixelring.py)

### IN PROGRESS (_to be refactored_)

- LED
  - [LED: Switch 1x ON/OFF by touch](Tutorials/one_single_led_touch.py)
  - [LED: Switch 3x ON/OFF by touch](Tutorials/three_single_led_touch.py)
  - [NeoPixel: (matrix)](Tutorials/neopixel_matrix.py)
  - [Webserver: WLAN station mode - control LED](Tutorials/fade_led_on_off.py)
- Sensors
  - [IR Flame detection](./examples/sensors/ir_flame_detection.py)
  - [Light/Shadow detection with LED](./examples/sensors/shadow_detection.py)
  - [DHT11 Temperature/Humidity measure](./examples/sensors/dht11.py)
  - [PIR Motion detection](./examples/sensors/pir.py)
  - [HC-SR04 Distance measure](./examples/sensors/hcsr04.py)
  - [ALLNET: B38 Temperature I2C Sensor](./examples/sensors/allnet_B38_temperature.py)
  - [ALLNET: B18 Light Barrier Sensor](./examples/sensors/allnet_B18_light_barrier.py)
  - [ALLNET: B08 Touch Sensor](./examples/sensors/allnet_B08_touch.py)
  - [WaveShare: Laser Sensor](./examples/sensors/LaserSensor10929.py)
  - [Pimoroni: VL53L1X TOF Sensor](./examples/sensors/pimoroni_vl53l1x.py)
  - [Adafruit: MAX9814](./examples/sensors/max9814.py)
  - [Bosh: Sensortec BME680](./examples/sensors/bosch_sensortec_bme680.py)
