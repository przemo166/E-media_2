#!/usr/bin/python3

# Importing tkinter
import tkinter as eMedia
from tkinter import *
# end

# Import tkinter library to show MessageBox
from tkinter import messagebox
# end

# importing other libraries
from PIL import Image
from PIL import ImageTk
import numpy as np
import io
# end

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from saveNewPng import *
from bytesArray import *
from checkSignature import *
# end

# Saving encrypted file
def saveEncrypted(fileName,app,imageFrame,newImageName,currentImageFrame,textProgramInfo,encryptionMethodName):

    x = checkPng(fileName)

    if (x==True):

        if (encryptionMethodName=="RSA"):

            hexArray=imageConvert(fileName)
            position = hexArray.find("49444154")

            chunkLenght = hexArray[(position-8):position]
            chunkLenghtDecimal = int(chunkLenght,16)
            position+=8

            idatArray = hexArray[position:position+(chunkLenghtDecimal*2)]

            tmparray1 = hexArray[0:position]
            tmparray2 = hexArray[position+(chunkLenghtDecimal*2):len(hexArray)]


            finalArray = tmparray1 + idatArray + tmparray2

            print(finalArray)

            tmp=tmparray1[0]+tmparray1[1]
            print(tmp)
            print(type(tmp))

            tmpInt=int(tmp,16)
            print(tmpInt)
            print(type(tmpInt))


            savePngFile(finalArray,newImageName)

            image = Image.open('created_files/{}'.format(newImageName))
            photo = ImageTk.PhotoImage(image)

            labelImage = Label(master=imageFrame,image=photo,width=700,height=650)
            labelImage.image = photo
            labelImage.grid(row=0,column=0)

            currentImageLabel = Label(master=currentImageFrame,text=newImageName,font=('ariel',18,'bold'),bg='yellow',width=40)
            currentImageLabel.grid(row=0,column=0)

            textProgramInfo.delete(1.0,END)
            textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
            textProgramInfo.insert(eMedia.INSERT,"\n")
            textProgramInfo.insert(eMedia.INSERT,"encrypted successfully")

        else :
            messagebox.showinfo("Powiadomienie", "{}\nnieprawidłowa metoda !".format(fileName))

            textProgramInfo.delete(1.0,END)
            textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
            textProgramInfo.insert(eMedia.INSERT,"\n")
            textProgramInfo.insert(eMedia.INSERT,"encryttion error")

    else:
        messagebox.showinfo("Powiadomienie", "{}\nto nie plik formatu png. !".format(fileName))

        textProgramInfo.delete(1.0,END)
        textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
        textProgramInfo.insert(eMedia.INSERT,"\n")
        textProgramInfo.insert(eMedia.INSERT,"loading error")
