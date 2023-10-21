"""Define Ball Movement"""

from collections.abc import Sequence
from math import radians, sin, cos

from model.cycledlist import CycledList, CycledListIterator
from model.vector import Vec2D


POS = Vec2D | Sequence[float]


class BallMovement:
    """Define ball movement"""

    def __init__(self, cycle: Sequence[POS]) -> None:
        cycled_list = CycledList()
        for vec in cycle:
            if isinstance(vec, Vec2D):
                cycled_list.append(vec)
            else:
                cycled_list.append(Vec2D(*vec))

        self._cycled_pos: CycledListIterator = iter(cycled_list)

        self._accuracy: float = 0

    def init(self) -> None:
        """init movement"""
        self._cycled_pos.pointer = 0

    def next(self, ball_pos: Vec2D) -> Vec2D:
        """get next target pos"""
        if ball_pos.distance_to(self._cycled_pos.current) <= self._accuracy:
            return next(self._cycled_pos)
        return self._cycled_pos.current


class StaticPos(BallMovement):
    def __init__(self, pos: POS) -> None:
        super().__init__([])
        if isinstance(pos, Vec2D):
            self.pos = pos
        else:
            self.pos = Vec2D(*pos)
        self._accuracy = 0

    def next(self, ball_pos: Vec2D) -> Vec2D:
        return self.pos


class CircleMovement(BallMovement):
    def __init__(self, radius: int) -> None:
        super().__init__(
            [
                (radius * cos(radians(i)), radius * sin(radians(i)))
                for i in range(0, 360)
            ]
        )
