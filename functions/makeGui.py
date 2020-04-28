#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# A font constant
LARGE_FONT = ('Verdana',30)

def makeStartPage(app):

    # Creating widgets and frames
    fileNameFrame = eMedia.Frame(master=app)
    fileNameEntry = eMedia.Entry(master=fileNameFrame,font=LARGE_FONT)

    newFileNameFrame = eMedia.Frame(master=app)
    newFileNameEntry = eMedia.Entry(master=newFileNameFrame,font=LARGE_FONT)

    fileNameLabel = eMedia.Label(master=fileNameFrame, text="File name :",font=LARGE_FONT)
    newFileNameLabel = eMedia.Label(master=newFileNameFrame, text="New name:",font=LARGE_FONT)


    # Creating button
    btn_convert = eMedia.Button(
        master=app,
        text="ENTER",
        font=LARGE_FONT,
        command=lambda:do(app,fileNameEntry.get())
    )

    # Set-up the frames and widets
    fileNameFrame.grid(row=0, column=0, padx=10)
    fileNameEntry.grid(row=0, column=1, sticky="e",padx=5,pady=5)

    newFileNameFrame.grid(row=1, column=0, padx=10)
    newFileNameEntry.grid(row=0, column=1, sticky="e",padx=5,pady=5)

    fileNameLabel.grid(row=0, column=0, sticky="w",padx=5,pady=5)
    newFileNameLabel.grid(row=0, column=0, sticky="w",padx=5,pady=5)

    btn_convert.grid(row=1, column=1, pady=10)
