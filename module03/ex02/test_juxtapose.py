from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()

imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
arr = sb.juxtapose(arr, 3, 1)
imp.display(arr)
