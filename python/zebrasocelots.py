pile = []
for i in range(int(input())):
    pile.append(input())
for i in range(len(pile)):
    if pile[i] == "O":
        pile[i] = "1"
    else:
        pile[i] = "0"
print(str(int("".join(pile), base = 2)))
