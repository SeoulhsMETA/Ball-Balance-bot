"""controll ball with PID"""

from __future__ import annotations

from core.plate import PlateController
from model.vector import Vec2D


class BallControl:
    """PID control using the plate controller"""

    def __init__(self, plate_controller: PlateController) -> None:
        self.plate = plate_controller

    def process(self, movement, ball_pos: Vec2D) -> None:
        """controll ball to target pos"""
        raise NotImplementedError
