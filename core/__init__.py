from __future__ import annotations

import asyncio
from typing import NoReturn

from picamera import PiCamera
from picamera.array import PiRGBArray
from socketio import AsyncClient

from core.controll import BallControl
from core.finder import BallFinder
from core.mode import ModeHandler
from core.plate import PlateController
from core.client import SocketIOClient
from model.status import BotStatusQueue, BotStatus
from config.config import get_config


class Bot:
    """Control Bot"""

    def __init__(self, status_queue: BotStatusQueue) -> None:
        self.camera = PiCamera()
        self.camera_output = PiRGBArray(self.camera)

        self.plate = PlateController.from_config()
        self.pid = BallControl(self.plate)
        self.mode = ModeHandler.from_config()
        self.finder = BallFinder.from_config()

        self.status_queue = status_queue

    async def run(self) -> NoReturn:
        while True:
            self.camera.capture(self.camera_output, format="rgb")

            ball_pos = self.finder.find_pos(self.camera_output.array)
            movement = self.mode.update()

            self.pid.process(movement, ball_pos)

            self.status_queue.put(BotStatus.make(ball_pos, self.plate))


class Client:
    """Bot status reporter"""

    def __init__(self, status_queue: BotStatusQueue) -> None:
        self.url = get_config()["client"]["url"]
        self.status_queue = status_queue

    async def run(self) -> NoReturn:
        async with AsyncClient() as sio:
            await sio.connect(self.url)

            while True:
                await asyncio.sleep(1)
                if (status_data := self.status_queue.get()) is not None:
                    await sio.emit("update_status", dict(status_data))
