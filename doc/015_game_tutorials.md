# Games

## Table of Contents

- [Prolog](#prolog)
- [Crazy Car Racer](#crazy-car-racer)
- [Space Invaders](#space-invaders)
- [Pong](#pong)
- [Snake](#snake)

## Prolog

Games are great and help to forget everyday life. In addition, the development of games helps to discover new possibilities and to expand the own knowledge.

## Crazy Car Racer

It's a cold and dark night. The drugs are still working and your blood is boiling. You get in your car and take off. As in reality, there is only one life and if you collide ... game over.

### Requirements

- mandatory 1x I2C OLED (_example 0.96" 128x64_) 
- mandatory 1x potentiometer (_e.g. 10 kilo ohms_)
- mandatory 1x passive buzzer (_Piezo Buzzer_)
- few cables 
- optional a breadboard

### Circuit

![015_ciruit_racer_game.png](../images/examples/015_ciruit_diagram_racer_game.png)

### Code

```shell
# create new subdirectory
$ mkdir -p ~/Projects/ESP/examples/games

# create script
$ touch ~/Projects/ESP/examples/games/racer.py

# download images
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/examples/games/racer_car.pbm' -o examples/games/racer_car.pbm
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/examples/games/racer_dead.pbm' -o examples/games/racer_dead.pbm
$ curl -L 'https://raw.githubusercontent.com/Lupin3000/ESP/master/examples/games/racer_intro.pbm' -o examples/games/racer_intro.pbm
```

> [Source Code](../examples/games/racer.py) for `racer.py`
> 
> [Source Code](../lib/ssd1306.py) for `lib/ssd1306.py`

Check your circuit and copy all images and the script to the microcontroller.

```shell
# start serial connection
(venv) $ rshell -p [SERIAL-PORT]

# upload images
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/racer_car.pbm /pyboard/
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/racer_dead.pbm /pyboard/
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/racer_intro.pbm /pyboard/

# upload script
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/racer.py /pyboard/main.py

# copy module file into lib
(venv) $ rshell -p [SERIAL-PORT] cp lib/ssd1306.py /pyboard/lib/

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press `reset` key or start with keys `Control` + `d`.

> Feel free to expand the game! For example, add more objects that simulate trees and bushes or more levels (_after about 10 points the road gets smaller_) and so on.

## Space Invaders

Everyone knows the Space Invaders! But nobody knows where they come from. If you value our planet, protect our world from these invaders.

### Requirements

- mandatory 1x SPI LCD Nokia 5110 
- mandatory 1x potentiometer (_e.g. 10 kilo ohms_)
- mandatory 1x button
- few cables 
- optional a breadboard

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/games/invader.py
```

> [Source Code](../examples/games/invader.py) for `invader.py`
> 
> [Source Code](../lib/pcd8544.py) for `lib/pcd8544.py`

Check your circuit and copy the script to the microcontroller.

```shell
# upload script
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/invader.py /pyboard/main.py

# copy module file into lib
(venv) $ rshell -p [SERIAL-PORT] cp lib/pcd8544.py /pyboard/lib/

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press `reset` key or start with keys `Control` + `d`.

> Feel free to expand the game! For example, add more objects enemies or change speed if enemy goes down.

## Pong

On of the retro-gaming classics! Catch the ball or die... 

## Requirements

- mandatory 1x NeoPixel Matrix (_[LED Matrix Panel ](https://www.waveshare.com/pico-rgb-led.htm)_)
- mandatory 1x potentiometer (_e.g. 10 kilo ohms_)
- few cables 
- optional a breadboard

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/games/pong.py
```

> [Source Code](../examples/games/pong.py) for `pong.py`

> [Source Code](../lib/neopixelmatrix.py) for `lib/neopixelmatrix.py`

Check your circuit and copy the script to the microcontroller.

```shell
# copy example file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/pong.py /pyboard/main.py

# copy module file into lib
(venv) $ rshell -p [SERIAL-PORT] cp lib/neopixelmatrix.py /pyboard/lib/

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press `reset` key or start with keys `Control` + `d`.

> Feel free to expand the game! For example, increase continuously the speed after some minutes.

## Snake

The vegan snake grows with every fruit it eats. But beware! Don't get to the edge or your own tail.

## Requirements

- mandatory 1x SPI OLED DISPLAY (_e.g. SH1106_) 
- mandatory 1x Joystick
- few cables 
- optional a breadboard

### Code

```shell
# create script
$ touch ~/Projects/ESP/examples/games/snake.py
```

> [Source Code](../examples/games/snake.py) for `snake.py`

> [Source Code](../lib/sh1106.py) for `lib/sh1106.py`

Check your circuit and copy the script to the microcontroller.

```shell
# copy example file into pyboard as main.py
(venv) $ rshell -p [SERIAL-PORT] cp examples/games/snake.py /pyboard/main.py

# copy module file into lib
(venv) $ rshell -p [SERIAL-PORT] cp lib/sh1106.py /pyboard/lib/

# start repl
(venv) $ rshell -p [SERIAL-PORT] repl
```

Press `reset` key or start with keys `Control` + `d`.

> Feel free to expand the game! For example, add speed or other enemies which eats the fruits too.

[Home](https://github.com/Lupin3000/ESP) | [Previous](./014_sensor_extended.md) | [Next]()
