#!/usr/bin/python3s
import random

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from checkIfPrime import *

# Generating big prime intigers
def generateRandomInt(bitsNumber):

    tmpRandomInt=random.getrandbits(bitsNumber)

    while not checkPrime(tmpRandomInt, 128):
        tmpRandomInt=random.getrandbits(bitsNumber)
    return tmpRandomInt
