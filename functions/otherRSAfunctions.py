#!/usr/bin/python3

def encryptRSA (publicKey,tmpNumber):
    m = hex(pow(tmpNumber,publicKey[0],publicKey[1])).rstrip("L")
    tmp = int(m,0)
    return tmp

def decryptRSA (privateKey,tmpNumber):
    m = hex(pow(tmpNumber,privateKey[0],privateKey[1])).rstrip("L")
    tmp = int(m,0)
    return tmp
