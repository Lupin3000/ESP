# MicroPython REPL

## Table of Contents

- [What is REPL?](#what-is-repl)
- [Start a REPL](#start-a-repl)
- [Usage of REPL](#usage-of-repl)

## What is REPL?

With the Python REPL (_Read–eval–print loop_) you type commands and see the output. The very nice thing is you have features like: Code Suggestions, Auto-Completion, Auto-Indentation, Contextual History and many more.  

> - `>>>` commandline prompt for input (_confirmed by `ENTER`_)
> - `#` are comments and will be ignored
> - output don't start with `>>>` or `#`
> - `===` paste mode (_started with CTRL-E_)

```python
>>> 10 * 10
100

>>> myname = 'demo-string'
>>> myname
'demo-string'
```

## Start a REPL

**SCREEN**

```shell
$ screen [SERIAL-PORT] 115200
# now press CTRL-D or RST button on device
```

**MPFSHELL**

```shell
(venv) $ mpfshell -o [SERIAL-PORT]
mpfs [/]> repl
```

**rshell**

You can start the REPL via two options

```shell
# start REPL directly
(venv) $ rshell -p [SERIAL-PORT] repl

# start serial connection
(venv) $ rshell -p [SERIAL-PORT]

# start REPL
/your/current/path> repl
```

## Usage of REPL

**Important control commands:**
 - CTRL-A - on a blank line, enter raw REPL mode
 - CTRL-B - on a blank line, enter normal REPL mode
 - CTRL-C - interrupt a running program
 - CTRL-D - on a blank line, do a soft reset of the board
 - CTRL-E - on a blank line, enter paste mode

**Some helpful examples**

```python
>>> # list all modules
>>> help('modules')

>>> # show help for module
>>> import machine
>>> help(machine)

>>> # show python version
>>> import sys
>>> sys.version
>>> # ... or ...
>>> sys.implementation

>>> # working with directories
>>> import os
>>> os.getcwd()
'/'
>>> os.mkdir('demo')
>>> os.chdir('demo')
>>> os.getcwd()
'/demo'
>>> os.listdir('../')
['boot.py', 'demo', 'main.py']

>>> # soft reset (like CTRL-D)
>>> import machine
>>> machine.soft_reset()
```

[Home](https://github.com/Lupin3000/ESP) | [Previous](./001_serial_connection.md) | [Next](./002_frozen_code.md)
