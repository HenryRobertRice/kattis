from sys import stdin, exit

def main():
    rows, cols, d1, d2 = set(), set(), set(), dict()
    n = int(stdin.readline())
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        if x in cols:
            print("INCORRECT")
            exit()
        else:
            cols.add(x)
        if y in rows:
            print("INCORRECT")
            exit()
        else:
            rows.add(y)
        temp = x + y
        if temp in d1:
            print("INCORRECT")
            exit()
        else:
            d1.add(temp)
        temp = abs(x - y)
        above = x > y
        if temp in d2 and (temp == 0 or len(d2[temp]) == 2 or d2[temp][0] == above):
            print("INCORRECT")
            exit()
        else:
            if temp in d2:
                d2[temp].append(above)
            else:
                d2[temp] = [above]
    print("CORRECT")

if __name__ == "__main__":
    main()
