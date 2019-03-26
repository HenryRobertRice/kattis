b = [int(i) for i in range(1, int(input()) + 1)]
c= [int(x) for x in input().split()]
c.sort()
for i in range(len(b)):
    if c[i] > b[i]:
        print("impossible")
        exit()
    c[i] /= b[i]
print(str(min(c)))
