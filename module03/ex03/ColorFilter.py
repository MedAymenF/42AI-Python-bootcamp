import numpy as np


class ColorFilter:
    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        new = np.zeros(array.shape)
        new[:, :, 2] = array[:, :, 2]
        return new

    def to_green(self, array):
        array[:, :, 0] = 0
        array[:, :, 2] = 0
        return array

    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)

    def to_celluloid(self, array):
        shades = np.linspace(0, 1, num=5)
        for i in range(len(shades) - 1):
            shade_index = (array >= shades[i]) & (array <= shades[i + 1])
            array[shade_index] = shades[i]
        return array

    def to_grayscale(self, array, filter="weighted"):
        if (filter == 'm' or filter == "mean"):
            tmp = np.sum(array, axis=2) / 3
            tmp = np.reshape(tmp, (array.shape[0], array.shape[1], 1))
            return np.broadcast_to(tmp, (array.shape[0], array.shape[1], 3))
        elif (filter == "weighted" or filter == 'w'):
            array[:, :, 0] = array[:, :, 1] * 0.299
            array[:, :, 1] = array[:, :, 1] * 0.587
            array[:, :, 2] = array[:, :, 2] * 0.114
            tmp = np.sum(array, axis=2, keepdims=True)
            return np.tile(tmp, 3)
