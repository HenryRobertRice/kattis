from math import ceil, sqrt
from sys import stdin

def main():
    for line in stdin:
        n = int(line)
        print(str(n) + " " + perfection(n))

def perfection(n):
    factors = [i for i in range(2, ceil(sqrt(n))) if n % i == 0]
    p = sum(factors) + sum([n // f for f in factors]) + 1
    if sqrt(n).is_integer():
        p += sqrt(n)
    if p == n:
        return "perfect"
    elif abs(p - n) <= 2:
        return "almost perfect"
    else:
        return "not perfect"

if __name__ == "__main__":
    main()
