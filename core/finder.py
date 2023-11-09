"""Find Ball in array image"""

from __future__ import annotations
from typing import Sequence, Optional

import numpy

from model.vector import Vec2D


class BallFinder:
    """Detect Ball in 3D array image"""

    def __init__(
        self,
        lower: Sequence[int],
        upper: Sequence[int],
        part_search_size: Sequence[int],
    ) -> None:
        self.latest_pos: Optional[Vec2D] = None
        self.lower = numpy.array(lower)
        self.upper = numpy.array(upper)
        self.part_size = part_search_size

    @classmethod
    def from_config(cls) -> BallFinder:
        from config.config import get_config

        config = get_config()
        lower = config["detector"]["lower"]
        upper = config["detector"]["upper"]
        part_search_size = config["detector"]["part_search_size"]

        return cls(lower, upper, part_search_size)

    def find_pos(self, arr_image: numpy.ndarray) -> Vec2D:
        """calc the position of the ball using the array image"""
        if self.latest_pos is None:
            # full search
            x_arr, y_arr = numpy.where(
                ((self.lower <= arr_image) & (arr_image <= self.upper)).all(axis=2)
            )

            pos = Vec2D(numpy.average(x_arr), numpy.average(y_arr))
        else:
            clip_rect = (
                self.latest_pos.x - (self.part_size[0] // 2),
                self.latest_pos.y - (self.part_size[1] // 2),
                self.part_size[0] + 1,
                self.part_size[1] + 1,
            )
            # part search
            part_img_arr = arr_image[
                clip_rect[0] : clip_rect[0] + clip_rect[2],
                clip_rect[1] : clip_rect[1] + clip_rect[3],
            ]
            x_arr, y_arr = numpy.where(
                ((self.lower <= part_img_arr) & (part_img_arr <= self.upper)).all(
                    axis=2
                )
            )

            pos = Vec2D(
                clip_rect[0] + numpy.average(x_arr), clip_rect[1] + numpy.average(y_arr)
            )

        if not pos.is_nan():
            self.latest_pos = Vec2D(round(pos.x), round(pos.y))
            return pos

        self.latest_pos = None
        raise BallNotFoundError


class BallNotFoundError(Exception):
    pass
