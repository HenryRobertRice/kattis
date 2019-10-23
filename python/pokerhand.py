hand = input().split()
mydict = dict()
for h in hand:
    if h[0] not in mydict:
        mydict[h[0]] = 1
    else:
        mydict[h[0]] = mydict[h[0]] + 1
max_ = 0
for d in mydict:
    if mydict[d] > max_:
        max_ = mydict[d]
print(max_)
