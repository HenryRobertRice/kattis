def main():
    p, q, s = map(int, input().split())
    blinktime = p
    while blinktime <= s:
        if blinktime % q == 0:
            print("yes")
            return
        blinktime += p
    print("no")


if __name__ == "__main__":
    main()
