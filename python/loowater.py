def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        heads = [int(input()) for _ in range(n)]
        knights = [int(input()) for _ in range(m)]
        heads.sort()
        knights.sort()
        index = 0
        cost = 0
        fail = False
        for h in heads:
            while not fail:
                if index == len(knights):
                    fail = True
                    break
                if knights[index] >= h:
                    cost += knights[index]
                    index += 1
                    break
                index += 1
        if not fail:
            print(cost)
        else:
            print("Loowater is doomed!")

if __name__ == "__main__":
    main()
