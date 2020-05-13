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

def encryptBlock(block,n,e):

    blockInt= int(block,16)
    encryptedBlock = encryptRSA(blockInt,publicRSA[1],publicRSA[0])
    hexBlock = format(encryptedBlock,'x')
    length = len(hexBlock)
    if length % 2 != 0:
        hexBlock = '0' + hexBlock
    return hexBlock

# Saving encrypted file
def saveEncrypted(fileName,app,imageFrame,newImageName,currentImageFrame,textProgramInfo,encryptionMethodName,privateRSA,publicRSA):

    x = checkPng(fileName)

    if (x==True):

        if (encryptionMethodName=="RSA"):

            # Tak było

            hexArray=imageConvert(fileName)
            position = hexArray.find("49444154")

            chunkLenght = hexArray[(position-8):position]
            chunkLenghtDecimal = int(chunkLenght,16)
            #position+=8

            realLength = 2 * chunkLenghtDecimal
            idatHex = hexArray[(position+8):(position + 8 + realLength)]
            newIDAT = ''
            i = 0

            print("\n")
            print(idatHex)
            print("\n")

            tmp = idatHex[4:6]
            print("\nhexArray[0] in hex : ", tmp)

            tmpInt = int(tmp,16)
            tmpCoded = encryptRSA(publicRSA,tmpInt)
            print("\nhexArray[0] coded in int :",tmpCoded)

            tmpCodedHex =format(tmpCoded,'x')
            print("\nhexArray[0]  coded in hex : ",tmpCodedHex)


            print("\nhexArray[0] encoded in int : ")
            tmpEncodedInt = decryptRSA(privateRSA,int(tmpCoded))
            print(tmpEncodedInt)

            tmpEncodedHex = format(tmpEncodedInt,'x')

            length = len(tmpEncodedHex)
            #print(length)

            if length % 2 == 1 :
                tmpEncodedHex = '0' + tmpEncodedHex

            print("\nhexArray[0] encoded in hex : ")
            print(tmpEncodedHex)

            i=0

            for i in range(0,4):
                newIDAT+=tmpCodedHex

            print("NewIdat : ", newIDAT)

            tmp22=newIDAT[0]
            print(tmp22)

            #savePngFile(newFile,newImageName)

            #image = Image.open('created_files/{}'.format(newImageName))
            #photo = ImageTk.PhotoImage(image)

            #labelImage = Label(master=imageFrame,image=photo,width=700,height=650)
            #labelImage.image = photo
            #labelImage.grid(row=0,column=0)

            #currentImageLabel = Label(master=currentImageFrame,text=newImageName,font=('ariel',18,'bold'),bg='yellow',width=40)
            #currentImageLabel.grid(row=0,column=0)

            #textProgramInfo.delete(1.0,END)
            #textProgramInfo.insert(eMedia.INSERT,"{}".format(fileName))
            #textProgramInfo.insert(eMedia.INSERT,"\n")
            #textProgramInfo.insert(eMedia.INSERT,"encrypted successfully")

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
