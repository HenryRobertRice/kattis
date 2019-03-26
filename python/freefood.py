days = set()
for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    for j in range(x, y + 1):
        days.add(j)
print(str(len(days)))
