import sys
import os
import io
# from PIL import Image
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import *
from tkinter import filedialog
import pyautogui

class PicForm:
    def __init__(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.picture = Label(self.root)
        self.picture.pack()
        
        self.butTake = Button(self.root, text="Take", command=self.lam)
        self.butTake.pack()
        
        self.button1 = Button(self.root, text="Save", command=self.save_image)
        self.button1.pack()
        
        self.root.mainloop()
    
    def lam(self):
        image = pyautogui.screenshot()
        # image.save("SS1.jpg")
        # s = "TAKE"
        # Program.nw.write(s + "\n")
        # Program.nw.flush()
        
        # s = Program.nr.readline()
        # data = bytearray(int(s))
        # rec = Program.client.recv_into(data)
        
        # image = Image.open(io.BytesIO(data))
        self.picture.image = ImageTk.PhotoImage(image)
        self.picture.configure(image=self.picture.image)
    
    def save_image(self):
        save_path = filedialog.asksaveasfilename(filetypes=[("Bmp files", "*.Bmp"), ("All files", "*.*")])
        if save_path:
            self.picture.image.save(save_path, "PNG")
    
    def on_close(self):
        s = "QUIT"
        # Program.nw.write(s + "\n")
        # Program.nw.flush()
        self.root.destroy()

if __name__ == "__main__":
    pic_form = PicForm()