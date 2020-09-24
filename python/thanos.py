def main():
    for _ in range(int(input())):
        p, r, f = map(int, input().split())
        print(analyze(p, r, f))


def analyze(p, r, f):
    i = 0
    while p <= f:
        p *= r
        i += 1
    return i


if __name__ == "__main__":
    main()
