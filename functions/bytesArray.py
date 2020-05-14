#!/usr/bin/python3

# Functions that are converting an image into bytes array
def imageConvertFirst(imageName):
    with open("example_files/{}".format(imageName), "rb") as image:
          f = image.read().hex()
          return(f)

def imageConvertSecond(imageName):
    with open("encrypted/{}".format(imageName), "rb") as image:
          f = image.read().hex()
          return(f)
