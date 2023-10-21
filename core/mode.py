from __future__ import annotations
from typing import Sequence

from gpiozero import Button

from model.cycledlist import CycledListIterator
from model.movement import BallMovement


class ModeHandler:
    def __init__(self, button_pin: int, modes: Sequence[BallMovement]) -> None:
        self.button = Button(pin=button_pin)
        self._modes = CycledListIterator[BallMovement](modes)

    @classmethod
    def from_config(cls):
        from config.config import get_config

        modes = []

        return cls(get_config()["mode"]["button_pin"], modes)

    @property
    def current_mode(self) -> BallMovement:
        return self._modes.current

    def _next(self) -> BallMovement:
        # 초기화
        self._modes.current.init()
        # 다음 mode로 넘어가기
        return next(self._modes)

    def update(self) -> BallMovement:
        if self.button.value == 1:
            return self._next()
        return self.current_mode
