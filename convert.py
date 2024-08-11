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

        # show image before converting
        cv.imshow('image', image)

        # convert to correct color setting
        if self.color:
            image_color = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        else:
            image_color = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        
        # save opened image as class variable
        self.image = image_color

    def start_webcam(self):
        # start webcam capture
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened():
            exit()

        cv.namedWindow("webcam")

    def get_webcam(self):
        # get current webcam video frame
        ret, frame = self.cap.read()

        if not ret:
            exit()

        # show image before converting
        cv.imshow('webcam', frame)

        # convert to correct color setting
        if self.color:
            frame_color = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        else:
            frame_color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # save opened image as class variable
        self.image = frame_color

        # end webcam video if q is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            return 0

    def convert_image(self):
        # enable ANSI
        init()

        # convert image to ascii by checking if it needs color or inverted brightness, getting pixel brightness and asigning a character to it, and adding the character
        art = ""
        for i in range(self.image.shape[0]):
            row = ""
            for j in range(self.image.shape[1]):
                if self.color:
                    brightness = (self.image[i][j][0] + self.image[i][j][1] + self.image[i][j][2]) / 3
                    index = int(brightness / 3.93)
                    if self.brightness_type == 1:
                        index = len(characters) - index
                    next = f"\033[38;2;{self.image[i, j][0]};{self.image[i, j][1]};{self.image[i, j][2]}m{characters[index] * 2}\033[0m"
                else:
                    brightness = self.image[i][j]
                    index = int(brightness / 3.93)
                    if self.brightness_type == 1:
                        index = len(characters) - index
                    next = characters[index] * 2
                # add character to current row
                row = row + next
            # add row to next line of the ascii art
            art = art + row + "\n"
        # print finished ascii art
        print(art)

    def set_size(self, doubled):
        # get and resize width and height to work best in terminal
        w = 80
        h = 60
        if doubled:
            w *= 2
            h *= 2
        self.image = cv.resize(self.image, (w, h))