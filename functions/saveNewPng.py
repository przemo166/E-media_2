#!/usr/bin/python3

# Function that saves new png file
def savePngFile(hexArray: str, newFileName: str):

        with open('binaryFile') as file:
            data = file.read()

        data = bytes.fromhex(hexArray)

        tmpStr = "created_files/" + newFileName

        with open(tmpStr, 'wb') as file:
            file.write(data)
