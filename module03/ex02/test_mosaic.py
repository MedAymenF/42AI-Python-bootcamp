from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()

imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
arr = sb.mosaic(arr, (2, 3))
imp.display(arr)
