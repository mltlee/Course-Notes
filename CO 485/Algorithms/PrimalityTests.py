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

def MillerRabin(n, r, details = False):
    d = n - 1
    s = 0
    while d % 2 == 0:
        if d == 0:
            break
        d = int(d / 2)
        s = s + 1
    if details:
        print()
        print("Input n = {}, r = {}".format(n, r))
        print("n - 1 = 2^s * d where s = {}, d = {}".format(s, d))
    for i in range(r):
        a = random.randint(2, n-2)
        if details:
            print()
            print("Iteration {}: a = {} selected".format(i+1, a))
            print("---------------------------------")
        gcd = GCD.GCD(a, n)
        if gcd > 1:
            print("n = {} is composite: gcd(a, n) > 1 where a = {} and n = {}".format(n, a, n))
            return 
        else:
            b = pow(a, d, n)
            if details: 
                print("b = a^d (mod n) = {}".format(b))
            if b == 1:
                if details:
                    print("b = {} is congruent to 1 mod n, so a = {} is not a Miller-Rabin witness".format(b, a))
                continue
            if details:
                print("b = {} is not congruent to 1 mod n".format(b))
                print("Computing b^(2^t) for 0 <= t <= s-1:")
            count = 0
            for t in range(s):
                power = pow(b, 2**t, n)
                if details:
                    print("b^(2^{}) (mod n) = {}".format(t, power))
                if power == -1 % n and count == 0:
                    count = count + 1
                    if details:
                        print("b^(2^{}) is congruent to -1 mod n, so a = {} is not a Miller-Rabin witness".format(t, a))
                    continue 
                if details:
                    print("None of these are congruent to -1 mod n")
                print()
                print("n = {} is composite: Miller-Rabin witness a = {} for the compositeness of n = {}".format(n, a, n))
                return 
    print()
    print("n = {} is probably prime: no Miller-Rabin witness found in r = {} iterations".format(n, r))