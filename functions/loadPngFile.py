#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *
# end

# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from checkSignature import *
from bytesArray import *
# end

# importing other libraries
from PIL import Image
from PIL import ImageTk
import numpy as np
import io
# end


# Loading png file and showing it in a label widget
def loadFile(fileName,app,imageFrame,currentImageFrame,textProgramInfo):

    x = checkPngFirst(fileName)

    if (x==True):

        hexArray=imageConvertFirst(fileName)
        position = hexArray.find("49444154")

        chunkLenght = hexArray[(position-8):position]
        chunkLenghtDecimal = int(chunkLenght,16)

        image = Image.open('example_files/{}'.format(fileName))
        photo = ImageTk.PhotoImage(image)

        labelImage = Label(master=imageFrame,image=photo,width=700,height=700)
        labelImage.image = photo
        labelImage.grid(row=0,column=0)

        currentImageLabel = Label(master=currentImageFrame,text=fileName,font=('ariel',15,'bold'),bg='yellow',width=40)
        currentImageLabel.grid(row=0,column=0)

        textProgramInfo.delete(1.0,END)
        textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"loaded successfully")
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"IDAT length : {}".format(chunkLenghtDecimal))


    else :
        messagebox.showinfo("Powiadomienie", "{}\nto nie plik formatu png. !".format(fileName))

        textProgramInfo.delete(1.0,END)
        textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"loading error")
