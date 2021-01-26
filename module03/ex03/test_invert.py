from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("musk.png")
print(arr)
cf = ColorFilter()
cf.invert(arr)
imp.display(arr)
