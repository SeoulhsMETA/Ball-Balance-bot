from picamera import PiCamera
from picamera.array import PiRGBArray

from core.finder import BallFinder

cam = PiCamera()
cam.resolution = (256,144)
output = PiRGBArray(cam)

finder = BallFinder.from_config()

print("ready")
while True:
    cam.capture(output, "rgb")
    print(f"capture: {output.array.shape}")
    print(finder.find_pos(output.array))
