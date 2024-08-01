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

# get and resize width and height
w, h = image.size
print(w)
print(h)

if w % 2 != 0:
    w -= 1
if h % 2 != 0:
    h -= 1
while w > 300:
    w = w // 2
    h = h // 2
size = w, h
print(size)
image.thumbnail(size, Image.Resampling.LANCZOS)

# get pixel values
pixels = []
px = image.load()

for i in range(image.height):
    row = []
    for j in range(image.width):
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

art = ""
for i in range(len(pixels)):
    row = "" 
    for j in range(len(pixels[i])):
        index = int(pixels[i][j] / 4)
        row = row + characters[index]
    art = art + row + "\n"
print(art)
