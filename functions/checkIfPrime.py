#!/usr/bin/python3
from random import randrange

# Checking if our big number is prime
def checkPrime(n,k):

    # 2 is prime
    if n == 2:
        return True

    # 3 is prime
    if n == 3:
        return True

    # if it can be divided by 2 is not a prime
    if n <= 1 or n % 2 == 0:
        return False

    ################
    # Miller-Rabin #
    ################

    # k is a depth of testing

    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
