from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
cf = ColorFilter()
arr = cf.to_grayscale(arr, 'm')
imp.display(arr)
