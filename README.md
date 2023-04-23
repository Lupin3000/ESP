# Learn MicroPython with ESP8266/ESP32 microcontroller

## Very Important

The author of this repository (_information, scripts, code_) take no responsibility for your use or misuse (_or any damage of your devices_)! Respect the law in your country/location/area! The information included at this repository is for educational purposes only!

## Information

To make it easier to get started, the basic examples are not object-oriented. On [wokwi](https://wokwi.com) you can test mostly all scripts and simulate your circuit/code inside the browser. Depending on your ESP microcontroller device, sensors and environment you may need to adapt values for GPIO pins. The important values are defined as constants after imports.

## Table of Contents

- Introduction
  - [Setup local environment](./doc/001_local_environment.md)
  - [Micropython firmware](./doc/002_firmware.md)
  - [Serial connection](./doc/003_serial_connection.md)
  - [MicroPython REPL](./doc/004_python_repl.md)
  - [MicroPython frozen code](./doc/005_frozen_code.md)
- Board
  - [Board tutorial](./doc/006_board_tutorials.md)
    - (code) [ESP32 board information](./examples/board/esp32_information.py)
    - (code) [ESP32 disc space and memory information](./examples/board/esp32_memory.py)
- WLAN
  - [WLAN tutorial](./doc/007_wlan_tutorials.md)
    - (code) [Access Point Scanner](./examples/wlan/ap_scanner.py)
    - (code) [Simple Station Mode](./examples/wlan/simple_station.py)
    - (code) [Open Access Point Mode](./examples/wlan/open_access_point.py)
    - (code) [WP2 Access Point Mode](./examples/wlan/wp2_access_point.py)
- LED (_[some help](./Tutorials/LED/help.md)_)
  - [LED: Blink 1x ON/OFF](./Tutorials/LED/one_single_led_blink.py)
  - [LED: Fade 1x ON/OFF](./Tutorials/LED/one_single_led_fade.py)
  - [LED: Switch 1x ON/OFF by button](./Tutorials/LED/one_single_led_btn.py)
  - [LED: Switch 1x ON/OFF by touch](./Tutorials/LED/one_single_led_touch.py)
  - [LED: Switch 3x ON/OFF by touch](./Tutorials/LED/three_single_led_touch.py)
  - [LED: Heartbeat](./Tutorials/LED/one_single_led_heartbeat.py)
  - [RGB LED: Blink 1x ON/OFF](./Tutorials/LED/one_rgb_led_blink.py)
  - [RGB LED: Fade 1x ON/OFF](./Tutorials/LED/one_rgb_led_fade.py)
  - [NeoPixel: (simple)](./Tutorials/LED/neopixel_simple.py)
  - [NeoPixel: (advanced)](./Tutorials/LED/neopixel_advanced.py)
  - [NeoPixel: (morse code)](./Tutorials/LED/neopixel_morse.py)
  - [NeoPixel: (matrix)](./Tutorials/LED/neopixel_matrix.py)
- Sound (_[some help](./Tutorials/SOUND/help.md)_)
  - [Passive Buzzer: play single tone](./Tutorials/SOUND/passive_buzzer_simple.py)
  - [Passive Buzzer: play many tones](./Tutorials/SOUND/passive_buzzer_tones.py)
  - [Passive Buzzer: play song](./Tutorials/SOUND/passive_buzzer_sound.py)
- Sensors (_[some help](./Tutorials/SENSORS/help.md)_)
  - [ESP32: I2C scanner](./Tutorials/BOARD/i2c_scan.py)
  - [IR Flame detection](./Tutorials/SENSORS/ir_flame_detection.py)
  - [Light/Shadow detection with LED](./Tutorials/SENSORS/shadow_detection.py)
  - [DHT11 Temperature/Humidity measure](./Tutorials/SENSORS/dht11.py)
  - [PIR Motion detection](./Tutorials/SENSORS/pir.py)
  - [HC-SR04 Distance measure](./Tutorials/SENSORS/hcsr04.py)
  - [ALLNET: B38 Temperature I2C Sensor](./Tutorials/SENSORS/allnet_B38_temperature.py)
  - [ALLNET: B18 Light Barrier Sensor](./Tutorials/SENSORS/allnet_B18_light_barrier.py)
  - [ALLNET: B08 Touch Sensor](./Tutorials/SENSORS/allnet_B08_touch.py)
  - [WaveShare: Laser Sensor](./Tutorials/SENSORS/LaserSensor10929.py)
  - [Pimoroni: VL53L1X TOF Sensor](./Tutorials/SENSORS/pimoroni_vl53l1x.py)
  - [Adafruit: MAX9814](./Tutorials/SENSORS/max9814.py)
  - [Bosh: Sensortec BME680](./Tutorials/SENSORS/bosch_sensortec_bme680.py) 
- Motor (_[some help](./Tutorials/MOTOR/help.md)_)
  - [Servo Motor (90°): control via duty](./Tutorials/MOTOR/servo_duty.py)
  - [Servo Motor (90°): control via duty_ns](./Tutorials/MOTOR/servo_duty_ns.py)
  - [Servo Motor (90°): control via duty_u16](./Tutorials/MOTOR/servo_duty_u16.py)
- Timer
  - [Virtual timers (cli only)](./Tutorials/TIMER/timer_cli.py)
  - [Blink a single LED ON/OFF](./Tutorials/TIMER/blink_single_led.py)
- WIFI
  - [WLAN: Get target IP](./Tutorials/WiFi/wlan_get_target_ip.py)
  - [WLAN: HTTP Status code](./Tutorials/WiFi/wlan_get_http_status.py)
  - [WLAN: NTP time synchronisation](./Tutorials/WiFi/wlan_ntp_time.py)
  - [WLAN: Webserver](./Tutorials/WiFi/wlan_webserver_station_mode.py)
- Bluetooth Low Energy (_[some help](./Tutorials/BLE/help.md)_)
  - [BLE: Device scanner](./Tutorials/BLE/ble_scan.py)
  - [BLE: Advertiser](./Tutorials/BLE/ble_advertiser.py)
  - [BLE: Services](./Tutorials/BLE/ble_service.py)
- Server
  - [Webserver: WLAN access point mode](./Tutorials/SERVER/ap_time_info.py)
  - [Webserver: WLAN station mode - control LED](./Tutorials/SERVER/fade_led_on_off.py)

## Classes & Drivers

> The 'drivers' are just copied from internet

- [BLE Advertiser](./classes/ble_advertiser.py)
- [NeoPixel Ring](./classes/neopixelring.py)
- [VL53L1X](./driver/vl53l1x.py)
- [BME680](./driver/bme680.py)
