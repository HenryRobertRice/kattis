x, y = map(int, input().split())
mario = set()
for _ in range(y):
    mario.add(int(input()))
for i in range(x):
    if i not in mario:
        print(i)
print("Mario got " + str(len(mario)) + " of the dangerous obstacles.")
