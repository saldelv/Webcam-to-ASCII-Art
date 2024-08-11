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

        # title text
        label = Label(root, text='Webcam to ASCII Art', font=(32))
        label.pack()

        # check boxes for color, brightness, and size values
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

        # button for uploading an image
        upload_button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        upload_button.pack()
        self.image_label = Label(text="")
        self.image_label.pack()

        # button for using webcam
        webcam_button = Button(root, text='Use Webcam', command=self.webcam, height=1, width=20)
        webcam_button.pack()

        root.mainloop()

    def upload(self, event=None):
        # gets color and brightness selections
        self.convertor.color = self.color_var.get()
        self.convertor.brightness_type = self.brightness_var.get()

        # opens file search for image
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            # analyzes and converts image
            self.image_label.configure(text="")
            self.convertor.get_user_image(filepath)
            self.convertor.set_size(self.size_var.get())
            self.convertor.convert_image()
        else:
            # tells user what file types to use if the type selected in wrong
            self.image_label.configure(text="Invalid file type, please use .png or .jpg", fg="red")

    def webcam(self):
        # gets color and brightness selections
        self.convertor.color = self.color_var.get()
        self.convertor.brightness_type = self.brightness_var.get()

        # starts webcam video capture
        self.convertor.start_webcam()
        while True:
            # checks if webcam window was closed
            if self.convertor.get_webcam() == 0:
                break

            # converts each frame of webcam video
            self.convertor.set_size(self.size_var.get())
            self.convertor.convert_image()
        # stops webcam capture
        self.convertor.cap.release()
        cv.destroyAllWindows()