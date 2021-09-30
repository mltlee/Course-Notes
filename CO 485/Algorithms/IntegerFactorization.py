import GCD

# N is assumed odd
def Pollard(N, B):
    a = 2
    for i in range(2, B+1):
        a = pow(a, i, N)
    n = GCD.GCD(a - 1, N)
    if n > 1 and n < N:
        return "n = {} is a nontrivial factor of N = {}".format(n, N)
    else:
        return "failed to find a nontrivial factor of N = {}".format(N)
