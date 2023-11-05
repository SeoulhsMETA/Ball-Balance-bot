import time
from functools import reduce

import cv2
import numpy

from core.finder import BallFinder
from model.vector import Vec2D

finder = BallFinder.from_config()
img = cv2.imread("image.jpg")

# 930, 1332
# [ 814  814  814 ... 1056 1056 1056] [1340 1341 1342 ... 1374 1375 1376]

# times = []
#
# for i in range(1000):
#     start = time.time()
#     pos = finder.find_pos(img)
#     times.append(time.time() - start)
#     print(pos)
#
# print(f"average: {sum(times) / len(times)}\nmax: {max(times)}\nmin: {min(times)}")

b_arr, g_arr, r_arr = numpy.dsplit(img, 3)

lower = [20, 20, 90]
upper = [60, 60, 255]

b_y_arr, b_x_arr, _ = numpy.where((lower[0] <= b_arr) & (b_arr <= upper[0]))
g_y_arr, g_x_arr, _ = numpy.where((lower[1] <= g_arr) & (g_arr <= upper[1]))
r_y_arr, r_x_arr, _ = numpy.where((lower[2] <= r_arr) & (r_arr <= upper[2]))

print(numpy.intersect1d(b_x_arr, g_x_arr, return_indices=True), numpy.intersect1d(b_y_arr, g_y_arr, return_indices=True))

print(Vec2D(numpy.average(reduce(numpy.intersect1d, (r_x_arr, g_x_arr, b_x_arr))), numpy.average(reduce(numpy.intersect1d, (r_y_arr, g_y_arr, b_y_arr)))))
