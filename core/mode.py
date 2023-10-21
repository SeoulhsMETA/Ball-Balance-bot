from __future__ import annotations

from gpiozero import Button

from config.config import get_config
from model.cycledlist import CycledListIterator
from model.movement import BallMovement


class ModeHandler:
    def __init__(self) -> None:
        self.button = Button(pin=get_config()["mode"]["button_pin"])
        self._mode = CycledListIterator[BallMovement]([])

    @property
    def current_mode(self) -> BallMovement:
        return self._mode.current

    def _next(self) -> BallMovement:
        #초기화
        self._mode.current.init()
        #다음 mode로 넘어가기
        return next(self._mode)
        

    def update(self) -> BallMovement:
        if self.button.value == 1:
            return self._next()
        return self.current_mode
