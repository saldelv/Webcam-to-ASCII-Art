import os
from PIL import Image
from PIL import ImageFile
import matplotlib.pyplot as plt

image = Image.open('test.jpg')

plt.imshow(image)
plt.show()

w, h = image.size
print(w)
print(h)