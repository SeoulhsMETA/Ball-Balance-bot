"""Plate controller"""

from __future__ import annotations

from gpiozero import AngularServo

from config.config import get_config


class PlateController:
    """Plate Controller using AngularServo"""

    def __init__(self) -> None:
        config = get_config()
        self.servo_x = AngularServo(pin=config["plate"]["servo_x_pin"])
        self.servo_y = AngularServo(pin=config["plate"]["servo_y_pin"])

    def tilt_to(self, xAngle, yAngle) -> None:
        """Rotate servo absolutely"""
        self.servo_x.angle = xAngle
        self.servo_y.angle = yAngle

    
    def tilt_by(self, d_xAngle, d_yAngle) -> None:
        """Rotate servo relatively"""
        self.servo_x.angle += d_xAngle
        self.servo_y.angle += d_yAngle
