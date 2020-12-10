def main():
    a, b, h = map(int, input().split())
    worm_height = 0
    climbs = 0
    while worm_height < h:
        worm_height += a
        climbs += 1
        if worm_height >= h:
            print(climbs)
            return
        worm_height -= b


if __name__ == "__main__":
    main()
