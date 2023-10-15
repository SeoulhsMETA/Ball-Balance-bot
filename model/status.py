"""Bot status data structure"""

from __future__ import annotations
from typing import Optional
from queue import Queue
import json

# import time

from gpiozero import AngularServo

from model.vector import Vec2D


class BotStatus:
    """Bot Status Data"""

    def __init__(
        self,
        timestamp: float,
        ball_pos: Vec2D,
        servo_x: AngularServo,
        servo_y: AngularServo,
    ) -> None:
        self.timestamp = timestamp
        self.ball_pos = ball_pos
        self.x_axis = servo_x.angle
        self.y_axis = servo_y.angle

    # @classmethod
    # def make(cls, ball_pos: Vec2D, servo_x: Servo, servo_y: Servo) -> BotStatus:
    #     """make BotStatus automatically"""
    #     timestamp = datetime.datetime.now().date()
    #     return cls(timestamp, ball_pos, servo_x, servo_y)

    def to_jsons(self) -> str:
        """convert to json"""
        return json.dumps(self, cls=BotStatusEncoder)

    def __repr__(self) -> str:
        return (
            f"BotStatus("
            f"{self.timestamp=}, "
            f"{self.ball_pos=}, "
            f"{self.x_axis=}, "
            f"{self.y_axis=})"
        )


class BotStatusQueue(Queue):
    """Bot Status Queue"""

    def put(
        self, item: BotStatus, block: bool = True, timeout: float | None = None
    ) -> None:
        if not isinstance(item, BotStatus):
            raise ValueError("item should be BotStatus")
        return super().put(item, block, timeout)

    def get(
        self, block: bool = True, timeout: float | None = None
    ) -> Optional[BotStatus]:
        if self.full():
            return super().get(block, timeout)
        return None


class BotStatusEncoder(json.JSONEncoder):
    """json encoder for BotStatus"""

    def default(self, o: BotStatus) -> dict:
        return {
            "timestamp": o.timestamp,
            "ballPos": list(o.ball_pos),
            "servo": [o.x_axis, o.y_axis],
        }
