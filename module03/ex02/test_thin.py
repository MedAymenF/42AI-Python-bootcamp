from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()

imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
arr = sb.thin(arr, 3, 0)
imp.display(arr)
