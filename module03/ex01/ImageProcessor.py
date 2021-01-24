import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        arr = plt.imread(path)
        print(f"Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}")
        return arr

    def display(self, array):
        plt.imshow(array)
        plt.show()


imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
imp.display(arr)
