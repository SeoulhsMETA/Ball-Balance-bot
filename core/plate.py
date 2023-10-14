"""Plate controller"""

from __future__ import annotations

from gpiozero import AngularServo

class PlateController:
    def __init__(self) -> None:
        self.servo_x = AngularServo
        self.servo_y = AngularServo
