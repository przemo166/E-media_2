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
from generateRSAkeys import *
from otherRSAfunctions import *

# Variables to save p and q numbers
p = 0
q = 0
# end

# Generating big prime ints
p = generateRandomInt(12)
q = generateRandomInt(12)
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

# For testing purposes
print("Private RSA :")
print(privateRSA)
print("Public RSA :")
print(publicRSA)
# end

# Testing RSA on simple example
print("Zakodowana liczba (123) :")
tmp=encryptRSA(publicRSA,123)
print(tmp)

print("Odkodowana liczba : ")
tmp =decryptRSA(privateRSA,tmp)
print(tmp)
# end

# Initializing a main window
app = eMedia.Tk()

# Making start gui function
makeStartPage(app)
# end

# Set-up the window
app.title("E_media etap 2")
app.geometry('1440x980')
app.resizable(False,False)
app.resizable(width=False, height=False)
app.mainloop()
