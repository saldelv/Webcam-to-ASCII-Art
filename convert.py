import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import cv2 as cv
from constants import *


class Convert:
    def __init__(self):
        self.webcam = False
        self.color = False
        self.brightness = 0
        self.image = None

    def get_user_image(self):
        # open image
        self.image = Image.open('test.jpg') 

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
        # get pixel values
        pixels = []
        px = self.image.load()

        for i in range(self.image.height):
            row = []
            for j in range(self.image.width):
                row.append(px[j, i])
            pixels.append(row)

        # get brightness values of each pixel, using average brightness
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j] = (pixels[i][j][0] + pixels[i][j][1] + pixels[i][j][2]) / 3

        art = ""
        for i in range(len(pixels)):
            row = "" 
            for j in range(len(pixels[i])):
                index = int(pixels[i][j] / 4)
                row = row + characters[index]
            art = art + row + "\n"
        print(art)

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