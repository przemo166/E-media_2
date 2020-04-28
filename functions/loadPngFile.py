#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# importing other libraries
from PIL import Image
from PIL import ImageTk
import numpy as np
import io

# Loading png file into decimal array ( global variable named decinalArray )
def loadFile(fileName,app,imageFrame,currentImageFrame):

    image = Image.open('example_files/{}'.format(fileName))
    photo = ImageTk.PhotoImage(image)

    labelImage = Label(master=imageFrame,image=photo,width=700,height=650)
    labelImage.image = photo
    labelImage.grid(row=0,column=0)

    currentImageLabel = Label(master=currentImageFrame,text=fileName,font=('ariel',18,'bold'),bg='yellow',width=40)
    currentImageLabel.grid(row=0,column=0)
