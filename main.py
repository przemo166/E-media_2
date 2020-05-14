#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *
# end

# Importing time library
import time
# end

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("functions"))
from makeGui import *
from generateRandomInt import *
from generateRSAkeys import *
from otherRSAfunctions import *
from showInfo import *
# end

# Variables to save p and q numbers
p = 0
q = 0
# end

# Generating big prime ints
p = generateRandomInt(512)
q = generateRandomInt(512)
# end

# Variables to save public and private RSA key
privateRSA = [0,0]
publicRSA = [0,0]
# end

# Generating public and private RSA keys
generatePrivateAndPublicKeys(privateRSA,publicRSA,p,q)
# end

# Delete p and q after generating public and private RSA key
p = 0
q = 0
# end

# For testing purposes (showing in a background terminal)
printRsaKeys(privateRSA,publicRSA)
# end

# Initializing a main window
app = eMedia.Tk()

# Making start gui function
makeStartPage(app,privateRSA,publicRSA)
# end

# Set-up the window
app.title("E_media etap 2")
app.geometry('1440x980')
app.resizable(False,False)
app.resizable(width=False, height=False)
app.mainloop()
