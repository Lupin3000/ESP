# MicroPython frozen code

## Table of Contents

- [Benefit of frozen code](#benefit-of-frozen-code)
- [Required package](#required-package)
- [Compile py to mpy](#compile-py-to-mpy)
- [Use MPY](#use-mpy)

## Benefit of frozen code

So far, you should pay attention to the freely available memory with microcontrollers. Each character in your code requires some storage space, for example comments. However, comments and docstrings are important and should therefore not be deleted!

There is also the issue of performance. If the code is already provided pre-compiled in bytecode, there can be advantages here. Once the code is frozen it can be quickly loaded and interpreted by MicroPython without as much memory and processing time.

Finally, you can also protect your code somewhat from strangers. It won't be possible for everyone to reverse engineer this bytecode again. However, there is no 100% protection here.

[Here](https://docs.micropython.org/en/latest/reference/mpyfiles.html) you will find all needed information about `*.mpy` files.

> At a later date I will explain how you can build your own MicroPython firmware. Frozen modules are also used again.

## Required package

The MicroPython `mpy-cross` compiler will help you to easily compile `*.py` scripts into `*.mpy` files.

```shell
# install mpy-cross
(venv) $ pip3 install mpy-cross

# show help (optional)
(venv) $ mpy-cross -h
```

## Compile py to mpy

You'll soon realize that the process is super simple.

```shell
# run mpy-cross compiler
(venv) $ mpy-cross example_module.py
```

## Use MPY

Now use `rshell` to copy the `*.mpy` file to the `pyboard` folder on your microcontroller.

**Create example module**

Now create a new folder with a sample Python script (_inside your local project_).

```shell
# create subdirectory for example
$ mkdir -p ~/Projects/ESP32/examples/mpy

# create a example module
$ touch ~/Projects/ESP32/examples/mpy/example_module.py
```

Inside this path you should now create a file called `example_module.py` with the following code.

```python
from gc import mem_free

print('[INFO] MPY example')
print(f'[INFO] Memory free {mem_free()} bytes')

```

Now compile this module.

```shell
# change directory
(venv) $ cd ~/Projects/ESP32/examples/mpy/

# run compile
(venv) $ mpy-cross example_module.py

# list directory files (optional)
(venv) $ ls -la
```

**Copy `*.mpy` file to microcontroller**

```shell
# start serial connection
(venv) $ rshell -p [SERIAL-PORT]

# copy mpy via rshell
/your/current/path> cp example_module.mpy /pyboard/example_module.mpy

# list files (optional)
/your/current/path> ls /pyboard/
```

**Run `*.mpy` via REPL**

```shell
# start REPL via rshell
/your/current/path> repl
```

Import the module and watch the output.

```python
>>> import example_module
```

To delete the `*.mpy` file from microcontroller, follow the next command.

```shell
# cleanup example
/your/current/path> rm /pyboard/example_module.mpy
```

> This was just an example for understanding! In this example, the file size of the `*.mpy` is slightly larger than that of the `*.py` file.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./004_python_repl.md) | [Next](./006_board_tutorials.md)
