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
# end

# importing other libraries
from PIL import Image
from PIL import ImageTk
import numpy as np
import io
# end

# Loading png file into decimal array ( global variable named decinalArray )
def loadFile(fileName,app,imageFrame,currentImageFrame,textProgramInfo):

    x = checkPng(fileName)

    if (x==True):

        image = Image.open('example_files/{}'.format(fileName))
        photo = ImageTk.PhotoImage(image)

        labelImage = Label(master=imageFrame,image=photo,width=700,height=650)
        labelImage.image = photo
        labelImage.grid(row=0,column=0)

        currentImageLabel = Label(master=currentImageFrame,text=fileName,font=('ariel',18,'bold'),bg='yellow',width=40)
        currentImageLabel.grid(row=0,column=0)

        textProgramInfo.delete(1.0,END)
        textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"loaded successfully")

    else :
        messagebox.showinfo("Powiadomienie", "{}\nto nie plik formatu png. !".format(fileName))

        textProgramInfo.delete(1.0,END)
        textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"loading error")
