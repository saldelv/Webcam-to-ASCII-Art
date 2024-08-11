import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from convert import *

class Window:
    def __init__(self):
        self.convertor = Convert()
        self.color_var = None
        self.size_var = None
        self.brightness_var = None
        self.image_label = None

    def create_winodw(self):
        root = tk.Tk()

        label = Label(root, text='Image to ASCII Art', font=(32))
        label.pack()

        self.color_var = tk.BooleanVar()
        color_button = Checkbutton(root, text="Color (slower)", 
                                   variable=self.color_var, 
                                   offvalue=False, 
                                   onvalue=True, 
                                   height=2)
        color_button.pack()

        self.size_var = tk.BooleanVar()
        size_button = Checkbutton(root, text="Double size (slower)", 
                                   variable=self.size_var, 
                                   offvalue=False, 
                                   onvalue=True, 
                                   height=2)
        size_button.pack()

        self.brightness_var = tk.IntVar()
        brightness_button = Checkbutton(root, text="Invert brightness", 
                                   variable=self.brightness_var, 
                                   offvalue=0, 
                                   onvalue=1, 
                                   height=2)
        brightness_button.pack()

        upload_button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        upload_button.pack()
        self.image_label = Label(text="")
        self.image_label.pack()

        webcam_button = Button(root, text='Use Webcam', command=self.webcam, height=1, width=20)
        webcam_button.pack()

        root.mainloop()

    def upload(self, event=None):
        self.convertor.color = self.color_var.get()
        self.convertor.brightness_type = self.brightness_var.get()
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            self.image_label.configure(text="")
            self.convertor.get_user_image(filepath)
            self.convertor.set_size(self.size_var.get())
            self.convertor.convert_image()
        else:
            self.image_label.configure(text="Invalid file type, please use .png or .jpg", fg="red")

    def webcam(self):
        self.convertor.color = self.color_var.get()
        self.convertor.brightness_type = self.brightness_var.get()
        self.convertor.start_webcam()
        while True:
            if self.convertor.get_webcam() == 0:
                break
            self.convertor.set_size(self.size_var.get())
            self.convertor.convert_image()
        self.convertor.cap.release()
        cv.destroyAllWindows()