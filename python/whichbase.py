def main():
    for _ in range(int(input())):
        k, d = input().split()
        try:
            o = int(d, 8)
        except ValueError:
            o = 0
        h = int(d, 16)
        d = int(d)
        print(k, o, d, h)


if __name__ == "__main__":
    main()
