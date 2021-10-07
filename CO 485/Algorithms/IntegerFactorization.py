import GCD

# N is assumed odd
def Pollard(N, B, a = 2, details = False):
    if details: 
        print("N = {}, B = {}, a = {}".format(N, B, a))
    for i in range(2, B+1):
        a = pow(a, i, N)
    n = GCD.GCD(a - 1, N)
    if details:
        print("a^(B!) (mod N) = {}".format(a))
        print("n = gcd(a^(B!) - 1, N) = {}".format(n))
    if n > 1 and n < N:
        print("n = {} is a nontrivial factor of N = {}".format(n, N))
    else:
        print("Failed to find a nontrivial factor of N = {}".format(N))