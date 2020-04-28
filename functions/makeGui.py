#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from loadPngFile import *
from saveEncrypted import *
from saveDecrypted import *

# A font constant
LARGE_FONT = ('Verdana',30)

def makeStartPage(app):

    # Creating widgets and frames

    # FileNameFrame
    fileNameFrame = eMedia.Frame(master=app)
    fileNameEntry = eMedia.Entry(master=fileNameFrame,font=LARGE_FONT)
    fileNameLabel = eMedia.Label(master=fileNameFrame, text="File name :  ",font=LARGE_FONT)

    fileNameLabel.grid(row=0,column=0)
    fileNameEntry.grid(row=0,column=1)
    fileNameFrame.pack(padx=10,pady=10)
    # end

    # NewFilenameFrame
    newFileNameFrame = eMedia.Frame(master=app)
    newFileNameEntry = eMedia.Entry(master=newFileNameFrame,font=LARGE_FONT)
    newFileNameLabel = eMedia.Label(master=newFileNameFrame, text="New name:  ",font=LARGE_FONT)

    newFileNameLabel.grid(row=0,column=0)
    newFileNameEntry.grid(row=0,column=1)
    newFileNameFrame.pack(padx=10,pady=10)
    # end

    # Buttons frame
    buttonsFrame = eMedia.Frame(master=app)

    btnLoadFile = eMedia.Button(
        master=buttonsFrame,
        text="LOAD",
        font=LARGE_FONT,
        command=lambda:loadFile(fileNameEntry.get(),app,imageFrame,currentImageFrame)
        )

    btnEncrypt = eMedia.Button(
        master=buttonsFrame,
        text="ENCRYPT",
        font=LARGE_FONT,
        foreground="white",
        background="red",
        command=lambda:saveEncrypted(fileNameEntry.get(),app,imageFrame,newFileNameEntry.get(),currentImageFrame)
        )

    btnDecrypt = eMedia.Button(
        master=buttonsFrame,
        text="DECRYPT",
        font=LARGE_FONT,
        foreground="white",
        background="green",
        command=lambda:saveDecrypted(newFileNameEntry.get(),app,imageFrame,currentImageFrame)
        )

    btnLoadFile.grid(row=0,column=0,padx=5,pady=5)
    btnEncrypt.grid(row=0,column=1,padx=5,pady=5)
    btnDecrypt.grid(row=0,column=2,padx=5,pady=5)

    buttonsFrame.pack(padx=10,pady=10)
    # end

    # ImageFrame
    imageFrame = eMedia.Frame(master=app)
    imageFrame.pack()
    # end

    # CurrentImageFrame
    currentImageFrame = eMedia.Frame(master=app)
    currentImageFrame.pack()
    # end
