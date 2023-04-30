# Learn MicroPython with ESP8266/ESP32 microcontroller

## Very Important

The author of this repository (_information, scripts, code_) take no responsibility for your use or misuse (_or any damage to your devices_)! Respect the law in your country/location/area! The information included at this repository is for educational purposes only!

## Information

On [wokwi](https://wokwi.com) you can test mostly all scripts and simulate your circuit/code inside the browser. 

> Depending on your ESP microcontroller device, sensors and environment you may need to adapt values for GPIO pins. The important values are defined as constants after imports.

## Tutorials & examples

### Table of Contents

- Introduction
  - [Setup local environment](./doc/001_local_environment.md)
  - [Micropython firmware](./doc/002_firmware.md)
  - [Serial connection](./doc/003_serial_connection.md)
  - [MicroPython REPL](./doc/004_python_repl.md)
  - [MicroPython frozen code](./doc/005_frozen_code.md)
    - (code example) [Frozen code](./examples/mpy/example_module.py) 
- Board
  - [Board tutorial](./doc/006_board_tutorials.md)
    - (code example) [ESP32 board information](./examples/board/esp32_information.py)
    - (code example) [ESP32 disc space and memory information](./examples/board/esp32_memory.py)
- WLAN
  - [WLAN tutorial](./doc/007_wlan_tutorials.md)
    - (code example) [Access point scanner](./examples/wlan/ap_scanner.py)
    - (code example) [Simple station mode](./examples/wlan/simple_station.py)
    - (code example) [Open access point mode](./examples/wlan/open_access_point.py)
    - (code example) [WP2 access point mode](./examples/wlan/wp2_access_point.py)
- Bluetooth Low Energy
  - [Bluetooth Low Energy tutorial](./doc/008_bluetooth_tutorials.md)
    - (code example) [BLE scanner](./examples/ble/ble_scanner.py)
    - (code example) [Own BLE service](./examples/ble/ble_service.py)
- GPIO basic
  - [GPIO basic tutorial](./doc/009_gpio_basic_tutorials.md)
    - (code example) [Blink a single LED](./examples/gpio_basic/blink_single_led_high_low.py)
    - (code example) [Blink a single LED with PWM](./examples/gpio_basic/blink_single_led_high_low_pwm.py)
    - (code example) [Blink a single LED with Timer](./examples/gpio_basic/blink_single_led_high_low_timer.py)
    - (code example) [Fade a single LED with PWM](./examples/gpio_basic/fade_single_led_high_low.py)
    - (code example) [Change RGB LED color](./examples/gpio_basic/change_rgb_led_color_high_low.py)
- Sound
  - [Sound tutorial](./doc/010_sound_tutorials.md)
    - (code example) [Create single tone (passive buzzer)](./examples/sound/passive_buzzer_simple.py)
    - (code example) [Create different tones (passive buzzer)](./examples/sound/passive_buzzer_tones.py)
    - (code example) [Play a song (passive buzzer)](./examples/sound/passive_buzzer_sound.py)
- Motor
  - [Motor tutorial](./doc/011_motor_tutorials.md)
    - (code example) [Control servo via duty](./examples/motor/servo_duty.py)
    - (code example) [Control servo via duty_ns](./examples/motor/servo_duty_ns.py)
    - (code example) [Control servo via duty_u16](./examples/motor/servo_duty_u16.py)
- NeoPixel
  - [NeoPixel tutorial](./doc/012_neopixel_tutorials.md)
    - (code example) [NeoPixel basics](./examples/neopixel/neopixel_basics.py)
    - (code example) [NeoPixel morse code](./examples/neopixel/neopixel_morse.py)
- More introduction
  - [Package management](./doc/013_package_management.md)
  - [I2C helper tutorial](./doc/014_i2c_helper_tutorials.md)
    - (code example) [I2C scanner](./examples/i2c_helper/i2c_scanner.py) 
- Displays
  - [Display tutorial](./doc/015_display_tutorials.md)
    - (code example) [I2C OLED (ssd1306) basics](./examples/display/i2c_oled_ssd1306_basics.py)
    - (code example) [I2C OLED (ssd1306) date/time](./examples/display/i2c_oled_ssd1306_time.py)
- Network
  - [Network tutorial](./doc/016_network_tutorials.md)
    - (code example) [Time synchronisation with NTP](./examples/network/time_synchronisation_ntp.py)
    - (code example) [DNS resolve](./examples/network/dns_resolve.py)
    - (code example) [HTTP status](./examples/network/http_status.py)
    - (code example) [REST API](./examples/network/rest_api.py)

## external libraries

Display
- [SSD1306 driver](./lib/ssd1306.py)
- [Writer module](./lib/writer.py)
- [freesans20 font](./lib/freesans20.py)

Sensors
- [BME680 driver](./lib/bme680.py)
- [Vl53L1X driver](./lib/vl53l1x.py)

### IN PROGRESS (_to be refactored_)

- LED
  - [LED: Switch 1x ON/OFF by button](./Tutorials/LED/one_single_led_btn.py)
  - [LED: Switch 1x ON/OFF by touch](./Tutorials/LED/one_single_led_touch.py)
  - [LED: Switch 3x ON/OFF by touch](./Tutorials/LED/three_single_led_touch.py)
  - [LED: Heartbeat](./Tutorials/LED/one_single_led_heartbeat.py)
  - [RGB LED: Fade 1x ON/OFF](./Tutorials/LED/one_rgb_led_fade.py)
  - [NeoPixel: (simple)](./Tutorials/LED/neopixel_simple.py)
  - [NeoPixel: (matrix)](./Tutorials/LED/neopixel_matrix.py)
- Sensors
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
- Timer
  - [Virtual timers (cli only)](./Tutorials/TIMER/timer_cli.py)
- Server
  - [Webserver: WLAN access point mode](./Tutorials/SERVER/ap_time_info.py)
  - [Webserver: WLAN station mode - control LED](./Tutorials/SERVER/fade_led_on_off.py)
  - [WLAN: Webserver](./Tutorials/SERVER/wlan_webserver_station_mode.py)
