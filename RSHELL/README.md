# RSHELL

## Basic commands

```shell
# start rshell
$ rshell

# show global help
/your/local/path> help

# show specific help for command
/your/local/path> help connect

# exit rshell
/your/local/path> exit
```

## Connect to board

There are basically 3 ways to connect to boards.

**First option**

```shell
# start rshell with serial port
$ rshell -p [SERIAL PORT]
```

**Second option**

```shell
# start rshell
$ rshell

# use rshell command connect (incl serial)
/your/local/path> connect serial [SERIAL PORT]

# use rshell command connect (incl telnet)
/your/local/path> connect telnet [IP-ADDRESS or NAME]
```

**Third option (_direct command execution_)**

```shell
# list files
$ rshell -p [SERIAL PORT] ls /pyboard
```

_Note: The following examples require the first or second option (what you see at the prompt)._

> Always pay attention to whether you are working locally or on the board!

## Boards

```shell
# show connected boards
/your/local/path> boards
```

> Normally (_after flashing_) the board should be called `pyboard`.

You can change the name of your board!

```shell
# rename board (create board.py)
/your/local/path> echo 'name="esp32"' > /pyboard/board.py
```

_Note: However, note the name change in the following examples (this has not been changed here)._

## Date

```shell
# show date (local)
/your/local/path> date

# show date (board)
/your/local/path> date -b pyboard
```

## Files

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

## Directories

```shell
# create directory (board)
/your/local/path> mkdir /pyboard/demo

# delete directory (board)
/your/local/path> rm -r /pyboard/demo/
```

## REPL

> [Here](../REPL/README.md) you will find more about the Python REPL.

```shell
# start python repl
/your/local/path> repl
```

## other commands

> There are many more commands but I am sure that you will find out for yourself what they do and how they are carried out.

[Go Back](https://github.com/Lupin3000/ESP)
