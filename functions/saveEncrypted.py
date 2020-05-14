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
from otherRSAfunctions import *
# end

# Saving encrypted file
def saveEncrypted(fileName,app,imageFrame,newImageName,currentImageFrame,textProgramInfo,encryptionMethodName,publicRSA,moduleLengthEntry):

    x = checkPngFirst(fileName)

    if (x==True):

        if (encryptionMethodName=="RSA"):

            hexArray=imageConvertFirst(fileName)
            position = hexArray.find("49444154")

            chunkLenght = hexArray[(position-8):position]
            chunkLenghtDecimal = int(chunkLenght,16)

            realLength = 2 * chunkLenghtDecimal
            idatHex = hexArray[(position+8):(position + 8 + realLength)]
            newIDAT = ''

            length = len(idatHex)
            tmp = ''

            moduleLengthEntryInt = int(moduleLengthEntry)
            tmpInt = int(length/2)

            if( (tmpInt % moduleLengthEntryInt) != 0 ):
                messagebox.showinfo("Powiadomienie", "{}\nŹle dobrany x !".format(encryptionMethodName))

            else :

                if length % 8 != 0 :

                    for j in range(0,(8-length%8)):
                        tmp = '0' + tmp

                i = 0

                while i < realLength:

                    block = idatHex[i:i+moduleLengthEntryInt]
                    blockInt = int(block,16)
                    blockCodedInt = encryptRSA(publicRSA,blockInt)
                    blockCodedHex = format(blockCodedInt,'x')

                    j = 0

                    length = len(blockCodedHex)

                    if length % 256 != 0 :

                        for j in range(0,(256-length%256)):
                            blockCodedHex = '0' + blockCodedHex

                    i+=moduleLengthEntryInt

                    newIDAT += blockCodedHex

                newIdatLength = int(len(newIDAT)/2)
                newIdatLengthHex = format(newIdatLength,'x')

                length = len(newIdatLengthHex)

                if length % 8 != 0 :

                    for j in range(0,(8-length%8)):
                        newIdatLengthHex = '0' + newIdatLengthHex

                newFile = hexArray[0:(position-8)]
                newFile += newIdatLengthHex
                newFile += hexArray[position:(position+8)]
                newFile += newIDAT
                newFile += hexArray[(position+realLength+8):]

                savePngFile1(newFile,newImageName)

                image = Image.open('example_files/{}'.format('encrypted.png'))
                photo = ImageTk.PhotoImage(image)

                labelImage = Label(master=imageFrame,image=photo,width=700,height=700)
                labelImage.image = photo
                labelImage.grid(row=0,column=0)

                currentImageLabel = Label(master=currentImageFrame,text=newImageName,font=('ariel',18,'bold'),bg='yellow',width=40)
                currentImageLabel.grid(row=0,column=0)

                textProgramInfo.delete(1.0,END)
                textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
                textProgramInfo.insert(eMedia.INSERT,"\n")
                textProgramInfo.insert(eMedia.INSERT,"encrypted successfully")

        else :
            messagebox.showinfo("Powiadomienie", "{}\nnieprawidłowa metoda !".format(encryptionMethodName))

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
