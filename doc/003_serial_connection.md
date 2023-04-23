# Serial connection

## Table of Contents

- [screen](#screen)
- [mpfshell](#mpfshell)
- [rshell](#rshell)

## screen

As soon as your microcontroller has flashed the latest MicroPython firmware, you can test a first connection with `screen`. For macOS screen is already available (_no installation needed_).

```shell
# start connection
$ screen [SERIAL-PORT] 115200
```

Screen is a great tool, but there is a more comfortable way. For example tools like `picocom` or `minicom` could be interesting. I would like to mention `mpfshell` and my favorite `rshell`.

## mpfshell

In addition to a connection from the local device to the microcontroller, options such as uploads/downloads and others are required. From here, the advantages over `screen quickly become apparent.

```shell
# install mpfshell package
(venv) $ pip3 install mpfshell

# start connection
(venv) $ mpfshell -o [SERIAL-PORT]
```

If you like to know more details about mpfshell, visit this [link](https://github.com/wendlers/mpfshell). It does have really awesome features.

## rshell

Now we finally come to my personal favorite `rshell`. Since I use this again and again in other sections (_for tutorials_), I also go into more detail about this tool here.

### Installation

```shell
# install rshell package
(venv) $ pip3 install rshell
```

### Basic commands

Basic commands without established connection.

```shell
# show rshell help
(venv) $ rshell -h

# list serial ports
(venv) $ rshell -l

# start rshell
(venv) $ rshell
```

Basic commands with established connection.

```shell
# show global help
/your/local/path> help

# show specific help for command
/your/local/path> help connect

# exit rshell
/your/local/path> exit
```

### Connect to microcontroller

There are basically 3 options to connect to microcontroller.

**First option**

Here you start `RSHELL` first and in a second step you connect to the microcontroller via `serial` or `telnet`.

```shell
# start rshell
(venv) $ rshell

# use rshell command connect (serial)
/your/local/path> connect serial [SERIAL PORT]

# use rshell command connect (telnet)
/your/local/path> connect telnet [IP-ADDRESS or NAME]
```

**Second option**

Here you start the serial connection directly.

```shell
# start rshell with serial port
(venv) $ rshell -p [SERIAL PORT]
```

**Third option (_direct command execution_)**

Here you establish the serial connection, execute a command and close the connection.

```shell
# list boards
(venv) $ rshell -p [SERIAL PORT] boards

# list files
(venv) $ rshell -p [SERIAL PORT] ls /pyboard/
```

> Choose the connection option according to the situation and needs. But always pay attention to whether you are working locally or on the board!

Here now a short overview about the most important commands. To follow this, establish the connection like in first or second option.

#### Boards

```shell
# show is_central_connected boards
/your/local/path> boards
```

> Normally (_after flashing_) the board should be called `pyboard`.

You can change the name of your board!

```shell
# rename board (create board.py)
/your/local/path> echo 'name="esp32"' > /pyboard/board.py
```

_Note: However, note the name change in the following examples (this has not been changed here)._

#### Date

```shell
# show date (local)
/your/local/path> date

# show date (board)
/your/local/path> date -b pyboard
```

#### Files

**List and show files**

```shell
# list local files
/your/local/path> ls

# list board files
/your/local/path> ls /pyboard/

# show board file conntent on stdout
/your/local/path> cat /pyboard/boot.py

# show filetype (board)
/your/local/path> filetype /pyboard/boot.py

# show filesize (board)
/your/local/path> filesize /pyboard/boot.py
```

**Copy files**

```shell
# copy from local to board
/your/local/path> cp main.py /pyboard/main.py

# copy from board to local
/your/local/path> cp /pyboard/boot.py boot.py
```

**Delete files**

```shell
# delete file (board)
/your/local/path> rm /pyboard/example.py
```

#### Directories

```shell
# create directory (board)
/your/local/path> mkdir /pyboard/demo

# delete directory (board)
/your/local/path> rm -r /pyboard/demo/
```

#### REPL

```shell
# start python repl
/your/local/path> repl
```

If you like to know more, have a look on this [link](https://github.com/dhylands/rshell).

[Home](https://github.com/Lupin3000/ESP) | [Previous](./002_firmware.md) | [Next](./004_python_repl.md)
