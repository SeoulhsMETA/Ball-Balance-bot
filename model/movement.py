"""Define Ball Movement"""

from collections.abc import Sequence

from model.cycledlist import CycledList, CycledListIterator
from model.vector import Vec2D
from config.config import get_config


class BallMovement:
    """Define ball movement"""

    def __init__(self, cycle: Sequence[Vec2D | Sequence[float]]) -> None:
        cycled_list = CycledList()
        for vec in cycle:
            if isinstance(vec, Vec2D):
                cycled_list.append(vec)
            else:
                cycled_list.append(Vec2D(vec))

        self._cycled_pos: CycledListIterator = iter(cycled_list)

        self._accuracy: float = get_config()["movement"][self.__class__.__name__][
            "accuracy"
        ]

    def init(self) -> None:
        """init movement"""
        self._cycled_pos.init()

    def next(self, ball_pos: Vec2D) -> Vec2D:
        """get next target pos"""
        if ball_pos.distance_to(self._cycled_pos.current) <= self._accuracy:
            return next(self._cycled_pos)
        return self._cycled_pos.current
