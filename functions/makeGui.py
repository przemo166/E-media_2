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

def makeStartPage(app,privateRSA,publicRSA):

    # Creating widgets and frames

    # FileNameFrame
    fileNameFrame = eMedia.Frame(master=app)
    fileNameEntry = eMedia.Entry(master=fileNameFrame,font=LARGE_FONT,width=15)
    fileNameLabel = eMedia.Label(master=fileNameFrame, text="File name :  ",font=LARGE_FONT)

    fileNameLabel.grid(row=0,column=0)
    fileNameEntry.grid(row=0,column=1)

    newFileNameFrame = eMedia.Frame(master=app)
    newFileNameEntry = eMedia.Entry(master=fileNameFrame,font=LARGE_FONT,width=15)
    newFileNameLabel = eMedia.Label(master=fileNameFrame, text="  New name:  ",font=LARGE_FONT)

    newFileNameLabel.grid(row=0,column=2)
    newFileNameEntry.grid(row=0,column=3)

    fileNameFrame.pack(padx=10,pady=10)
    # end
    encryptionMethod = eMedia.Frame(master=app)
    encryptionMethodLabel = eMedia.Label(master=encryptionMethod, text="Encryption method:  ",font=LARGE_FONT)

    encryptionMethodEntry = eMedia.Entry(master=encryptionMethod,font=LARGE_FONT,width=15)

    encryptionMethodLabel.grid(row=0,column=0)
    encryptionMethodEntry.grid(row=0,column=1)

    encryptionMethod.pack(padx=10,pady=10)
    # EncryptionMethodFrame

    # end

    # Buttons frame and label and text program info
    buttonsFrame = eMedia.Frame(master=app)

    btnLoadFile = eMedia.Button(
        master=buttonsFrame,
        text="LOAD",
        font=LARGE_FONT,
        command=lambda:loadFile(fileNameEntry.get(),app,imageFrame,currentImageFrame,textProgramInfo)
        )

    btnEncrypt = eMedia.Button(
        master=buttonsFrame,
        text="ENCRYPT",
        font=LARGE_FONT,
        foreground="white",
        background="red",
        command=lambda:saveEncrypted(fileNameEntry.get(),app,imageFrame,newFileNameEntry.get(),
                                        currentImageFrame,textProgramInfo,encryptionMethodEntry.get(),
                                        publicRSA)
        )

    btnDecrypt = eMedia.Button(
        master=buttonsFrame,
        text="DECRYPT",
        font=LARGE_FONT,
        foreground="white",
        background="green",
        command=lambda:saveDecrypted(newFileNameEntry.get(),app,imageFrame,currentImageFrame,encryptionMethodEntry.get(),privateRSA,
                                        textProgramInfo)
        )

    programInfoLabel = eMedia.Label(master=buttonsFrame, text="Program info: ",font=LARGE_FONT)
    textProgramInfo = eMedia.Text(master=buttonsFrame,height=2,width=25)
    textProgramInfo.configure(font=("Times New Roman", 28, "bold"))

    btnLoadFile.grid(row=0,column=0,padx=5,pady=5)
    btnEncrypt.grid(row=0,column=1,padx=5,pady=5)
    btnDecrypt.grid(row=0,column=2,padx=5,pady=5)
    programInfoLabel.grid(row=0,column=3,padx=20,pady=5)
    textProgramInfo.grid(row=0,column=4,padx=5,pady=5)

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
