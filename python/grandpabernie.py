def main():
    log = dict()
    for _ in range(int(input())):
        location, year = input().split()
        year = int(year)
        if location not in log:
            log[location] = [year]
        else:
            temp = log[location]
            temp.append(year)
            log[location] = temp
    for location in log:
        temp = log[location]
        temp.sort()
        log[location] = temp
    for _ in range(int(input())):
        location, n = input().split()
        n = int(n)
        print(log[location][n - 1])

if __name__ == "__main__":
    main()
