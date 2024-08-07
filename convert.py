import cv2 as cv
from colorama import init
from constants import *

class Convert:
    def __init__(self):
        self.webcam = False
        self.color = False
        self.brightness_type = 0
        self.image = None
        self.cap = None
        self.console = None

    def get_user_image(self, filepath):
        # open image
        image = cv.imread(filepath)

        if not self.color:
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        self.image = image
        # show image before converting
        cv.imshow('image', self.image)

    def start_webcam(self):
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened():
            exit()

        cv.namedWindow("webcam")

    def get_webcam(self):
        # get webcam footage
        ret, frame = self.cap.read()

        if not ret:
            exit()

        if self.color:
            frame_color = frame
        else:
            frame_color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        self.image = frame_color

        # show image before converting
        cv.imshow('webcam', self.image)

        if cv.waitKey(1) & 0xFF == ord('q'):
            return 0

    def convert_image(self):
        # enable ANSI
        init()

        # convert image to ascii
        art = ""
        for i in range(self.image.shape[0]):
            row = ""
            for j in range(self.image.shape[1]):
                if self.color:
                    brightness = (self.image[i][j][0] + self.image[i][j][1] + self.image[i][j][2]) / 3
                    index = int(brightness / 4)
                    if self.brightness_type == 1:
                        index = len(characters) - index
                    next = f"\033[38;2;{self.image[i, j][0]};{self.image[i, j][1]};{self.image[i, j][2]}m{characters[index] * 2}\033[0m"
                else:
                    brightness = self.image[i][j]
                    index = int(brightness / 4)
                    if self.brightness_type == 1:
                        index = len(characters) - index
                    next = characters[index] * 2
                row = row + next
            art = art + row + "\n"
        #print(chr(27) + "[2J")
        print(art)

    def set_size(self):
        # get and resize width and height
        w = 80
        h = 60
        self.image = cv.resize(self.image, (w, h))