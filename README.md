# ESP

## Very Important

The author of this repository (_information, scripts, code_) take no responsibility for your use or misuse (_or any damage of your devices_)! Respect the law in your country/location/area! The information included at this repository is for educational purposes only!

## Information

To make it easier to get started, the basic examples are not object-oriented. On [wokwi](https://wokwi.com) you can test mostly all scripts and simulate your circuit/code inside the browser. Depending on your microcontroller device, sensors and environment you may need to adapt values for GPIO pins. The important values are defined as constants after imports.

## Table of Contents

- Introduction
  - [Setup](./Setup/README.md)
  - [RSHELL](./RSHELL/README.md)
  - [REPL](./REPL/README.md)
- Board
  - [ESP32 Board Information](./Tutorials/BOARD/esp32_info.py) 
  - [Show memory information](./Tutorials/BOARD/memory.py)
  - [List I2C devices](./Tutorials/BOARD/i2c_scan.py)
- LED's (_[Some help](./Tutorials/LED/help.md)_)
  - [Blink a single LED ON/OFF](./Tutorials/LED/one_single_led_blink.py)
  - [Fade a single LED ON/OFF](./Tutorials/LED/one_single_led_fade.py)
  - [Turn single LED ON/OFF with button](./Tutorials/LED/one_single_led_btn.py)
  - [Heartbeat a single LED ON/OFF](./Tutorials/LED/one_single_led_heartbeat.py)
  - [Blink a single RGB LED](./Tutorials/LED/one_rgb_led_blink.py)
  - [Fade a single RGB LED](./Tutorials/LED/one_rgb_led_fade.py)
  - [Touch single LED ON/OFF](./Tutorials/LED/one_single_led_touch.py)
  - [Touch 3 single LEDs ON/OFF](./Tutorials/LED/three_single_led_touch.py)
  - [NeoPixel LED Strip random colors](./Tutorials/LED/neopixel_sidelight_strip_simple.py)
  - [NeoPixel LED Strip color race](./Tutorials/LED/neopixel_sidelight_strip_race.py)
- Sensor's (_[Some help](./Tutorials/SENSORS/help.md)_)
  - [IR Flame detection](./Tutorials/SENSORS/ir_flame_detection.py)
  - [Light/Shadow detection with LED](./Tutorials/SENSORS/shadow_detection.py)
  - [Temperature/Humidity with DHT11](./Tutorials/SENSORS/dht11.py)
  - [Motion detection with PIR](./Tutorials/SENSORS/pir.py)
  - [Distance measure with HC-SR04](./Tutorials/SENSORS/hcsr04.py)
- Motor (_[Some help](./Tutorials/MOTOR/help.md)_)
  - [Servo Motor via duty](./Tutorials/MOTOR/servo_duty.py)
  - [Servo Motor via duty_ns](./Tutorials/MOTOR/servo_duty_ns.py)
  - [Servo Motor via duty_u16](./Tutorials/MOTOR/servo_duty_u16.py)
- WLAN
  - [Simple OPEN WLAN Access Point](./Tutorials/WiFi/wlan_access_point_mode_open.py)
  - [Simple WPA2 WLAN Access Point](./Tutorials/WiFi/wlan_access_point_mode_wp2.py)
  - [Simple WLAN Station](./Tutorials/WiFi/wlan_station_mode.py)
  - [Access Point Scanner (station mode)](./Tutorials/WiFi/access_point_scan.py)
- Network
  - [Get target IP (station mode)](./Tutorials/NETWORK/get_target_ip.py)
- Server
  - [Webserver (station mode)](./Tutorials/SERVER/webserver_station_mode.py)
  - [Webserver (access point mode)](./Tutorials/SERVER/ap_time_info.py)
  - [Fade LED via webpage (station mode)](./Tutorials/SERVER/fade_led_on_off.py)
