#!/usr/bin/python3

# Function that checks if our file is png file
def checkPng (imageName):
    with open('example_files/{}'.format(imageName), 'rb') as f:
        hexData = f.read().hex()
    if hexData[0:16] != "89504e470d0a1a0a":
        return False
    else:
        return True
