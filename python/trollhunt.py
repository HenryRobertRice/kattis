b, k, g = [int(x) for x in input().split()]
b -= 1
k //= g
i = 1
t = k
while True:
    if t >= b:
        print(str(i))
        break
    else:
        t += k
        i += 1
