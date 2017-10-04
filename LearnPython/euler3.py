import math


def prime_factor(n):
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            return False
        else:
            i += 1
    return True


t = int(raw_input().strip())
for a0 in range(t):
    n = int(raw_input().strip())
    if prime_factor(n):
        print (n)
    else:
        i = int(n / 2) + 1
        while True:
            if n % i == 0 and prime_factor(i):
                print i
                break
            else:
                i -= 1
