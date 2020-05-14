#!/usr/bin/python3

# Function that saves new png file in directory created files
def savePngFile1(hexArray: str, newFileName: str):

        with open('binaryFile') as file:
            data = file.read()

        data = bytes.fromhex(hexArray)

        tmpStr = "encrypted/" + newFileName

        with open(tmpStr, 'wb') as file:
            file.write(data)

def savePngFile2(hexArray: str, newFileName: str):

        with open('binaryFile') as file:
            data = file.read()

        data = bytes.fromhex(hexArray)

        tmpStr = "decrypted/" + newFileName

        with open(tmpStr, 'wb') as file:
            file.write(data)
