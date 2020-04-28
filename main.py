#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("functions"))
from makeGui import *

# Initializing a main window
app = eMedia.Tk()
makeStartPage(app)

# Set-up the window
app.title("E_media etap 2")
app.geometry('1440x900')
app.resizable(False,False)
app.resizable(width=False, height=False)
app.mainloop()
