from math import sqrt
m, w, h = [int(x) for x in raw_input().split()]
d = sqrt(w ** 2 + h ** 2)
for i in range(m):
  if(int(input()) <= d):
    print("DA")
  else:
    print("NE")
