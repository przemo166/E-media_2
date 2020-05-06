#!/usr/bin/python3

# NWD function for two intigers
def nwd (a,b):
    while b:
        a, b = b, a%b
    return a

# Function for inverse calculation of modulo n
def moduleInverse (a,n):

    a0 = a
    n0 = n
    p0 = 0
    p1 = 1
    q = int(n0 / a0)
    r = n0 % a0

    while r > 0:
        t = p0 - (q * p1)
        if(t>=0):
            t = t % n
        else:
            t = n - ((-t) % n )

        p0 = p1
        p1 = t
        n0 = a0
        a0 = r
        q = int(n0 / a0)
        r = n0 % a0

    return p1

def generatePrivateAndPublicKeys(privateRSA,publicRSA,p,q):

    phi = (p-1)*(q-1)
    n   = p * q

    e = 3

    # Calculating e
    while nwd(e,phi) != 1:
        e+=2

    # Calculating d
    d = moduleInverse(e,phi)

    privateRSA[0] = d
    privateRSA[1] = n

    publicRSA[0] = e
    publicRSA[1] = n
