"""Plate controller"""

from __future__ import annotations

from gpiozero import AngularServo


class PlateController:
    """Plate Controller using AngularServo"""

    def __init__(self, servo_x_pin: int, servo_y_pin: int) -> None:
        self.servo_x = AngularServo(pin=servo_x_pin)
        self.servo_y = AngularServo(pin=servo_y_pin)

    @classmethod
    def from_config(cls) -> PlateController:
        from config.config import get_config

        config = get_config()

        return cls(config["plate"]["servo_x_pin"], config["plate"]["servo_y_pin"])

    def tilt_to(self, x_angle: float, y_angle: float) -> None:
        """Rotate servo absolutely"""
        self.servo_x.angle = x_angle
        self.servo_y.angle = y_angle

    def tilt_by(self, dx_angle: float, dy_angle: float) -> None:
        """Rotate servo relatively"""
        self.servo_x.angle += dx_angle
        self.servo_y.angle += dy_angle
