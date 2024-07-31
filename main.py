import os
import math
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

# get brightness values of each pixel, using average brightness
for i in range(len(pixels)):
    for j in range(len(pixels[i])):
        pixels[i][j] = (pixels[i][j][0] + pixels[i][j][1] + pixels[i][j][2]) / 3

# mapping brightness to characters
characters = ["'", "^", "\\", "\"", ",", ":", ";", "I", "1", "!", "i", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "|", "/", "t", "f", "j", "r", "x", "n", "u",
              "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B",
              "@", "$"]

for i in range(len(pixels)):
    row = "" 
    for j in range(len(pixels[i])):
        index = int(pixels[i][j] / 4)
        row = row + characters[index]
    print(row)
