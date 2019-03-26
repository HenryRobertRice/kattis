s, c, k = [int(x) for x in input().split()]
socks = [int(x) for x in input().split()]
socks.sort()
ctr = 1
wm = 0
for i in range(1, len(socks)):
    if ctr == c or socks[i] - socks[i - 1] > k:
        wm += 1
        ctr = 1
    else:
        ctr += 1
print(str(wm + 1))
