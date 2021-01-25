import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker:
    def crop(self, array, dimensions, position=(0, 0)):
        if (dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]):
            print("Incorrect dimensions")
            return None
        return array

    def thin(self, array, n, axis):
        pass

    def juxtapose(self, array, n, axis):
        pass

    def mosaic(self, array, dimensions):
        pass


sb = ScrapBooker()

imp = ImageProcessor()
arr = imp.load("42AI.png")
arr = sb.crop(arr, (100, 100), (0, 0))
imp.display(arr)
