"""Find Ball in array image"""

from __future__ import annotations

from numpy import ndarray

from model.vector import Vec2D
from config.config import get_config


class BallFinder:
    """Detect Ball in 3D array image"""

    def __init__(self) -> None:
        config = get_config()
        self._r_range = (config["detector"]["r"][0],config["detector"]["r"][1]+1)
        self._g_range = (config["detector"]["g"][0],config["detector"]["g"][1]+1)
        self._b_range = (config["detector"]["b"][0],config["detector"]["b"][1]+1)
        


    def find_pos(self, arr_image: ndarray[ndarray[int, int, int]]) -> Vec2D:
        """calc the position of the ball using the array image"""
        ball_loc = [] 
        for y, arr in enumerate(arr_image):
            for x, rgb in enumerate(arr):
                if rgb[0] in range(*self._r_range) and rgb[1] in range(*self._g_range) and rgb[2] in range(*self._b_range):
                    ball_loc.append(Vec2D(x,y))
        
        return ball_loc
    