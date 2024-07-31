import os
from PIL import Image
from PIL import ImageFile
import matplotlib.pyplot as plt

# open image
image = Image.open('test.jpg') 

# show image before converting
plt.imshow(image)
plt.show()

# get width and height
w, h = image.size
print(w)
print(h)

# get pixel values
pixels = []
px = image.load()

for i in range(h):
    row = []
    for j in range(w):
        row.append(px[j, i])
    pixels.append(row)
print(pixels)