from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor


sb = ScrapBooker()

imp = ImageProcessor()
arr = imp.load("42AI.png")
print(arr)
arr = sb.crop(arr, (50, 150), (50, 50))
imp.display(arr)
