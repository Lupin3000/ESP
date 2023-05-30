from micropython import const
from machine import Pin
from lib.dfplayermini import Player
from utime import sleep_ms, ticks_ms


PLAYER_TX = const(17)
PLAYER_RX = const(16)
PLAYER_BOOT = const(1000)

BTN_ONE = const(22)
BTN_TWO = const(23)


class SoundPlayer:
    def __init__(self, tx: int, rx: int, tracks: int, wait: int = 200):
        """
        Sound player constructor
        :param tx: value for TX GPIO pin
        :param rx: value for RX GPIO pin
        :param wait: waiting period in milliseconds to read SD card files
        """
        self._tracks_amount = int(tracks)
        self._track_current = 1

        self.player = Player(pin_TX=int(tx), pin_RX=int(rx))
        sleep_ms(int(wait))

        self.player.volume(10)

    def next(self) -> None:
        """
        play next track
        :return: None
        """
        if self._track_current < self._tracks_amount:
            self._track_current += 1
            self.player.play(self._track_current)

    def prev(self) -> None:
        """
        play previous track
        :return: None
        """
        if self._track_current > 1:
            self._track_current -= 1
            self.player.play(self._track_current)


class Control:
    def __init__(self, player):
        """
        control constructor
        :param player: DFPlayer object
        """
        self._last_time = 0
        self._player = player

        self.btn_next = Pin(BTN_ONE, Pin.IN, Pin.PULL_UP)
        self.btn_prev = Pin(BTN_TWO, Pin.IN, Pin.PULL_UP)

        self.btn_next.irq(trigger=Pin.IRQ_FALLING, handler=self._handler)
        self.btn_prev.irq(trigger=Pin.IRQ_FALLING, handler=self._handler)

    def _handler(self, pin) -> None:
        """
        interrupt handler for buttons (next/prev)
        :param pin: handler pin object
        :return: None
        """
        new_time = ticks_ms()

        if (new_time - self._last_time) > 200:
            self._last_time = new_time

            if pin == Pin(BTN_ONE):
                self._player.next()

            if pin == Pin(BTN_TWO):
                self._player.prev()


if __name__ == '__main__':
    music = SoundPlayer(tx=PLAYER_TX, rx=PLAYER_RX, tracks=5, wait=PLAYER_BOOT)
    btn = Control(player=music)
