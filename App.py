import tkinter as tk
from tkinter import filedialog
import sys
import os
import io
from PIL import Image
from io import BytesIO
from PicForm import PicForm
from KeyLog import Keylog
from Registry import Registry
from ListApp import ListApp
from Kill import Kill
from Process import Process

def butApp():
    print("App Running")
    viewApp = ListApp()

def butConnect():
    print("Kết nối")

def txtIP():
    print("Nhập IP")

def butTat():
    print("Tắt máy")

def butReg():
    print("Sửa registry")
    reg = Registry()
    
def butExit():
    print("Thoát")

def butPic():
    print("Chụp màn hình")
    pic_form = PicForm()

def butKeyLock():
    print("Keystroke")
    key_log = Keylog()


def butProcess():
    print("Process Running")
    run = Process()

def SuspendLayout():
    print("Suspend")
    
root = tk.Tk()  # create parent window

butApp = tk.Button(root, text="App Running", command=butApp)
butApp.pack()

butConnect = tk.Button(root, text="Kết nối", command=butConnect)
butConnect.pack()

txtIP = tk.Label(root, text="Nhập IP", bg="lightgrey")
txtIP.pack()

butTat = tk.Button(root, text="Tắt máy", command=butTat)
butTat.pack()

butReg = tk.Button(root, text="Sửa registry", command=butReg)
butReg.pack()

butExit = tk.Button(root, text="Thoát", command=root.quit)
butExit.pack()

butPic = tk.Button(root, text="Chụp màn hình", command=butPic)
butPic.pack()

butKeyLock = tk.Button(root, text="Keystroke", command=butKeyLock)
butKeyLock.pack()

butProcess = tk.Button(root, text="Process Running", command=butProcess)
butProcess.pack()

root.mainloop()