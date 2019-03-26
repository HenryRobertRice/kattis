from math import ceil
a, i = [int(x) for x in raw_input().split()]
i = float(i) - 0.999
print(int(ceil(a * i)))
