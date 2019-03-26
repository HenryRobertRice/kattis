from math import sqrt, ceil
def isPrime(num):
    if num == 2:
        return True
    for i in range(2, int(ceil(sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True

primes = set()

for i in range(2, 32001):
    if isPrime(i):
        primes.add(i)

for i in range(int(input())):
    num = int(input())
    pairs = []
    for j in range(2, num // 2 + 1):
        if j in primes and (num - j) in primes:
            pairs.append((j, num - j))
    print(str(num) + " has " + str(len(pairs)) + " representation(s)")
    for pair in pairs:
        print(str(pair[0]) +  "+" + str(pair[1]))
    print()
