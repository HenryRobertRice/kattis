trash = input()
p1 = [int(x) for x in input().split()]
p2 = []
moves = 0
#if p1 empty, end
#else if p2 empty, pop p1 to p2
#else if p2 not empty, check for match
#  if match, pop p1 and p2 to void
m = 0
while p1:
    if p2 and p1[-1] == p2[-1]:
        p1.pop()
        p2.pop()
    else:
        p2.append(p1.pop())
    m += 1
if p2:
    print("impossible")
else:
    print(str(m))
