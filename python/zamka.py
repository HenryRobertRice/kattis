def sum_dig(i):
    out = 0
    while i:
        out, i = out + i % 10, i // 10
    return out
l, d, x = input(), input(), input()
for i in range(l, d + 1):
    if sum_dig(i) == x:
        print(i)
        break
for i in range(d, l - 1, -1):
    if sum_dig(i) == x:
        print(i)
        break
