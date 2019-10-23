tb, lr = 0, 0
for _ in range(int(input())):
    temp = input()
    if temp[0] == "0":
        tb += 1
    if temp[1] == "0":
        tb += 1
    if temp[2] == "0":
        lr += 1
    if temp[3] == "0":
        lr += 1
limit = min(tb, lr)
swords = limit // 2
tb -= swords * 2
lr -= swords * 2
print(str(swords) + " " + str(tb) + " " + str(lr))
