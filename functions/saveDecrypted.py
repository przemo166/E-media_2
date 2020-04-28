#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *

# importing other libraries
from PIL import Image
from PIL import ImageTk
import numpy as np
import io

# Saving decrypted file
def saveDecrypted(fileName,app,imageFrame,currentImageFrame):

    with open('created_files/{}'.format(fileName), "rb") as image:
        f = image.read()
        decimalArray = bytearray(f)

    image = Image.open(io.BytesIO(decimalArray))
    image.save('created_files/{}'.format(fileName))

    image = Image.open('created_files/{}'.format(fileName))
    photo = ImageTk.PhotoImage(image)

    labelImage = Label(master=imageFrame,image=photo,width=700,height=650)
    labelImage.image = photo
    labelImage.grid(row=0,column=0)

    currentImageLabel = Label(master=currentImageFrame,text=fileName,font=('ariel',18,'bold'),bg='yellow',width=40)
    currentImageLabel.grid(row=0,column=0)
