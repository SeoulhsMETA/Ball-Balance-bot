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

        # TODO 서보 구동 코드 구현
        # PlateController를 이용해서 target Vec2D로 공을 옮기기 위해
        #  서보를 조종하는 코드를 구현해야됨
        # 현재 윗 줄에 있는 PID 계산 식도 이론상 이상적인 데이터가 나올 수 있는 값으로
        #  정확하게 output들을 분석 후, 오차 수정같은 과정이 수행되지 않았음

        raise NotImplementedError
