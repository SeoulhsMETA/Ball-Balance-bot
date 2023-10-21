"""Find Ball in array image"""

from __future__ import annotations
from typing import Sequence

from numpy import ndarray, nditer

from model.vector import Vec2D


class BallFinder:
    """Detect Ball in 3D array image"""

    def __init__(
        self, r_range: Sequence[int], g_range: Sequence[int], b_range: Sequence[int]
    ) -> None:
        self._r_range = range(r_range[0], r_range[1] + 1)
        self._g_range = range(g_range[0], g_range[1] + 1)
        self._b_range = range(b_range[0], b_range[1] + 1)

    @classmethod
    def from_config(cls) -> BallFinder:
        from config.config import get_config

        config = get_config()
        r_range = (config["detector"]["r"][0], config["detector"]["r"][1] + 1)
        g_range = (config["detector"]["g"][0], config["detector"]["g"][1] + 1)
        b_range = (config["detector"]["b"][0], config["detector"]["b"][1] + 1)

        return cls(r_range, g_range, b_range)

    def find_pos(self, arr_image: ndarray[ndarray[int, int, int]]) -> Vec2D:
        """calc the position of the ball using the array image"""
        vec = Vec2D(0, 0)
        count = 0

        it = nditer(arr_image, flags=["multi_index"])

        rgb = []

        while not it.finished:
            index = it.multi_index
            x, y = index[0], index[1]
            rgb.append(arr_image[index])

            if len(rgb) == 3:
                if rgb[0] in self._r_range and rgb[1] in self._g_range and rgb[2] in self._b_range:
                    vec += Vec2D(x, y)
                    count += 1
                rgb.clear()
            
            it.iternext()

        if count:
            return vec / count
        
        raise BallNotFoundError

class BallNotFoundError(Exception):
    pass
