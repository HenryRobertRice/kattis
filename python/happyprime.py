from math import ceil, sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_happy(n):
    if is_prime(n):
        prev = set()
        prev.add(n)
        while n != 1:
            n = sum([x ** 2 for x in [int(y) for y in list(str(n))]])
            if n in prev:
                return False
            prev.add(n)
        return True
    return False


def main():
    for _ in range(int(input())):
        k, m = map(int, input().split())
        print(f'{k} {m} {"YES" if is_happy(m) else "NO"}')


if __name__ == "__main__":
    main()
