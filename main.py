from core.finder import BallFinder
from numpy import ndarray
import numpy as np

find = BallFinder()

image = np.array([[[100,100,100],[101,101,101]],
                [[120,120,120],[120,120,120]],
                [[100,100,100],[101,101,101]],
                [[120,120,120],[120,120,120]],
                [[100,100,100],[101,101,101]],
                [[120,120,120],[120,120,120]]
                ])

print(find.find_pos(image))

