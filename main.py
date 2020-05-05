#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("functions"))
from makeGui import *
from generateRandomInt import *

# Variables to save p and q numbers
p = 0
q = 0
# end

# Generating big prime ints
p = generateRandomInt(512)
q = generateRandomInt(512)
# end

# Initializing a main window
app = eMedia.Tk()

# Making start gui function
makeStartPage(app)
# end

# To test p and q while programming
print("P")
print(p)
print("Q")
print(q)
# end

# Set-up the window
app.title("E_media etap 2")
app.geometry('1440x980')
app.resizable(False,False)
app.resizable(width=False, height=False)
app.mainloop()
