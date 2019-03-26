from sys import exit
while True:
    temp = input()
    if temp[0] == "0":
        exit()
    k, m = [int(x) for x in temp.split()]
    fred = set(input().split())
    out = True
    for i in range(m):
        cat = input().split()
        req = int(cat[1])
        cat = set(cat[2:])
        for course in cat:
            if course in fred:
                req -= 1
        if req > 0:
            out = False
    if out:
        print("yes")
    else:
        print("no")

