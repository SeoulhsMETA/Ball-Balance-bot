"""Find Ball in array image"""

from __future__ import annotations

from numpy.typing import NDArray

from model.vector import Vec2D
from config.config import get_config


class BallFinder:
    """Detect Ball in 3D array image"""

    def __init__(self) -> None:
        config = get_config()
        self._r_range: list[int, int] = config["detector"]["r"]
        self._g_range: list[int, int] = config["detector"]["g"]
        self._b_range: list[int, int] = config["detector"]["b"]

    def find_pos(self, image: NDArray) -> Vec2D:
        """calc the position of the ball using the array image"""
        raise NotImplementedError
