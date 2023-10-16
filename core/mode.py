from __future__ import annotations

from gpiozero import Button

from config.config import get_config
from model.cycledlist import CycledListIterator
from model.movement import BallMovement


class ModeHandler:
    def __init__(self) -> None:
        self.button = Button(pin=get_config()["mode"]["button_pin"])
        self._mode = CycledListIterator([])

    @property
    def current_mode(self) -> BallMovement:
        pass

    def next(self):
        pass

    def update(self):
        pass
