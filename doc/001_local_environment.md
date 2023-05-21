# Setup local environment

## Table of Contents

- [Local requirements](#local-requirements)
- [VCP driver](#vcp-driver)
- [Project preparation](#project-preparation)
- [Basic Python packages](#basic-python-packages)

## Local requirements

Here are the most important things you need to get started with Micropython/microcontrollers.

- ESP32 device(s)
- USB cable(s)
- Python 3.x locally installed (_minimum version 3.5_)
- Internet access

> Later you will also need various cables, active/passive components, possibly a breadboard, a display plus other devices and software. I will point this out to you in the relevant examples.

## VCP Driver

Depending on the operating system, you also need the CP210x USB to UART Bridge VCP drivers. You can download the free drivers for your operating system (_e.g. Linux, macOS or Windows_) from [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) and install them after a successful download.

Without these drivers, there may be difficulties in detecting and communicating with the ESP32 microcontroller via USB.

Depending on the operating system, a restart is recommended after successful installation of the VCP driver.

### Verify installation

You can now connect your ESP32 with the USB cable and the local device. Shortly after the connection you should find the microcontroller.

```shell
# get SERIAL-PORT (on macOS)
$ ls -l /dev/cu.usb*
$ ls -l /dev/tty.usb*

# get SERIAL-PORT (on linux)
$ ls -l /dev/ttyUSB*
```
Depending on the ESP32 microcontroller and operating system, the following outputs can be displayed:

- `/dev/tty.usbmodem*` or `/dev/tty.usbserial*` for macOS
- `/dev/ttyUSB*` or `/dev/ttyACM*`for Linux
- Windows will have COM ports 

> Since I don't use Windows myself, I can't provide examples or information.

## Project preparation

So that you can follow each example later, you should now create a project folder and create a Python virtual environment in it.

```shell
# create local project directory
$ mkdir -p ~/Projects/ESP

# change into project directory
$ cd ~/Projects/ESP

# create python virtualenvironment
$ python3 -m venv venv
```

> If you don't know the advantages of this environment exactly, read this [content](https://docs.python.org/3/tutorial/venv.html).

## Basic Python packages

Now you install the first (_and most important packages_) in your virtual environment. To do this, you first activate this environment.

```shell
# activate python virtual environment
$ source venv/bin/activate
```

> Please always pay attention to where you are! Otherwise, it can quickly lead to confusion with the local environment. As soon as you see (venv) in front of the $ sign, I talk about the virtual environment.

```shell
# install minimum required packages
(venv) $ pip3 install esptool

# list installed packages (optional)
(venv) $ pip3 freeze
```

We will install more packages later! If you want to exit the virtual environment, run the following command. But don't forget to start it again later.

```shell
# exit python virtual environment
(venv) $ deactivate
```

[Home](https://github.com/Lupin3000/ESP) | [Next](./001_firmware.md)
