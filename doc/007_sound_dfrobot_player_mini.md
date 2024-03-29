# DFRobot Player Mini (DFR0299)

## Table of Contents

- [Prolog](#prolog)
- [Important notes](#important-notes)
- [Folder and file structure](#folder-and-file-structure)
- [Next/previous track](#nextprevious-track)

## Prolog

Even if MicroPython has now integrated the I2S protocol natively, it can be much easier to use the 'DFRobot Player Mini' module. The advantage is that this module comes with an SD card memory slot and the sound files are stored there. In addition, you can control it very easily via UART and do not have to worry about decoding.

## Important notes

- SD card should be in format FAT16 or FAT32 (_max 32 GB_)
- Power supply 3.3 V till 5V
- Serial TX/RX baud rate is 9600
- 1 kOhm resistor is recommended before the RX input
- Speaker up to 3W
- Supported sampling rates are 8/11.025/12/16/22.05/24/32/44.1/48 kHz
- only MP3 and WMA filetypes supported
- 24 -bit DAC output for dynamic range 90dB / SNR support for 85dB
- Sound channel: Mono

**Example**

![dfrobot_player_mini.png](../images/modules/dfrobot_player_mini.png)

### Few more online information

- [Product page](https://www.dfrobot.com/product-1121.html)
- [Wiki](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)

## Folder and file structure

> After starting, the module needs a few seconds to read the files as tracks from the SD card. The more files there are on the card, the longer this process can take! Take this time into account in your MicroPython code.

### Main directory (not recommended)

- max. 3000 mp3 files (_but not all can be used_)
- filenames: `0001.mp3`, `0002.mp3` till `0255.mp3`
- no track order by names (_that's why it's not recommended_)

### MP3 directory (recommended)

- folder name must be: `MP3`
- filenames: `0001.mp3`, `0002.mp3` till `3000.mp3`
- max. 3000 mp3 files
- track order by file names

### ADVERT directory

- folder name must be: `ADVERT`
- filenames: `0001.mp3`, `0002.mp3` till `3000.mp3`
- max. 3000 mp3 files
- new song interrupt current playing song, after they finish the previous song continue

### Standard directories (recommended)

- folder names must be: `01`, `02` till `99` (_max. 99 directories_)
- filenames per folder: `001.mp3`, `002.mp3` till `255.mp3` or `001xxx.mp3` (_example: 001_my_song.mp3_)
- track order by file names

### Hidden files and folders

All hidden files and directories should be deleted! Otherwise, they also are counted as tracks!

```shell
# list all files (optional)
$ ls -la /Volumes/MUSIC/

# delete apple double files (macos)
$ dot_clean -m /Volumes/[NAME]
```

> To delete hidden macOS directories `.Spotlight-V100`, `.Trashes` and `.fseventsd`, I recommend to use any other OS like Linux.

## Next/previous track

This is about switching between different tracks. As soon as one of the two buttons is pressed, the current track should stop and one of the next ones should start.

> If you haven't had any experience with buttons before, check out this [information](./013_human_interaction_tutorials.md) first.

### Requirements

- mandatory 1x DFPlayer Mini (_incl. 5 mp3 tracks_)
- mandatory 1x Speaker (_Piezo Speaker or any other what meets requirements_)
- mandatory 2x buttons 
- few cables
- optional breadboard

**Example**

![piezo_speaker.png](../images/modules/piezo_speaker.png)

> Be careful not to mix up the piezo speaker with the piezo buzzer! Both look very similar.

### Pinout table

| ESP32         | DFPlayer Mini | Speaker | Button         |
|---------------|---------------|---------|----------------|
| 3.3V          | VCC           | -       | -              |
| GND           | GND           | -       | OUT (BTN Both) |
| GPIO 17 (TX2) | RX            | -       | -              |
| GPIO 16 (RX2) | TX            | -       | -              |
| -             | SPK_1         | IN      | -              |
| -             | SPK_2         | OUT     | -              |
| GPIO 22       | -             | -       | IN (BTN NEXT)  |
| GPIO 23       | -             | -       | IN (BTN PREV)  |

> On many boards the pins GPIO 1 (_TX0_), GPIO 2 (_RX0_), GPIO 10 (_TX1_) and GPIO (_RX1_) cannot be used for UART connection!

### Code

```shell
# create local script
$ touch ~/Projects/ESP/examples/sound/dfplayer_control.py
```

> [Source Code](../examples/sound/dfplayer_control.py) for example `dfplayer_control.py`
> 
> [Source Code](../lib/dfplayermini.py) for module `dfplayermini.py`

Check your circuit careful, connect the microcontroller and copy needed files to the microcontroller.

```shell
# connect via rshel
(venv) $ rshell -p [SERIAL-PORT]

# copy module file into /pyboard/lib/
/your/current/path> cp lib/dfplayermini.py /pyboard/lib/

# copy script as main.py
/your/current/path> cp examples/sound/dfplayer_control.py /pyboard/main.py

# start repl
/your/current/path> repl
```

Start with keys `Control` + `d` or press `reset` key. To leave the REPL, press keys `Control` + `x`.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./007_sound_tutorials.md) | [Next](./008_motor_tutorials.md)
