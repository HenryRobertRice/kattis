x, y = [int(x[::-1]) for x in raw_input().split()]
if x > y:
    print(str(x))
else:
    print(str(y))
