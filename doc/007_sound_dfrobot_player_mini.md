# DFRobot Player Mini

## Table of Contents

- [Prolog](#prolog)
- [Important notes](#important-notes)
- [Connection (ESP32 and speaker)](#connection-esp32-and-speaker)
- [Folder and file structure](#folder-and-file-structure)

## Prolog

Even if MicroPython has now integrated the I2S protocol natively, it can be much easier to use the 'DFRobot Player Mini' module. The advantage is that this module comes with an SD card memory slot and the sound files are stored there. In addition, you can control it very easily via UART and do not have to worry about decoding.

## Important notes

- SD card should be in format FAT16 or FAT32 (_max 32 GB_)
- Power supply 3.3 V till 5V
- Serial TX/RX baud rate is 9600
- 1 kOhm resistor is recommended before the RX input
- Speaker up to 3W
- Supported sampling rates are 8/11.025/12/16/22.05/24/32/44.1/48 kHz

## Connection (ESP32 and speaker)

| ESP32         | DFPlayer Mini | Speaker |
|---------------|---------------|---------|
| 3.3V          | VCC           | -       |
| GND           | GND           | -       |
| GPIO 17 (TX2) | RX            | -       |
| GPIO 16 (RX2) | TX            | -       |
| -             | SPK_1         | IN      |
| -             | SPK_2         | OUT     |    

> On many boards the pins GPIO 1 (_TX0_), GPIO 2 (_RX0_), GPIO 10 (_TX1_) and GPIO (_RX1_) cannot be used for UART connection!

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
- filenames per folder: `001.mp3`, `002.mp3` till `255.mp3` or `001xxx.mp3`
- track order by file names

### Hidden files and folders

All hidden files and directories should be deleted! Otherwise, they also are counted as tracks!

```shell
# list all files (optional)
$ ls -la /Volumes/MUSIC/

# elete apple double files (macos)
$ dot_clean -m /Volumes/[NAME]
```

> To delete hidden macos directories `.Spotlight-V100`, `.Trashes` and `.fseventsd`, I recommend to use any other OS like Linux.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./007_sound_tutorials.md) | [Next](./008_motor_tutorials.md)
