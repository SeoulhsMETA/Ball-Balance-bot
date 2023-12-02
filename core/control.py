"""control ball with PID"""

from __future__ import annotations
import time

from core.plate import PlateController
from model.vector import Vec2D
from model.movement import BallMovement


class BallControl:
    """PID control using the plate controller"""

    def __init__(self, plate_controller: PlateController, kp: float, ki: float, kd: float) -> None:
        self.plate = plate_controller

        self._latest_time = 0
        self._latest_error = 0
        self._error_integral = 0
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def process(self, movement: BallMovement, ball_pos: Vec2D) -> None:
        """control ball to target pos"""
        current_time = time.time()
        dt = self._latest_time - current_time

        target = movement.next(ball_pos)
        error = target.distance_to(ball_pos)

        error_derivation = (error - self._latest_error) / dt
        self._error_integral += error * dt

        pid = self.kp * error + self.ki * self._error_integral + self.kd * error_derivation

        self._latest_error = error
        self._latest_time = current_time
        raise NotImplementedError
