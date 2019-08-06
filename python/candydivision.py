from math import sqrt
n = int(input())
higher_factors = []
all_factors = []
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        if n / i == i:
            all_factors.append(i)
        else:
            all_factors.append(i)
            higher_factors.append(n // i)
all_factors.extend(higher_factors[::-1])
print(" ".join([str(x - 1) for x in all_factors]))
