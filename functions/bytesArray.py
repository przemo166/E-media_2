#!/usr/bin/python3

# Function that is converting an image into bytes array
def imageConvert(imageName):
    with open("example_files/{}".format(imageName), "rb") as image:
          f = image.read().hex()
          return(f)
