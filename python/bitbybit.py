def clear(reg, i):
    reg[int(i[1])] = "0"
    return reg
def sett(reg, i):
    reg[int(i[1])] = "1"
    return reg
def orr(reg, i):
    b1 = reg[int(i[1])]
    b2 = reg[int(i[2])]
    if b1 == "1" or b2 == "1":
        reg[int(i[1])] = "1"
    elif b1 == "?" or b2 == "?":
        reg[int(i[1])] = "?"
    return reg
def andd(reg, i):
    b1 = reg[int(i[1])]
    b2 = reg[int(i[2])]
    if b1 == "0" or b2 == "0":
        reg[int(i[1])] = "0"
    elif b1 == "?" or b2 == "?":
        reg[int(i[1])] = "?"
    return reg
def ex(reg, i):
    if i[0] == "CLEAR":
        reg = clear(reg, i)
    if i[0] == "SET":
        reg = sett(reg, i)
    if i[0] == "OR":
        reg = orr(reg, i)
    if i[0] == "AND":
        reg = andd(reg, i)
    return reg
while True:
    n = int(input())
    if n == 0:
        break
    reg = list("?" * 32)
    for i in range(n):
        reg = ex(reg, input().split())
    print("".join(reg)[::-1])
