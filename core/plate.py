"""Plate controller"""

from __future__ import annotations

from gpiozero import AngularServo

from config.config import get_config


class PlateController:
    """Plate Controller using AngularServo"""

    def __init__(self) -> None:
        config = get_config()
        self.servo_x = AngularServo(pin=config["servo"]["x_axis_pin"])
        self.servo_y = AngularServo(pin=config["servo"]["x_axis_pin"])

    def tilt_by(self) -> None:
        """rotate relatively"""
        return

    def tilt_to(self) -> None:
        """rotate absolutely"""
        return
