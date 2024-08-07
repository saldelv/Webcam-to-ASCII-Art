import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from convert import *

class Window:
    def __init__(self):
        self.convertor = Convert()

    def create_winodw(self):
        root = tk.Tk()
        root.configure(background='black')

        label = Label(root, text='Image to ASCII Art', font=(32), fg="white", background='black')
        label.pack()
        upload_button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        upload_button.pack()
        webcam_button = Button(root, text='Use Webcam', command=self.webcam, height=1, width=20)
        webcam_button.pack()

        root.mainloop()

    def upload(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            self.convertor.get_user_image(filepath)
            self.convertor.set_size()
            self.convertor.convert_image()

    def webcam(self):
        self.convertor.start_webcam()
        while True:
            if self.convertor.get_webcam() == 0:
                break
            self.convertor.set_size()
            self.convertor.convert_image()
        self.convertor.cap.release()
        cv.destroyAllWindows()