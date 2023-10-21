from picamera import PiCamera
frmo picamera.array import PiRGBArray

from core.controll import BallControl
from core.finder import BallFinder
from core.mode import ModeHandler
from core.plate import PlateController
from model.status import BotStatusQueue, BotStatus

class Bot:
    def __init__(self, status_queue: BotStatusQueue):
        self.camera = PiCamera()
        self.camera_output = PiRGBArray(self.camera)

        self.plate = PlateController.from_config()
        self.pid = BallControl(self.plate)
        self.mode = ModeHandler.from_config()
        self.finder = BallFinder.from_config()

        self.status_queue = status_queue

    def run(self):
        while True:
            self.camera.capture(self.camera_output, format="bgr")

            ball_pos = self.finder.find_pos(self.camera_output.array)
            movement = self.mode.update()

            self.pid.process(movement, ball_pos)

            self.status_queue.put(BotStatus.make(ball_pos, self.plate))

class Main:
    def __init__(self):
        self.status_queue = BotStatusQueue()
        self.bot = Bot(self.status_queue)
