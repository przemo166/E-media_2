#!/usr/bin/python3

# Import tkinter library to show MessageBox
from tkinter import messagebox
# end


# Functions that check if our file is png file
def checkPngFirst (imageName):

    with open('example_files/{}'.format(imageName), 'rb') as f:
        hexData = f.read().hex()
        if hexData[0:16] != "89504e470d0a1a0a":
            return False
        else:
            return True

def checkPngSecond (imageName):

    with open('encrypted/{}'.format(imageName), 'rb') as f:
        hexData = f.read().hex()
        if hexData[0:16] != "89504e470d0a1a0a":
            return False
        else:
            return True
