import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker:
    def crop(self, array, dimensions, position=(0, 0)):
        if (dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]):
            print("Incorrect dimensions")
            raise Exception
        return array[position[0]:dimensions[0]+position[0],
                     position[1]:dimensions[1]+position[1]]

    def thin(self, array, n, axis):
        if axis:
            index = np.array([i % n != n - 1 for i in range(array.shape[0])])
            return array[index, :]
        else:
            index = np.array([i % n != n - 1 for i in range(array.shape[1])])
            return array[:, index]

    def juxtapose(self, array, n, axis):
        new = array
        for _ in range(n - 1):
            new = np.concatenate((new, array), axis=axis)
        return new

    def mosaic(self, array, dimensions):
        vert_new = self.juxtapose(array, dimensions[0], 0)
        new = self.juxtapose(vert_new, dimensions[1], 1)
        return new
