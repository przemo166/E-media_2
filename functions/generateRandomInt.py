#!/usr/bin/python3
import random

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/"))
from checkIfPrime import *

# Generating big prime intigers
def generateRandomInt(bitsNumber):

    tmp=random.getrandbits(bitsNumber)

    check = checkPrime(tmp)

    if(tmp==True):
        return tmp

    else:
        generateRandomInt(bitsNumber)
