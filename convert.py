import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import cv2 as cv
from constants import *
from colorama import init

class Convert:
    def __init__(self):
        self.webcam = False
        self.color = False
        self.brightness = 0
        self.image = None

    def get_user_image(self, image):
        # open image
        self.image = image

        # show image before converting
        plt.imshow(self.image)
        plt.show()

    def get_webcam(self):
        # get webcam footage
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            exit()

        ret, frame = cap.read()

        if not ret:
            exit()

        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.image = Image.fromarray(frame)

        # show image before converting
        plt.imshow(self.image)
        plt.show()

    def convert_image(self):
        #enable ANSI
        init()

        # get pixel values
        pixels = []
        px = self.image.load()

        for i in range(self.image.height):
            row = []
            for j in range(self.image.width):
                row.append(px[j, i])
            pixels.append(row)

        # get brightness values of each pixel, using average brightness
        brightness = [i[:] for i in pixels]
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                brightness[i][j] = (pixels[i][j][0] + pixels[i][j][1] + pixels[i][j][2]) / 3

        art = ""
        for i in range(len(pixels)):
            row = "" 
            for j in range(len(brightness[i])):
                index = int(brightness[i][j] / 4)
                r = pixels[i][j][0]
                g = pixels[i][j][1]
                b = pixels[i][j][2]
                next = f"\033[38;2;{r};{g};{b}m{characters[index]}\033[0m"
                row = row + next
            art = art + row + "\n"
        print(art)
        return art

    def set_size(self):
        # get and resize width and height
        w, h = self.image.size
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
        self.image.thumbnail(size, Image.Resampling.LANCZOS)