import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from convert import *

class Window:
    def __init__(self):
        self.convertor = Convert()
        self.color_var = None

    def create_winodw(self):
        root = tk.Tk()

        label = Label(root, text='Image to ASCII Art', font=(32))
        label.pack()
        self.color_var = tk.BooleanVar()
        color_button = Checkbutton(root, text="Color (slower)", 
                                   variable=self.color_var, 
                                   offvalue=False, 
                                   onvalue=True, 
                                   height=2, 
                                   width=10)
        color_button.pack()
        upload_button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        upload_button.pack()
        webcam_button = Button(root, text='Use Webcam', command=self.webcam, height=1, width=20)
        webcam_button.pack()

        root.mainloop()

    def upload(self, event=None):
        self.convertor.color = self.color_var.get()
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            self.convertor.get_user_image(filepath)
            self.convertor.set_size()
            self.convertor.convert_image()

    def webcam(self):
        self.convertor.color = self.color_var.get()
        self.convertor.start_webcam()
        while True:
            if self.convertor.get_webcam() == 0:
                break
            self.convertor.set_size()
            self.convertor.convert_image()
        self.convertor.cap.release()
        cv.destroyAllWindows()