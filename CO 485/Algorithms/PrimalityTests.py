import random
import GCD
import Jacobi

def Fermat(n, r):
    for i in range(r):
        a = random.randint(2, n-2)
        gcd = GCD.GCD(a, n)
        if gcd > 1:
            return "n = {} is composite: gcd(a, n) > 1 where a = {} and n = {}".format(n, a, n)
        else:
            t = pow(a, n-1, n)
            if t != 1:
                return "n = {} is composite: Fermat witness a = {} for the compositeness of n = {}".format(n, a, n)
    return "n = {} is probably prime: no Fermat witness found in r = {} iterations".format(n, r)

def SolovayStrassen(n, r):
    for i in range(r):
        a = random.randint(2, n-2)
        gcd = GCD.GCD(a, n)
        if gcd > 1:
            return "n = {} is composite: gcd(a, n) > 1 where a = {} and n = {}".format(n, a, n)
        else:
            t = pow(a, int((n-1)/2), n)
            jacobi = Jacobi.Jacobi(a, n) % n
            if t != jacobi:
                return "n = {} is composite: Euler-Jacobi witness a = {} for the compositeness of n = {}".format(n, a, n)
    return "n = {} is probably prime: no Euler-Jacobi witness found in r = {} iterations".format(n, r)

def MillerRabin(n, r):
    d = n - 1
    s = 0
    while d % 2 == 0:
        if d == 0:
            break
        d = int(d / 2)
        s = s + 1
    for i in range(r):
        a = random.randint(2, n-2)
        gcd = GCD.GCD(a, n)
        if gcd > 1:
            return "n = {} is composite: gcd(a, n) > 1 where a = {} and n = {}".format(n, a, n)
        else:
            b = pow(a, d, n)
            if b == 1:
                continue
            count = 0
            for t in range(s):
                power = pow(b, 2**t, n)
                if power == -1 % n:
                    count = count + 1
            if count == 0:
                return "n = {} is composite: Miller-Rabin witness a = {} for the compositeness of n = {}".format(n, a, n)
    return "n = {} is probably prime: no Miller-Rabin witness found in r = {} iterations".format(n, r)