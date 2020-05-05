#!/usr/bin/python3
import math

# Checking if our big number is prime
def checkPrime(randomNumber):

    if randomNumber == 1:
        return False

    if randomNumber == 2:
        return True

    if randomNumber > 2 and randomNumber % 2 == 0:
        return False

    maxDivisor = math.floor(math.sqrt(randomNumber))
    for d in range(3,1+maxDivisor,2):
        if randomNumber % d == 0:
            return False

    return True
