import tkinter as tk
from tkinter import *
from tkinter import filedialog
from convert import *

class Window:
    def __init__(self):
        self.convertor = Convert()

    def create_winodw(self):
        root = tk.Tk()

        label = Label(root, text='Image to ASCII Art', font=(32))
        label.pack()
        button = Button(root, text='Upload Image', command=self.upload, height=1, width=20)
        button.pack()

        root.mainloop()

    def upload(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath.endswith((".png", ".jpg")):
            self.convertor.image = Image.open(filepath)

        self.convertor.convert_image()