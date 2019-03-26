def conv(b, n):
    out = []
    while n:
        out.append(n % b)
        n //= b
    return out
def ssd(n):
    out = 0
    for c in n:
        out += int(c) ** 2
    return out
for i in range(input()):
    f, b, n = [int(x) for x in raw_input().split()]
    print(str(f) + " " + str(ssd(conv(b, n))))
