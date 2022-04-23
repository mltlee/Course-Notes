def GCD(a, b):
    while True:
        a, b = b, a%b
        if (b == 1):
            return 1
        elif (b == 0):
            return a