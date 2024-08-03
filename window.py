import tkinter as tk
from tkinter import *
from tkinter import filedialog
from convert import *

class Window:
    def __init__(self):
        self.convertor = Convert()
        self.print_label = None

    def create_winodw(self):
        root = tk.Tk()
        root.configure(background='black')

        label = Label(root, text='Image to ASCII Art', font=(32), fg="white", background='black')
        label.pack()
        upload_button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        upload_button.pack()
        webcam_button = Button(root, text='Use Webcam', command=self.webcam, height=1, width=20)
        webcam_button.pack()

        self.print_label = Label(root, text="", justify=LEFT, fg="white", background='black')
        self.print_label.pack()

        root.mainloop()

    def upload(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            image = Image.open(filepath)
            self.convertor.get_user_image(image)
            self.print_label.configure(text=self.convertor.convert_image(), font=('Consolas', 2))

    def webcam(self):
        self.convertor.get_webcam()
        self.print_label.configure(text=self.convertor.convert_image())