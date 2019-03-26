total = 0.0
c, l = float(input()), input()
for i in range(l):
    h, v = [float(x) for x in raw_input().split()]
    total += h * v * c
print(total)
